#!/usr/bin/env python3

from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path
from string import Template


REPO_ROOT = Path(__file__).resolve().parents[1]
PROFILE_PATH = REPO_ROOT / "scripts" / "cover_letter_profile.json"
TEMPLATE_PATH = REPO_ROOT / "scripts" / "templates" / "coverletter-generated.tex.tmpl"
DEFAULT_OUTPUT_PREFIX = REPO_ROOT / "output" / "coverletter-generated"


LATEX_REPLACEMENTS = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a tailored cover letter from a job description URL or text."
    )
    parser.add_argument("--company", required=True, help="Target company name")
    parser.add_argument("--role", required=True, help="Role title from the job posting")
    parser.add_argument(
        "--company-address",
        default="Company Address",
        help="Optional address line shown in the cover letter header",
    )
    parser.add_argument(
        "--track",
        choices=["auto", "qa-lead", "qa-automation", "devops-platform"],
        default="auto",
        help="Force a template track or let the script infer it",
    )
    parser.add_argument(
        "--output-prefix",
        default=str(DEFAULT_OUTPUT_PREFIX),
        help="Output path without extension, default: output/coverletter-generated",
    )
    parser.add_argument(
        "--no-compile",
        action="store_true",
        help="Generate the .tex file only and skip PDF compilation",
    )

    source_group = parser.add_mutually_exclusive_group(required=True)
    source_group.add_argument("--job-url", help="URL of the job posting")
    source_group.add_argument("--job-file", help="Path to a text or HTML file with the job posting")
    source_group.add_argument("--job-text", help="Inline job description text")
    return parser.parse_args()


def load_profile() -> dict:
    return json.loads(PROFILE_PATH.read_text(encoding="utf-8"))


def latex_escape(value: str) -> str:
    escaped = value
    for old, new in LATEX_REPLACEMENTS.items():
        escaped = escaped.replace(old, new)
    return escaped


def collapse_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def strip_html(raw_html: str) -> str:
    text = re.sub(r"(?is)<script.*?>.*?</script>", " ", raw_html)
    text = re.sub(r"(?is)<style.*?>.*?</style>", " ", text)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    text = html.unescape(text)
    return collapse_ws(text)


def read_job_text(args: argparse.Namespace) -> tuple[str, str]:
    if args.job_text:
        return args.job_text, "inline"
    if args.job_file:
        path = Path(args.job_file).expanduser().resolve()
        raw = path.read_text(encoding="utf-8")
        if path.suffix.lower() in {".html", ".htm"}:
            return strip_html(raw), str(path)
        return collapse_ws(raw), str(path)
    request = urllib.request.Request(
        args.job_url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; CoverLetterGenerator/1.0)"},
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        payload = response.read()
        content_type = response.headers.get("Content-Type", "")
        charset = response.headers.get_content_charset() or "utf-8"
    raw = payload.decode(charset, errors="replace")
    if "html" in content_type or "<html" in raw.lower():
        return strip_html(raw), args.job_url
    return collapse_ws(raw), args.job_url


def infer_track(job_text: str, profile: dict, forced_track: str) -> str:
    if forced_track != "auto":
        return forced_track

    haystack = job_text.lower()
    scores: dict[str, int] = {}
    for track_name, config in profile["tracks"].items():
        score = 0
        for signal in config["signals"]:
            if signal in haystack:
                score += 2
        for keyword in config["keywords"]:
            if keyword in haystack:
                score += 1
        scores[track_name] = score

    best_track, best_score = max(scores.items(), key=lambda item: item[1])
    return best_track if best_score > 0 else "qa-automation"


def collect_matches(job_text: str, terms: list[str], limit: int = 6) -> list[str]:
    haystack = job_text.lower()
    matches: list[str] = []
    for term in terms:
        if term.lower() in haystack:
            matches.append(term)
    return matches[:limit]


def collect_domains(job_text: str, profile: dict, limit: int = 3) -> list[str]:
    haystack = job_text.lower()
    matches: list[str] = []
    for needle, label in profile["shared"]["domains"].items():
        if needle in haystack:
            matches.append(label)
    return matches[:limit]


def natural_join(items: list[str]) -> str:
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} and {items[1]}"
    return f"{', '.join(items[:-1])}, and {items[-1]}"


def sentence_case_track_label(track_config: dict) -> str:
    return track_config["label"]


def build_paragraphs(
    company: str,
    role: str,
    profile: dict,
    track_name: str,
    job_text: str,
) -> tuple[str, str, str, list[str], list[str]]:
    track = profile["tracks"][track_name]
    matches = collect_matches(job_text, track["keywords"] + profile["shared"]["common_skills"])
    domains = collect_domains(job_text, profile)

    paragraph_1 = Template(track["intro"]).substitute(
        company=company,
        role=role,
        current_roles=profile["shared"]["current_roles"],
    )

    extras: list[str] = []
    if matches:
        extras.append(
            f"The strongest overlap with your role includes {natural_join(matches)}."
        )
    if domains:
        extras.append(
            f"I have also worked in environments related to {natural_join(domains)}."
        )
    paragraph_2 = " ".join([track["body"], *extras]).strip()

    paragraph_3 = Template(track["closing"]).substitute(company=company)
    return paragraph_1, paragraph_2, paragraph_3, matches, domains


def render_tex(
    template: Template,
    profile: dict,
    company: str,
    company_address: str,
    role: str,
    paragraphs: tuple[str, str, str],
) -> str:
    person = profile["person"]
    paragraph_1, paragraph_2, paragraph_3 = paragraphs
    return template.substitute(
        first_name=latex_escape(person["first_name"]),
        last_name=latex_escape(person["last_name"]),
        position=person["position"],
        address=latex_escape(person["address"]),
        mobile=latex_escape(person["mobile"]),
        email=latex_escape(person["email"]),
        homepage=latex_escape(person["homepage"]),
        github=latex_escape(person["github"]),
        linkedin=latex_escape(person["linkedin"]),
        quote=person["quote"],
        photo_path=person["photo_path"],
        company=latex_escape(company),
        company_address=latex_escape(company_address),
        role=latex_escape(role),
        paragraph_1=latex_escape(paragraph_1),
        paragraph_2=latex_escape(paragraph_2),
        paragraph_3=latex_escape(paragraph_3),
    )


def compile_pdf(tex_path: Path) -> None:
    subprocess.run(
        ["lualatex", "-output-directory", str(tex_path.parent), str(tex_path)],
        cwd=REPO_ROOT,
        check=True,
    )


def write_metadata(
    prefix: Path,
    source: str,
    track_name: str,
    track_label: str,
    matches: list[str],
    domains: list[str],
) -> None:
    metadata = {
        "source": source,
        "track": track_name,
        "track_label": track_label,
        "matched_keywords": matches,
        "matched_domains": domains,
    }
    prefix.with_suffix(".json").write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    args = parse_args()
    profile = load_profile()
    template = Template(TEMPLATE_PATH.read_text(encoding="utf-8"))
    job_text, source = read_job_text(args)
    output_prefix = Path(args.output_prefix)
    if not output_prefix.is_absolute():
        output_prefix = (REPO_ROOT / output_prefix).resolve()
    output_prefix.parent.mkdir(parents=True, exist_ok=True)

    track_name = infer_track(job_text, profile, args.track)
    paragraph_1, paragraph_2, paragraph_3, matches, domains = build_paragraphs(
        company=args.company,
        role=args.role,
        profile=profile,
        track_name=track_name,
        job_text=job_text,
    )

    tex_path = output_prefix.with_suffix(".tex")
    pdf_path = output_prefix.with_suffix(".pdf")
    tex_content = render_tex(
        template=template,
        profile=profile,
        company=args.company,
        company_address=args.company_address,
        role=args.role,
        paragraphs=(paragraph_1, paragraph_2, paragraph_3),
    )
    tex_path.write_text(tex_content, encoding="utf-8")
    write_metadata(
        prefix=output_prefix,
        source=source,
        track_name=track_name,
        track_label=sentence_case_track_label(profile["tracks"][track_name]),
        matches=matches,
        domains=domains,
    )

    if not args.no_compile:
        compile_pdf(tex_path)

    print(f"Generated TeX: {tex_path}")
    if not args.no_compile:
        print(f"Generated PDF: {pdf_path}")
    print(f"Selected track: {track_name}")
    if matches:
        print(f"Matched keywords: {', '.join(matches)}")
    if domains:
        print(f"Matched domains: {', '.join(domains)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
