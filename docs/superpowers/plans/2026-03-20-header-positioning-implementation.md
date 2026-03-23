# Header Positioning Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Update the top-level profile positioning in CV, resume, and ATS so the candidate is presented as `QA Lead`, then `Senior Full Stack Engineer`, then `AI-Native Developer`, while keeping historical experience titles unchanged.

**Architecture:** This is a focused copy update across the title/header layer and summary layer only. The work should modify the profile framing in `cv.tex`, `resume.tex`, `resume/summary.tex`, and `cv-ats.tex`, then rebuild the generated PDFs and verify the ATS still stays within the intended layout constraints.

**Tech Stack:** LaTeX, Awesome CV, LuaLaTeX, `pdftotext`, `pdfinfo`

---

### Task 1: Update Header Titles

**Files:**
- Modify: `examples/cv.tex`
- Modify: `examples/resume.tex`
- Modify: `examples/cv-ats.tex`

- [ ] **Step 1: Update the full CV header title**

Change the `\position{...}` line in `examples/cv.tex` to:

```tex
\position{QA Lead{\enskip\cdotp\enskip}Senior Full Stack Engineer{\enskip\cdotp\enskip}AI-Native Developer}
```

- [ ] **Step 2: Update the resume header title**

Change the `\position{...}` line in `examples/resume.tex` to:

```tex
\position{QA Lead{\enskip\cdotp\enskip}Senior Full Stack Engineer{\enskip\cdotp\enskip}AI-Native Developer}
```

- [ ] **Step 3: Update the ATS header title**

Change the top title line in `examples/cv-ats.tex` to:

```tex
{\large QA Lead | Senior Full Stack Engineer | AI-Native Developer}\par
```

### Task 2: Update Summary Framing

**Files:**
- Modify: `examples/resume/summary.tex`
- Modify: `examples/cv-ats.tex`

- [ ] **Step 1: Rewrite the resume summary**

Replace the current summary in `examples/resume/summary.tex` so it:

- starts from `QA Lead`
- explicitly includes `Senior Full Stack Engineer`
- explicitly includes `AI-Native Developer`
- keeps the rest concise and engineering-first

Target direction:

```text
QA Lead, Senior Full Stack Engineer, and AI-Native Developer ...
```

- [ ] **Step 2: Rewrite the ATS summary**

Replace the current ATS summary in `examples/cv-ats.tex` so it:

- starts from `QA Lead`
- removes narrow `QA Automation Engineer` framing
- adds `Senior Full Stack Engineer` and `AI-Native Developer`
- keeps hands-on Node.js / Python / Django / platform wording visible

### Task 3: Rebuild PDFs

**Files:**
- Modify: `examples/cv.pdf`
- Modify: `examples/resume.pdf`
- Modify: `examples/cv-ats.pdf`

- [ ] **Step 1: Rebuild all affected PDFs**

Run:

```bash
make cv.pdf resume.pdf cv-ats.pdf
```

Expected:
- exit code `0`
- regenerated `examples/cv.pdf`
- regenerated `examples/resume.pdf`
- regenerated `examples/cv-ats.pdf`

### Task 4: Verify Positioning and Layout

**Files:**
- Test: `examples/cv.pdf`
- Test: `examples/resume.pdf`
- Test: `examples/cv-ats.pdf`

- [ ] **Step 1: Verify updated header/title text in extracted PDFs**

Run:

```bash
pdftotext examples/cv.pdf - | rg "QA Lead|Senior Full Stack Engineer|AI-Native Developer"
pdftotext examples/resume.pdf - | rg "QA Lead|Senior Full Stack Engineer|AI-Native Developer"
pdftotext examples/cv-ats.pdf - | rg "QA Lead|Senior Full Stack Engineer|AI-Native Developer"
```

Expected:
- each command exits with code `0`
- old `QA Automation Engineer` header wording is gone from ATS

- [ ] **Step 2: Verify ATS summary wording and page count**

Run:

```bash
pdftotext examples/cv-ats.pdf - | sed -n '1,40p'
pdfinfo examples/cv-ats.pdf | rg '^Pages:'
```

Expected:
- ATS summary reflects the new engineering-first framing
- ATS stays at `2` pages

- [ ] **Step 3: Review source diff**

Run:

```bash
git diff -- examples/cv.tex examples/resume.tex examples/resume/summary.tex examples/cv-ats.tex
```

Expected:
- diff only shows the intended header and summary repositioning changes
