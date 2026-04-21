# CKSource Applied AI Cover Letter Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extend the local cover letter generator with an `applied-ai` variant and generate a concrete, technical cover letter for the `Principal Applied AI Engineer` role at `CKSource`.

**Architecture:** Keep the scope centered on the existing generator workflow instead of adding a one-off handwritten file. Add a new `applied-ai` track in the JSON profile, make the generator aware of it, avoid the current overly generic keyword-overlap sentence for this track, then render a named output artifact for CKSource under `output/`.

**Tech Stack:** Python 3, JSON, LaTeX, LuaLaTeX, `unittest`, `pdftotext`

---

### Task 1: Add Regression Coverage for the New AI Track

**Files:**
- Create: `tests/test_generate_cover_letter.py`

- [ ] **Step 1: Create a focused unittest module for track inference and paragraph content**

Create `tests/test_generate_cover_letter.py` with two regression checks:

```python
import importlib.util
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "scripts" / "generate_cover_letter.py"
SPEC = importlib.util.spec_from_file_location("generate_cover_letter", SCRIPT_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class GenerateCoverLetterTests(unittest.TestCase):
    def test_infer_track_prefers_applied_ai_for_agentic_backend_role(self) -> None:
        profile = MODULE.load_profile()
        job_text = (
            "Principal Applied AI Engineer. Build systems involving LLMs, "
            "integrations, multi-step or agentic workflows, internal tools, "
            "TypeScript, Node.js, backend engineering."
        )
        self.assertEqual(MODULE.infer_track(job_text, profile, "auto"), "applied-ai")

    def test_build_paragraphs_for_applied_ai_are_explicit_and_not_generic(self) -> None:
        profile = MODULE.load_profile()
        job_text = (
            "AI-assisted development systems, internal tools, TypeScript, "
            "Node.js, LLM workflows, backend systems."
        )
        paragraph_1, paragraph_2, paragraph_3, matches, domains = MODULE.build_paragraphs(
            "CKSource",
            "Principal Applied AI Engineer",
            profile,
            "applied-ai",
            job_text,
        )
        combined = " ".join([paragraph_1, paragraph_2, paragraph_3])
        self.assertIn("Lexense.ai", combined)
        self.assertIn("Node.js", combined)
        self.assertIn("LLM", combined)
        self.assertIn("CKSource", combined)
        self.assertNotIn("The strongest overlap with your role includes", combined)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the new tests before implementation**

Run:

```bash
python3 -m unittest tests/test_generate_cover_letter.py -v
```

Expected:
- exit code is non-zero before implementation
- one failure shows the inferred track is not yet `applied-ai`
- one failure or error shows the new track content does not exist yet

### Task 2: Implement the Applied AI Generator Track

**Files:**
- Modify: `scripts/cover_letter_profile.json`
- Modify: `scripts/generate_cover_letter.py`
- Modify: `README.md`
- Test: `tests/test_generate_cover_letter.py`

- [ ] **Step 1: Add a new `applied-ai` track to the profile**

Extend `scripts/cover_letter_profile.json` with an `applied-ai` entry under `tracks` using signals and wording aligned with the approved spec.

Target shape:

```json
"applied-ai": {
  "label": "Applied AI Engineer",
  "signals": [
    "applied ai",
    "ai engineer",
    "llm",
    "agentic",
    "ai-assisted development",
    "internal tools",
    "developer tooling",
    "node.js",
    "typescript",
    "backend"
  ],
  "keywords": [
    "node.js",
    "typescript",
    "llm",
    "rag",
    "openai",
    "automation",
    "agentic workflows",
    "backend",
    "internal tools",
    "developer tooling"
  ],
  "include_overlap_summary": false,
  "intro": "I am applying for the ${role} position at ${company}. My work combines AI-native product engineering, backend system design, and hands-on delivery across product systems and internal engineering workflows.",
  "body": "At Lexense.ai I architected an AI-native legal platform across mobile, web, extension, backend, and knowledge services, designing the system around Node.js / NestJS, OpenAI, RAG, OCR, document analysis, and conversational workflows, with self-hosted infrastructure, observability, CI/CD, and secure handling of sensitive data. At Efectivo / Humanit Group I designed LLM-powered agents for test automation and built LLM + RAG documentation workflows to improve internal engineering efficiency.",
  "closing": "I would bring to ${company} a pragmatic applied AI profile: identify where AI or automation creates real value, design the system end to end, and ship maintainable solutions in production-oriented Node.js / TypeScript environments."
}
```

- [ ] **Step 2: Teach the generator about the new track and optional overlap suppression**

Update `scripts/generate_cover_letter.py` so:

```python
choices=["auto", "qa-lead", "qa-automation", "devops-platform", "applied-ai"]
```

and `build_paragraphs()` only appends the keyword-overlap sentence when the track configuration allows it:

```python
include_overlap_summary = track.get("include_overlap_summary", True)

extras: list[str] = []
if include_overlap_summary and matches:
    extras.append(
        f"The strongest overlap with your role includes {natural_join(matches)}."
    )
if include_overlap_summary and domains:
    extras.append(
        f"I have also worked in environments related to {natural_join(domains)}."
    )
```

- [ ] **Step 3: Update CLI documentation**

Update the optional flags section in `README.md` so it lists:

```text
--track qa-lead|qa-automation|devops-platform|applied-ai
```

and add one short example command for an AI-oriented role if the README section still reads clearly after the change.

- [ ] **Step 4: Re-run the regression tests**

Run:

```bash
python3 -m unittest tests/test_generate_cover_letter.py -v
```

Expected:
- exit code `0`
- `applied-ai` is selected for the AI-heavy sample posting
- generated applied AI paragraphs contain the explicit narrative and omit the generic overlap sentence

### Task 3: Generate the CKSource-Specific Cover Letter

**Files:**
- Modify: `output/cksource-applied-ai.tex`
- Modify: `output/cksource-applied-ai.pdf`
- Modify: `output/cksource-applied-ai.json`

- [ ] **Step 1: Render the CKSource cover letter with the new track**

Run:

```bash
python3 scripts/generate_cover_letter.py \
  --company "CKSource" \
  --role "Principal Applied AI Engineer" \
  --job-url "https://justjoin.it/job-offer/cksource-principal-applied-ai-engineer-wroclaw-ai" \
  --track applied-ai \
  --output-prefix output/cksource-applied-ai
```

Expected:
- exit code `0`
- files written to:
  - `output/cksource-applied-ai.tex`
  - `output/cksource-applied-ai.pdf`
  - `output/cksource-applied-ai.json`

- [ ] **Step 2: Inspect the generated source for the approved narrative**

Run:

```bash
sed -n '1,220p' output/cksource-applied-ai.tex
```

Expected:
- opening paragraph frames Wojciech as a hands-on applied AI engineer
- body paragraph references `Lexense.ai`, `Node.js / NestJS`, `OpenAI`, `RAG`, `OCR`, and `LLM` agent work at `Efectivo / Humanit Group`
- closing paragraph emphasizes pragmatic end-to-end delivery
- the phrase `The strongest overlap with your role includes` does not appear

### Task 4: Verify PDF and Metadata Output

**Files:**
- Test: `output/cksource-applied-ai.tex`
- Test: `output/cksource-applied-ai.pdf`
- Test: `output/cksource-applied-ai.json`

- [ ] **Step 1: Verify extracted PDF text contains the expected signals**

Run:

```bash
pdftotext output/cksource-applied-ai.pdf - | rg "CKSource|Principal Applied AI Engineer|Lexense.ai|Node.js|LLM|RAG|CI/CD|observability"
```

Expected:
- command exits with code `0`
- extracted text shows the technical positioning approved in the spec

- [ ] **Step 2: Verify metadata and source scope**

Run:

```bash
cat output/cksource-applied-ai.json
git diff -- scripts/generate_cover_letter.py scripts/cover_letter_profile.json README.md tests/test_generate_cover_letter.py
```

Expected:
- metadata shows track `applied-ai`
- tracked source diff is limited to the generator, profile, README, and test file
- no unrelated repository files are changed
