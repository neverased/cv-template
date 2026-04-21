# QA Lead CV Repositioning Design

## Goal

Reposition this CV package so it works primarily for `QA Lead` roles and secondarily for `QA Automation Specialist` roles.

The current materials are too broad and signal:

- QA
- senior full-stack engineering
- AI-native product work
- founder / CTO work

That breadth weakens recruiter match quality and ATS alignment for quality-focused roles.

The redesign should create a focused pack where:

- the main profile is `QA Lead`
- the supporting profile is `QA Automation Specialist`
- `Lexense` remains visible, but only as supporting engineering depth
- commercial QA experience remains the dominant narrative

## Why The Current CV Underperforms

### 1. Headline and summary are too broad

The current headline and summary present Wojciech as:

- `QA Lead`
- `Senior Full Stack Engineer`
- `AI-Native Developer`

This makes the profile read like a technical generalist rather than a quality leader or senior automation engineer.

### 2. Experience order weakens the main story

`Lexense` and consulting work appear before the current QA Lead role, which makes the profile look like a founder/consultant who also does QA rather than a QA leader with additional technical depth.

### 3. Skills are not QA-centric enough

The current skills sections give too much visual weight to:

- front-end
- general programming
- AI tooling
- broad DevOps stacks

For QA roles, those areas should support the profile rather than define it.

### 4. Too few measurable outcomes

The strongest QA roles in the market repeatedly ask for:

- hands-on leadership
- test strategy ownership
- automation ownership
- API/backend coverage
- CI/CD integration
- measurable quality outcomes

The current bullets describe responsibilities well, but not enough quantified impact.

## Market Research Summary

Research was conducted on `2026-04-21` using recent Poland and remote-Europe QA Lead / QA Automation postings.

### Repeated QA Lead signals

- hands-on QA leadership, not manager-only leadership
- QA strategy, quality gates, release readiness, quality metrics
- API, integration, E2E, regression, UAT, and cross-team coordination
- Jira / Confluence / TestRail / Xray / Qase / similar test-management tooling
- CI/CD and stakeholder communication as baseline requirements

### Repeated QA Automation signals

- strong `Playwright` signal across current openings
- engineering-heavy automation profiles, not test execution only
- API and backend coverage as baseline
- framework ownership, including building automation from scratch
- CI/CD, flakiness reduction, root-cause analysis, and cloud/platform literacy

### Research implication

One hybrid CV is not enough. The package should split into:

1. `QA Lead` as the main profile
2. `QA Automation Specialist` as a supporting profile

## Approved Positioning

The approved positioning is:

- keep `Lexense`
- keep the engineering depth
- do not hide the fact that the commercial core is QA with some DevOps
- make `QA Lead` the default story
- make `QA Automation Specialist` a separate role-specific variant

`Lexense` should be framed as:

- a private / after-hours product
- built from scratch
- evidence of infrastructure, coding, and architecture depth
- supporting credibility for systems-level QA leadership

It must not outrank commercial QA experience.

## Artifact Strategy

### 1. Main full CV

Use `examples/cv.tex` as the main `QA Lead` CV.

This document should become the primary recruiter / hiring-manager version.

### 2. Main ATS CV

Use `examples/cv-ats.tex` as the main `QA Lead` ATS version.

This document should be keyword-richer, more direct, and more screening-oriented than the full CV.

### 3. Supporting automation resume

Use `examples/resume.tex` as the `QA Automation Specialist` version.

This remains the shorter, role-specific alternative for automation-heavy applications.

### 4. New automation ATS file

Add a separate ATS-oriented automation variant instead of trying to make one ATS fit both role families.

Create:

- `examples/cv-ats-qa-automation.tex`

This should mirror the `resume.tex` positioning, but in ATS-first form.

## Narrative Architecture

### Main narrative

The dominant story should be:

`Hands-on QA Lead with strong automation, API/backend, CI/CD, and quality-systems depth.`

### Supporting narrative

The secondary story should be:

`Senior QA Automation engineer who builds frameworks, owns cross-system quality, and understands delivery platforms deeply.`

### Explicitly not the main narrative

The package should no longer primarily read as:

- full-stack engineer
- AI-native developer
- founder / CTO
- DevOps engineer

Those areas remain supporting signals only.

## Header And Summary Design

### QA Lead header

The top-line title in `examples/cv.tex` and `examples/cv-ats.tex` should be narrowed to QA leadership.

Target direction:

- `QA Lead | Test Strategy | Automation | API | CI/CD`

or equivalent wording with the same meaning.

`Senior Full Stack Engineer` and `AI-Native Developer` should be removed from the main title.

### QA Automation header

The title in `examples/resume.tex` and the new automation ATS file should be narrowed to automation engineering.

Target direction:

- `QA Automation Specialist | Playwright | API | CI/CD`

or

- `Senior QA Automation Engineer | Playwright | TypeScript | API`

### QA Lead summary

The new main summary should explicitly cover:

- line management of a `5`-person QA team
- QA strategy, QA minima, release readiness, and quality metrics ownership
- quality ownership across an ecosystem of approximately `6-8` layers / components
- scope across `API`, local customer-hosted servers, backend, frontend, mobile, E2E, and infrastructure
- `dozens` of `E2E/API` scenarios
- regression / release validation reduced by `more than 1 day`
- manual work reduced by `30%+`
- support for `several releases per month`

### QA Automation summary

The automation summary should focus on:

- building automation from scratch
- framework ownership
- Playwright / Python / TypeScript / API / CI/CD
- backend and cross-system testing
- reduced regression time and manual work

## Section Ordering

### Full CV

The full CV should no longer open with education.

Preferred order:

1. Header
2. Summary / impact section
3. Skills
4. Experience
5. Education
6. Certifications
7. Optional remaining sections if still useful

This likely requires adding a new file:

- `examples/cv/summary.tex`

and reordering inputs in:

- `examples/cv.tex`

### ATS versions

The ATS versions should keep the simplest possible order:

1. Header
2. Professional summary
3. Core skills
4. Professional experience
5. Education
6. Certifications

## Skills Design

### QA Lead skills

The full CV and QA Lead ATS should use QA-centric groupings.

Preferred categories:

- `QA Leadership & Strategy`
- `Test Automation & QA Engineering`
- `API / Backend / Integration Testing`
- `CI/CD / Observability / Test Infrastructure`
- `Test Management & Collaboration`
- `Languages`

### Prioritize

- QA strategy
- test planning
- test architecture
- QA minima / quality gates
- release readiness
- quality metrics
- Playwright / Selenium / Pytest
- API testing
- backend services
- CI/CD
- Grafana / Datadog / ReportPortal
- Jira / Confluence / TestRail / equivalent if used

### De-emphasize

- front-end stacks
- general product engineering stacks
- AI tools as a standalone identity category

If AI appears at all, it should sit inside a supporting bullet or skill phrase, not as a primary skills column.

## QA Automation skills

The automation resume and automation ATS should prioritize:

- Playwright
- Selenium
- Pytest
- TypeScript / JavaScript / Python
- API testing
- backend testing
- CI/CD
- GitHub Actions / Azure DevOps
- Docker / Kubernetes
- observability and flakiness reduction

This version should still keep QA leadership evidence visible, but not lead with it.

## Experience Design

### New experience order for QA Lead materials

The main CV and QA Lead ATS should reorder experience as follows:

1. `Quality Assurance Team Lead` at `Efectivo, Humanit Group`
2. `QA and Automation Specialist` at `Efectivo, Humanit Group`
3. `QA Engineer / QA Lead - Consumer Entertainment Technology` at `Dolby Laboratories`
4. `Associate QA Engineer - Consumer Entertainment Technology` at `Dolby Laboratories`
5. `DevOps Engineer` roles at `Polestar` and `Volvo Cars`
6. `Lexense.ai`
7. `Consulting Wojciech Bajer`

### Efectivo QA Lead bullet design

This role becomes the anchor of the entire package.

The rewritten bullets should include:

- line-managed a `5`-person QA team
- owned QA delivery, QA minima, test scenarios, release readiness, and quality metrics
- owned quality across an ecosystem of approximately `6-8` product / platform layers
- expanded and maintained `dozens` of `E2E/API` scenarios
- reduced regression / release validation time by `more than 1 day`
- reduced manual verification effort by `30%+`
- supported `several releases per month`
- drove observability, backend testing, CI/CD, and reporting improvements

The language should be outcome-first, not responsibility-first.

### Efectivo QA Automation Specialist bullet design

This role should explain the transition into QA leadership.

The rewritten bullets should emphasize:

- built end-to-end automation from scratch
- API and backend testing
- Playwright / Python / TypeScript-oriented automation where supported by existing materials
- HIL verification
- collaboration with frontend, backend, mobile, hardware, and infrastructure teams
- progression from implementation to strategy ownership

### Dolby bullet design

The Dolby roles should be reframed as early evidence of:

- quality systems thinking
- software + hardware integration testing
- test architecture and metrics ownership
- CI/CD-enabled QA process improvement
- stakeholder-facing reporting and dashboards

These roles should show that QA leadership and structured quality work predate the current lead title.

### DevOps roles

The DevOps roles stay, but only as supporting experience for:

- CI/CD depth
- release visibility
- observability
- environment portability
- platform understanding that strengthens QA leadership

They should not pull the CV back toward a platform-engineer identity.

### Lexense framing

`Lexense.ai` remains in the package, but is compressed and clearly framed as a side project.

The role should be labeled or described so it is unmistakably:

- private / after-hours work
- built from scratch
- evidence of architecture, infrastructure, and coding depth
- not the main commercial identity

The bullets should stay short and support the case that Wojciech can reason deeply about product systems, backend services, and infrastructure.

### Consulting role

The consulting role should be either:

- highly compressed

or

- moved near the end of the experience section

It should no longer compete with the QA story.

## ATS Design Rules

### QA Lead ATS

The QA Lead ATS should emphasize direct keywords and short sentences around:

- `QA Lead`
- `hands-on leadership`
- `QA strategy`
- `quality gates`
- `release readiness`
- `quality metrics`
- `API testing`
- `manual and automated testing`
- `E2E`
- `regression`
- `integration`
- `CI/CD`
- `Playwright`
- `Selenium`
- `Pytest`
- `Jira`
- `Confluence`
- `ReportPortal`
- `English`

### QA Automation ATS

The automation ATS should emphasize:

- `QA Automation Specialist`
- `Playwright`
- `TypeScript`
- `Python`
- `API testing`
- `backend services`
- `REST`
- `CI/CD pipelines`
- `GitHub Actions`
- `Azure DevOps`
- `Docker`
- `Kubernetes`
- `framework ownership`
- `automation from scratch`
- `flakiness reduction`
- `regression time reduction`

### ATS writing rules

For both ATS files:

- keep short, explicit sentences
- avoid over-compressed founder language
- avoid visually prominent non-QA categories
- mirror market language where truthful
- keep metrics approximate but honest when exact counts are unavailable

## Content Constraints

### Keep

- `Lexense`
- technical depth
- DevOps / CI/CD credibility
- AI-related testing/tooling only where it supports quality work

### Remove or de-emphasize

- full-stack as a primary identity
- AI-native as a primary identity
- front-end as a top-level competency
- broad founder positioning at the top of the CV

## Acceptance Criteria

- The main full CV clearly reads as a `QA Lead` profile.
- The main ATS CV clearly reads as a `QA Lead` profile.
- The shorter supporting version clearly reads as `QA Automation Specialist`.
- A separate automation ATS variant exists.
- `Lexense` remains visible, but is clearly secondary to commercial QA work.
- Efectivo QA Lead bullets include the approved metrics:
  - `5` people
  - `6-8` ecosystem layers / components
  - `dozens` of `E2E/API` scenarios
  - `more than 1 day` faster regression / release validation
  - `30%+` less manual work
  - `several releases per month`
- Skills sections become QA-centric across all targeted variants.
- The package no longer reads like a generalist founder/full-stack profile.

## Out Of Scope

- Rewriting cover letters in this phase
- Building a platform-engineer or AI-engineer primary CV
- Inventing unsupported metrics
- Removing `Lexense` completely
- Rewriting unrelated repository tooling unless needed to produce the new document variants
