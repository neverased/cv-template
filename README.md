<h1 align="center">
  <a href="https://github.com/posquit0/Awesome-CV" title="AwesomeCV Documentation">
    <img alt="AwesomeCV" src="https://github.com/posquit0/Awesome-CV/raw/master/icon.png" width="200px" height="200px" />
  </a>
  <br />
  Awesome CV
</h1>

<p align="center">
  LaTeX template for your outstanding job application
</p>

<br />

## What is Awesome CV?

**Awesome CV** is LaTeX template for a **CV(Curriculum Vitae)**, **Résumé** or **Cover Letter** inspired by [Fancy CV](https://www.sharelatex.com/templates/cv-or-resume/fancy-cv). It is easy to customize your own template, especially since it is really written by a clean, semantic markup.

## Personal CVs

The application profiles are **QA Lead / Test Manager** and **Senior QA Automation Engineer**. All four PDFs have two pages and a single text column. The main QA Lead CV includes a portrait and expanded Lexense AI engineering and verification experience; its plain ATS version remains more concise. The two automation versions have identical content. All use distribution-provided TeX Gyre Heros fonts and a shared base layout. The Awesome CV class is still used by the cover letters.

Build and refresh the four PDFs in `examples/`, then copy clearly named application files to `output/pdf/`:

```bash
make application-pdfs CC='lualatex -interaction=nonstopmode -halt-on-error'
```

| Profile | Main entry point | Plain entry point | Shared content |
| --- | --- | --- | --- |
| QA Lead / Test Manager | `examples/cv.tex` (photo and AI focus) | `examples/cv-ats.tex` | `examples/cv/` |
| QA Automation | `examples/resume.tex` | `examples/cv-ats-qa-automation.tex` | `examples/resume/` |

Base contact details and typography are in `examples/shared/layout.tex`; the main CV overrides the header in `examples/cv/photo-header.tex` using `examples/profile-wb.png`. Names, role titles, dates, languages and the release improvement statement are in `examples/shared/profile.tex`. The main CV uses `summary-ai.tex`, `skills-ai.tex` and `experience-ai.tex` in `examples/cv/`, with compact earlier experience and education. Other versions use the original profile sections and shared earlier experience, education and certifications.

Edit shared facts rather than copying them into the entry points. Historical role titles and dates must remain accurate when tailoring the headline. See `docs/cv-revision-2026-09-07.md` for the initial audit corrections and `docs/cv-ai-update-2026-09-07.md` for the subsequent main-CV expansion and verification.

## Upstream template preview

#### Résumé

You can see [PDF](https://raw.githubusercontent.com/posquit0/Awesome-CV/master/examples/resume.pdf)

| Page. 1 | Page. 2 |
|:---:|:---:|
| [![Résumé](https://raw.githubusercontent.com/posquit0/Awesome-CV/master/examples/resume-0.png)](https://raw.githubusercontent.com/posquit0/Awesome-CV/master/examples/resume.pdf)  | [![Résumé](https://raw.githubusercontent.com/posquit0/Awesome-CV/master/examples/resume-1.png)](https://raw.githubusercontent.com/posquit0/Awesome-CV/master/examples/resume.pdf) |

#### Cover Letter

You can see [PDF](https://raw.githubusercontent.com/posquit0/Awesome-CV/master/examples/coverletter.pdf)

| Without Sections | With Sections |
|:---:|:---:|
| [![Cover Letter(Traditional)](https://raw.githubusercontent.com/posquit0/Awesome-CV/master/examples/coverletter-0.png)](https://raw.githubusercontent.com/posquit0/Awesome-CV/master/examples/coverletter.pdf)  | [![Cover Letter(Awesome)](https://raw.githubusercontent.com/posquit0/Awesome-CV/master/examples/coverletter-1.png)](https://raw.githubusercontent.com/posquit0/Awesome-CV/master/examples/coverletter.pdf) |

## How to Use

#### Requirements

A current TeX Live 2026 distribution with LuaLaTeX is recommended. The template uses [Font Awesome 7](https://ctan.org/pkg/fontawesome7), version 7.3.1-1 (2026-08-09) or newer. For an upstream TeX Live or MacTeX installation, update the package manager and packages before building:

```bash
tlmgr update --self --all
tlmgr install fontawesome7
```

For a package-manager-owned TeX installation (for example Homebrew), use that package manager to update TeX Live, or use the Docker command below. The CI build updates all TeX packages before compiling.

Roboto and Source Sans 3 are optional system fonts; the class falls back to TeX Gyre Heros when they are unavailable. The Python cover letter generator uses only the standard library and has no third-party Python packages to update.

If you don't want to install the dependencies on your system, this can also be obtained via [Docker](https://docker.com).

#### Usage

At a command prompt, run

```bash
make CC='lualatex -interaction=nonstopmode -halt-on-error'
```

Or using docker:

```bash
docker run --rm --pull=always -i -w /doc -v "$PWD":/doc texlive/texlive:latest \
  sh -ec 'tlmgr update --self --all; make CC="lualatex -interaction=nonstopmode -halt-on-error"'
```

Both commands compile all eight variants into `examples/*.pdf`.

## Tailored Cover Letter Generator

This repo also includes a local generator that creates a tailored cover letter from a job description URL or text and compiles it to PDF.

Examples:

```bash
python3 scripts/generate_cover_letter.py \
  --company "Acme" \
  --role "Senior QA Automation Engineer" \
  --job-file /path/to/job-description.txt
```

```bash
python3 scripts/generate_cover_letter.py \
  --company "Acme" \
  --role "Platform Engineer" \
  --job-url "https://example.com/jobs/platform-engineer"
```

```bash
python3 scripts/generate_cover_letter.py \
  --company "Acme" \
  --role "Principal Applied AI Engineer" \
  --job-url "https://example.com/jobs/applied-ai-engineer" \
  --track applied-ai
```

Optional flags:

- `--track qa-lead|qa-automation|devops-platform|applied-ai` to force a specific variant
- `--company-address "Street, City"` to change the header block
- `--output-prefix output/acme-platform` to choose output paths
- `--no-compile` to generate only the `.tex` file

By default the script writes:

- `output/coverletter-generated.tex`
- `output/coverletter-generated.pdf`
- `output/coverletter-generated.json`

## Credit

[**LaTeX**](https://www.latex-project.org) is a fantastic typesetting program that a lot of people use these days, especially the math and computer science people in academia.

[**FontAwesome7 LaTeX Package**](https://github.com/braniii/fontawesome) is a LaTeX package that provides access to the [Font Awesome 7](https://fontawesome.com/icons) icon set.

[**Roboto**](https://github.com/google/roboto) is the default font on Android and ChromeOS, and the recommended font for Google’s visual language, Material Design.

[**Source Sans Pro**](https://github.com/adobe-fonts/source-sans-pro) is a set of OpenType fonts that have been designed to work well in user interface (UI) environments.

## Contact

You are free to take my `.tex` file and modify it to create your own resume. Please don't use my resume for anything else without my permission, though!

Good luck!
