# QA Lead CV Repositioning Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild the CV package so `examples/cv.tex` and `examples/cv-ats.tex` become focused `QA Lead` variants, `examples/resume.tex` becomes the `QA Automation Specialist` variant, and a new `examples/cv-ats-qa-automation.tex` provides a dedicated automation ATS document.

**Architecture:** Keep the existing Awesome CV / ATS split, but stop trying to make one story serve every role. The implementation should create one dominant `QA Lead` narrative for the main CV and main ATS, one narrower `QA Automation Specialist` narrative for the short resume and automation ATS, and reposition `Lexense` as a secondary after-hours proof of systems depth rather than the main commercial identity.

**Tech Stack:** LaTeX, Awesome CV, LuaLaTeX, XeLaTeX-compatible source structure, Make, `pdftotext`, `pdfinfo`

---

## File Map

- Create: `examples/cv/summary.tex`
- Create: `examples/cv-ats-qa-automation.tex`
- Modify: `examples/cv.tex`
- Modify: `examples/cv/skills.tex`
- Modify: `examples/cv/experience.tex`
- Modify: `examples/cv-ats.tex`
- Modify: `examples/resume.tex`
- Modify: `examples/resume/summary.tex`
- Modify: `examples/resume/skills.tex`
- Modify: `examples/resume/experience.tex`
- Modify: `Makefile`
- Modify: `examples/cv.pdf`
- Modify: `examples/cv-ats.pdf`
- Modify: `examples/resume.pdf`
- Modify: `examples/cv-ats-qa-automation.pdf`

### Task 1: Rebuild the Main Full CV Structure Around QA Lead

**Files:**
- Create: `examples/cv/summary.tex`
- Modify: `examples/cv.tex`

- [ ] **Step 1: Add the new full-CV summary section**

Create `examples/cv/summary.tex` with the exact summary block below:

```tex
%-------------------------------------------------------------------------------
%	SECTION TITLE
%-------------------------------------------------------------------------------
\cvsection{Summary}


%-------------------------------------------------------------------------------
%	CONTENT
%-------------------------------------------------------------------------------
\begin{cvparagraph}

Hands-on QA Lead with commercial experience across API, customer-hosted servers, backend, frontend, mobile, end-to-end, and infrastructure workflows. Currently line-managing a 5-person QA team at Efectivo / Humanit Group, owning QA strategy, QA minima, release readiness, and quality metrics across an ecosystem spanning 6-8 product and platform layers. Built and maintained dozens of E2E and API scenarios, reduced regression and release validation by more than 1 day, cut manual verification effort by 30%+, and supported several releases per month. Additional after-hours product work at Lexense.ai strengthens backend, infrastructure, and architecture depth without changing the primary QA focus.
\end{cvparagraph}
```

- [ ] **Step 2: Narrow the main title and reorder the section inputs**

Update `examples/cv.tex` so the position line and content inputs become:

```tex
\position{QA Lead{\enskip\cdotp\enskip}Test Strategy{\enskip\cdotp\enskip}Automation{\enskip\cdotp\enskip}API{\enskip\cdotp\enskip}CI/CD}
```

and

```tex
\input{cv/summary.tex}
\input{cv/skills.tex}
\input{cv/experience.tex}
\input{cv/education.tex}
\input{cv/certificates.tex}
\newpage
\input{cv/extracurricular.tex}
\input{cv/presentation.tex}
```

This step should remove the old pattern where education appears before skills and experience.

- [ ] **Step 3: Verify the source now reflects the new structure**

Run:

```bash
rg -n "\\\\position|\\\\input\\{cv/" examples/cv.tex
sed -n '1,220p' examples/cv/summary.tex
```

Expected:
- `examples/cv.tex` shows the new `QA Lead ... CI/CD` title
- `examples/cv.tex` loads `cv/summary.tex` before `cv/skills.tex`
- `examples/cv/summary.tex` exists and contains the new QA Lead summary text

- [ ] **Step 4: Commit the structural QA Lead CV entry-point changes**

Run:

```bash
git add examples/cv.tex examples/cv/summary.tex
git commit -m "feat(cv): restructure full CV around QA lead profile"
```

Expected:
- commit succeeds
- only the full CV entry-point files are included

### Task 2: Rewrite the Main Full CV Skills and Experience

**Files:**
- Modify: `examples/cv/skills.tex`
- Modify: `examples/cv/experience.tex`

- [ ] **Step 1: Replace the full-CV skills matrix with QA-centric categories**

Rewrite `examples/cv/skills.tex` so the `cvskills` block becomes:

```tex
\begin{cvskills}

  \cvskill
    {QA Leadership \& Strategy}
    {QA Strategy, QA Minima, Release Readiness, Quality Metrics, Test Planning, Test Architecture, Cross-Functional Leadership}

  \cvskill
    {Test Automation \& QA Engineering}
    {Playwright, Selenium, Pytest, E2E Testing, Regression Testing, Exploratory Testing, HIL Testing, Root Cause Analysis}

  \cvskill
    {API / Backend / Integration}
    {API Testing, Backend Services, REST APIs, WebSockets, Django, Node.js, Integration Testing}

  \cvskill
    {CI/CD \& Observability}
    {GitHub Actions, Azure DevOps, Docker, Kubernetes, Grafana, Datadog, ReportPortal, Release Visibility}

  \cvskill
    {Test Management \& Collaboration}
    {TestRail, qTest, Confluence, Stakeholder Reporting, Documentation, Agile / Scrum}

  \cvskill
    {Languages}
    {Polish, English}

\end{cvskills}
```

- [ ] **Step 2: Reorder and rewrite the full-CV experience section**

Rewrite `examples/cv/experience.tex` so the roles appear in this order:

1. `Quality Assurance Team Lead`
2. `QA and Automation Specialist`
3. `QA Engineer / QA Lead - Consumer Entertainment Technology`
4. `Associate QA Engineer - Consumer Entertainment Technology`
5. `DevOps Engineer` at `Polestar`
6. `DevOps Engineer` at `Volvo Cars`
7. `Co-founder and CTO (Private, after-hours product)`
8. `IT Consultant`

Use these exact bullet blocks for the most important rewritten roles:

```tex
\cventry
  {Quality Assurance Team Lead}
  {Efectivo, Humanit Group}
  {Wrocław, Poland}
  {Feb 2025 - Present}
  {
    \begin{cvitems}
      \item {Line-managing a 5-person QA team and owning QA delivery, QA minima, release readiness, and quality metrics across product and ecosystem releases.}
      \item {Leading QA strategy and quality ownership across an ecosystem spanning approximately 6-8 product and platform layers, including API, customer-hosted servers, backend, frontend, mobile, E2E, and infrastructure workflows.}
      \item {Building and maintaining dozens of E2E and API scenarios to improve cross-system regression depth and release confidence.}
      \item {Reducing regression and release validation time by more than 1 day and cutting manual verification effort by 30%+ while supporting several releases per month.}
      \item {Driving backend testing, observability, CI/CD, and reporting improvements with Grafana, Datadog, ReportPortal, and internal tooling.}
      \item {Designing LLM-assisted workflows to automate testing tasks and improve internal product documentation and knowledge access.}
    \end{cvitems}
  }
```

```tex
\cventry
  {QA and Automation Specialist}
  {Efectivo, Humanit Group}
  {Wrocław, Poland}
  {May 2024 - Feb 2025}
  {
    \begin{cvitems}
      \item {Built end-to-end automation for product and ecosystem workflows from scratch across web, backend, and cross-system flows.}
      \item {Created verification scripts for Hardware-in-the-Loop testing and broader release validation workflows.}
      \item {Worked with frontend, backend, mobile, hardware, and infrastructure engineers to define automation scope, QA practices, and test coverage priorities.}
      \item {Contributed to the transition from manual-heavy validation toward repeatable E2E and API-driven release checks.}
    \end{cvitems}
  }
```

```tex
\cventry
  {QA Engineer / QA Lead - Consumer Entertainment Technology}
  {Dolby Laboratories}
  {Wrocław, Poland}
  {Jan 2021 - Dec 2021}
  {
    \begin{cvitems}
      \item {Led interoperability and ecosystem health testing across software and hardware workflows in a complex consumer entertainment environment.}
      \item {Owned test design, test planning, test architecture, quality metrics, and CI/CD-enabled QA process improvements.}
      \item {Built stakeholder-facing dashboards that consolidated qTest, Excel, and Confluence data into clearer release and risk reporting.}
      \item {Supported Dolby Atmos and Dolby Vision pilot programs with broadcasters and streaming services.}
    \end{cvitems}
  }
```

```tex
\cventry
  {Co-founder and CTO (Private, after-hours product)}
  {Lexense.ai}
  {Poland}
  {Jan 2025 - Present}
  {
    \begin{cvitems}
      \item {Built a private after-hours product from scratch, owning architecture, backend, infrastructure, and secure deployment for an AI-native legal platform.}
      \item {Designed the system around Node.js / NestJS, MongoDB, Redis, Qdrant, OCR, and self-hosted operations, strengthening backend and platform depth alongside commercial QA leadership work.}
    \end{cvitems}
  }
```

Keep the remaining roles concise and QA-supportive rather than platform-first.

- [ ] **Step 3: Verify the full-CV source now centers QA leadership**

Run:

```bash
rg -n "QA Leadership|Test Automation|Quality Assurance Team Lead|5-person|6-8|30%|after-hours" examples/cv/skills.tex examples/cv/experience.tex
```

Expected:
- matches appear in both files
- the first experience match in `examples/cv/experience.tex` is the QA Lead role
- `Lexense` is still present, but marked as private / after-hours

- [ ] **Step 4: Commit the full-CV content rewrite**

Run:

```bash
git add examples/cv/skills.tex examples/cv/experience.tex
git commit -m "feat(cv): rewrite full CV for QA lead positioning"
```

Expected:
- commit succeeds
- only the full CV skills and experience changes are included

### Task 3: Rewrite the QA Lead ATS Document

**Files:**
- Modify: `examples/cv-ats.tex`

- [ ] **Step 1: Replace the ATS header and summary with QA Lead positioning**

Update the top block in `examples/cv-ats.tex` so it reads:

```tex
{\large QA Lead | Test Strategy | Automation | API | CI/CD}\par
```

and replace the current professional summary paragraph with:

```tex
Hands-on QA Lead with commercial experience across API, customer-hosted servers, backend, frontend, mobile, end-to-end, and infrastructure workflows. Line-managed a 5-person QA team, owned QA strategy, QA minima, release readiness, and quality metrics across a 6-8-layer ecosystem, and built and maintained dozens of E2E and API scenarios. Reduced regression and release validation by more than 1 day, cut manual verification effort by 30%+, and supported several releases per month. Additional after-hours work at Lexense.ai strengthens backend, infrastructure, and architecture depth while keeping the primary profile focused on quality leadership.
```

- [ ] **Step 2: Replace the ATS skills section with QA Lead screening keywords**

Replace the `Core Skills` block with these lines:

```tex
\textbf{QA Leadership \& Strategy:} QA Lead, hands-on leadership, QA strategy, QA minima, release readiness, quality metrics, test planning, test architecture, stakeholder management\par
\textbf{Testing \& Automation:} Playwright, Selenium, Pytest, E2E testing, regression testing, exploratory testing, API testing, integration testing, backend testing, HIL testing\par
\textbf{CI/CD \& Observability:} GitHub Actions, Azure DevOps, Docker, Kubernetes, Grafana, Datadog, ReportPortal, release visibility, root cause analysis\par
\textbf{Test Management \& Collaboration:} TestRail, qTest, Confluence, documentation, Agile, Scrum, English, Polish\par
```

- [ ] **Step 3: Reorder and rewrite the ATS experience entries**

Rewrite the `Professional Experience` entries so they follow the same order as the full QA Lead CV, with the top ATS entry for Efectivo using this exact block:

```tex
\experienceentry
  {Quality Assurance Team Lead}
  {Efectivo, Humanit Group}
  {Wroclaw, Poland}
  {Feb 2025 - Present}
  {
    \item Line-managed a 5-person QA team and owned QA strategy, QA minima, release readiness, and quality metrics.
    \item Owned quality across a 6-8-layer ecosystem covering API, customer-hosted servers, backend, frontend, mobile, E2E, and infrastructure.
    \item Built and maintained dozens of E2E and API scenarios, reducing regression and release validation by more than 1 day.
    \item Reduced manual verification effort by 30%+ while supporting several releases per month.
    \item Improved backend testing, CI/CD, observability, and reporting with Grafana, Datadog, ReportPortal, and internal tooling.
  }
```

Use shorter keyword-rich blocks for the remaining roles, and keep `Lexense` present but clearly secondary and after-hours.

- [ ] **Step 4: Verify the ATS source contains the required QA Lead signals**

Run:

```bash
rg -n "QA Lead|QA strategy|release readiness|5-person|6-8-layer|Playwright|ReportPortal|after-hours" examples/cv-ats.tex
```

Expected:
- all major QA Lead screening terms are present
- the ATS title no longer includes `Senior Full Stack Engineer` or `AI-Native Developer`

- [ ] **Step 5: Commit the QA Lead ATS rewrite**

Run:

```bash
git add examples/cv-ats.tex
git commit -m "feat(cv): rewrite ATS CV for QA lead roles"
```

Expected:
- commit succeeds
- only `examples/cv-ats.tex` is included

### Task 4: Rewrite the Short Resume for QA Automation Specialist

**Files:**
- Modify: `examples/resume.tex`
- Modify: `examples/resume/summary.tex`
- Modify: `examples/resume/skills.tex`
- Modify: `examples/resume/experience.tex`

- [ ] **Step 1: Narrow the resume header to QA Automation**

Update the title in `examples/resume.tex` to:

```tex
\position{QA Automation Specialist{\enskip\cdotp\enskip}Playwright{\enskip\cdotp\enskip}API{\enskip\cdotp\enskip}CI/CD}
```

- [ ] **Step 2: Replace the resume summary with automation-first positioning**

Replace the content of `examples/resume/summary.tex` with:

```tex
\begin{cvparagraph}

QA Automation Specialist with commercial experience building end-to-end and API automation across backend, frontend, mobile, hardware-integrated, and infrastructure workflows. Built automation from scratch at Efectivo / Humanit Group, maintained dozens of E2E and API scenarios, reduced regression and release validation by more than 1 day, and cut manual verification effort by 30%+ while supporting several releases per month. Hands-on with Playwright, Selenium, Pytest, TypeScript, JavaScript, Python, CI/CD, Docker, Kubernetes, Grafana, and Datadog. Current QA Lead responsibilities add release readiness, quality metrics, and team leadership depth.
\end{cvparagraph}
```

- [ ] **Step 3: Replace the resume skills matrix with automation-first categories**

Rewrite `examples/resume/skills.tex` so the `cvskills` block becomes:

```tex
\begin{cvskills}

  \cvskill
    {Automation Frameworks}
    {Playwright, Selenium, Pytest, E2E Testing, Regression Testing, Exploratory Testing, HIL Testing}

  \cvskill
    {Programming \& API}
    {TypeScript, JavaScript, Python, API Testing, REST APIs, Backend Testing, WebSockets}

  \cvskill
    {CI/CD \& Platform}
    {GitHub Actions, Azure DevOps, Docker, Kubernetes, AWS, Azure}

  \cvskill
    {Observability \& Reliability}
    {Grafana, Datadog, ReportPortal, Release Visibility, Root Cause Analysis, Flakiness Reduction}

  \cvskill
    {Quality Leadership}
    {Test Strategy, QA Minima, Release Readiness, Quality Metrics, Cross-Functional Collaboration}

  \cvskill
    {Languages}
    {Polish, English}

\end{cvskills}
```

- [ ] **Step 4: Rework resume experience for automation-heavy screening**

Rewrite the top blocks in `examples/resume/experience.tex` so the first two roles become:

```tex
\cventry
  {Quality Assurance Team Lead}
  {Efectivo, Humanit Group}
  {Wrocław, Poland}
  {Feb. 2025 - Present}
  {
    \begin{cvitems}
      \item {Led a 5-person QA team while remaining hands-on with E2E, API, backend, and release-quality automation across a 6-8-layer ecosystem.}
      \item {Maintained and expanded dozens of E2E and API scenarios, reducing regression and release validation by more than 1 day and cutting manual verification effort by 30%+.}
      \item {Improved CI/CD, observability, backend testing, and internal tooling to support several releases per month.}
    \end{cvitems}
  }
```

```tex
\cventry
  {QA and Automation Specialist}
  {Efectivo, Humanit Group}
  {Wrocław, Poland}
  {May 2024 - Feb 2025}
  {
    \begin{cvitems}
      \item {Built end-to-end automation from scratch for product and ecosystem workflows across web, backend, and cross-system paths.}
      \item {Created verification scripts for Hardware-in-the-Loop testing and broader release validation.}
      \item {Worked with frontend, backend, mobile, hardware, and infrastructure engineers to define automation priorities and test coverage.}
    \end{cvitems}
  }
```

Keep the rest of the roles concise, and rewrite `Lexense` as a short private after-hours engineering entry rather than a headline role.

- [ ] **Step 5: Verify the resume source now reads as QA Automation**

Run:

```bash
rg -n "QA Automation Specialist|Playwright|dozens|30%|after-hours|Automation Frameworks" examples/resume.tex examples/resume/summary.tex examples/resume/skills.tex examples/resume/experience.tex
```

Expected:
- the resume header is automation-first
- the summary and skills show Playwright/API/CI/CD clearly
- `Lexense` remains present but secondary

- [ ] **Step 6: Commit the automation resume rewrite**

Run:

```bash
git add examples/resume.tex examples/resume/summary.tex examples/resume/skills.tex examples/resume/experience.tex
git commit -m "feat(cv): retarget resume for QA automation roles"
```

Expected:
- commit succeeds
- only the resume automation files are included

### Task 5: Add a Dedicated QA Automation ATS Variant

**Files:**
- Create: `examples/cv-ats-qa-automation.tex`
- Modify: `Makefile`

- [ ] **Step 1: Create the automation ATS document**

Create `examples/cv-ats-qa-automation.tex` by copying the ATS structure from `examples/cv-ats.tex` and replacing the header, summary, skills, and top experience blocks with this content:

```tex
{\LARGE\bfseries Wojciech Bajer}\par
{\large QA Automation Specialist | Playwright | API | CI/CD}\par

\cvsection{Professional Summary}
QA Automation Specialist with commercial experience building end-to-end and API automation across backend, frontend, mobile, hardware-integrated, and infrastructure workflows. Built automation from scratch at Efectivo / Humanit Group, maintained dozens of E2E and API scenarios, reduced regression and release validation by more than 1 day, and cut manual verification effort by 30%+ while supporting several releases per month. Hands-on with Playwright, Selenium, Pytest, TypeScript, JavaScript, Python, CI/CD, Docker, Kubernetes, Grafana, and Datadog.

\cvsection{Core Skills}
\textbf{Automation Frameworks:} Playwright, Selenium, Pytest, E2E testing, regression testing, exploratory testing, HIL testing\par
\textbf{Programming \& API:} TypeScript, JavaScript, Python, API testing, REST APIs, backend testing, WebSockets\par
\textbf{CI/CD \& Platform:} GitHub Actions, Azure DevOps, Docker, Kubernetes, AWS, Azure\par
\textbf{Observability \& Reliability:} Grafana, Datadog, ReportPortal, release visibility, root cause analysis, flakiness reduction\par
\textbf{Quality Leadership:} test strategy, QA minima, release readiness, quality metrics, cross-functional collaboration\par
```

Use the same shortened automation-focused experience ordering as the resume, while still keeping the QA Lead role visible first because it is the current role.

- [ ] **Step 2: Add a build target for the new ATS PDF**

Update `Makefile` so these lines exist:

```make
examples: $(foreach x, coverletter coverletter-qa-lead coverletter-qa-automation coverletter-devops-platform cv resume cv-ats cv-ats-qa-automation, $x.pdf)
```

and

```make
cv-ats-qa-automation.pdf: $(EXAMPLES_DIR)/cv-ats-qa-automation.tex
	$(CC) -output-directory=$(EXAMPLES_DIR) $<
```

- [ ] **Step 3: Verify the new ATS artifact is wired into the build**

Run:

```bash
rg -n "cv-ats-qa-automation" Makefile examples/cv-ats-qa-automation.tex
```

Expected:
- both the new file and the Make target are present
- the new ATS title is `QA Automation Specialist | Playwright | API | CI/CD`

- [ ] **Step 4: Commit the new automation ATS variant**

Run:

```bash
git add examples/cv-ats-qa-automation.tex Makefile
git commit -m "feat(cv): add ATS variant for QA automation roles"
```

Expected:
- commit succeeds
- only the new automation ATS file and Makefile changes are included

### Task 6: Rebuild and Verify All Targeted CV Variants

**Files:**
- Modify: `examples/cv.pdf`
- Modify: `examples/cv-ats.pdf`
- Modify: `examples/resume.pdf`
- Modify: `examples/cv-ats-qa-automation.pdf`

- [ ] **Step 1: Rebuild all four targeted PDFs**

Run:

```bash
make cv.pdf cv-ats.pdf resume.pdf cv-ats-qa-automation.pdf
```

Expected:
- exit code `0`
- regenerated PDFs appear in `examples/`

- [ ] **Step 2: Verify PDF text for the QA Lead full CV**

Run:

```bash
pdftotext examples/cv.pdf - | rg "QA Lead|5-person|5 person|30%|after-hours|release readiness|quality metrics"
```

Expected:
- command exits with code `0`
- extracted text shows the QA Lead summary and metrics

- [ ] **Step 3: Verify PDF text for the QA Lead ATS**

Run:

```bash
pdftotext examples/cv-ats.pdf - | rg "QA Lead|QA strategy|release readiness|Playwright|API testing|ReportPortal|5-person|5 person"
```

Expected:
- command exits with code `0`
- extracted text shows the ATS keyword set for QA Lead screening

- [ ] **Step 4: Verify PDF text for the automation resume and automation ATS**

Run:

```bash
pdftotext examples/resume.pdf - | rg "QA Automation Specialist|Playwright|dozens|30%|CI/CD"
pdftotext examples/cv-ats-qa-automation.pdf - | rg "QA Automation Specialist|Playwright|API|Pytest|CI/CD|30%"
```

Expected:
- both commands exit with code `0`
- both files read as automation-first documents rather than generalist profiles

- [ ] **Step 5: Verify page counts stay reasonable**

Run:

```bash
pdfinfo examples/cv.pdf | rg '^Pages:'
pdfinfo examples/cv-ats.pdf | rg '^Pages:'
pdfinfo examples/resume.pdf | rg '^Pages:'
pdfinfo examples/cv-ats-qa-automation.pdf | rg '^Pages:'
```

Expected:
- all commands exit with code `0`
- `examples/cv-ats.pdf`, `examples/resume.pdf`, and `examples/cv-ats-qa-automation.pdf` stay at `2` pages
- `examples/cv.pdf` does not grow unexpectedly beyond the current `2`-page layout

- [ ] **Step 6: Review source diff and final repository scope**

Run:

```bash
git diff -- examples/cv.tex examples/cv/summary.tex examples/cv/skills.tex examples/cv/experience.tex examples/cv-ats.tex examples/resume.tex examples/resume/summary.tex examples/resume/skills.tex examples/resume/experience.tex examples/cv-ats-qa-automation.tex Makefile
git status --short
```

Expected:
- tracked source changes are limited to the intended CV / ATS files plus `Makefile`
- rebuilt PDFs are the only generated artifacts changed under `examples/`
