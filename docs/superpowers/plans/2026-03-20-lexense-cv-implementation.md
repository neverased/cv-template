# Lexense CV Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reposition the `Lexense.ai` experience entry across CV variants as `CTO / platform architect` and `AI-native platform builder`, while aligning the resume date mismatch.

**Architecture:** Update only the `Lexense` experience copy in the long CV, short resume, and ATS version. Use variant-specific compression: the long CV gets 3 architecture-led bullets, the resume gets 2 concise executive bullets, and the ATS version gets 3 keyword-rich bullets optimized for discoverability.

**Tech Stack:** LaTeX, Awesome CV templates, LuaLaTeX, PDF text extraction (`pdftotext`)

---

### Task 1: Update Lexense Entry Sources

**Files:**
- Modify: `examples/cv/experience.tex`
- Modify: `examples/resume/experience.tex`
- Modify: `examples/cv-ats.tex`

- [ ] **Step 1: Replace the long CV Lexense bullets**

Update `examples/cv/experience.tex` so the `Lexense.ai` entry uses 3 bullets:

1. AI-native legal platform architecture across products and services.
2. Core platform and AI design across backend, RAG/knowledge, OCR, chat, and voice workflows.
3. Self-hosted infrastructure, observability, CI/CD, and security-by-default for sensitive legal data.

- [ ] **Step 2: Replace the short resume Lexense bullets and fix the date**

Update `examples/resume/experience.tex` so the `Lexense.ai` entry:

- uses `Jan 2025 - Present`
- uses 2 concise bullets focused on platform architecture and AI-native/self-hosted platform design

- [ ] **Step 3: Replace the ATS Lexense bullets**

Update `examples/cv-ats.tex` so the `Lexense` entry uses 3 ATS-oriented bullets with the strongest relevant keywords:

- platform architecture
- Node.js / NestJS
- MongoDB / Redis / Qdrant
- OpenAI / RAG / OCR
- streaming / voice
- observability / CI/CD / security

### Task 2: Render Updated Documents

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
- command exits with code `0`
- updated PDFs are written to `examples/`

### Task 3: Verify Extracted ATS-Friendly Content

**Files:**
- Test: `examples/cv.pdf`
- Test: `examples/resume.pdf`
- Test: `examples/cv-ats.pdf`

- [ ] **Step 1: Verify expected Lexense phrases in the PDFs**

Run:

```bash
pdftotext examples/cv.pdf - | rg "AI-native|Node.js|RAG|OCR|security|observability"
pdftotext examples/resume.pdf - | rg "AI-native|Node.js|self-hosted|Jan 2025"
pdftotext examples/cv-ats.pdf - | rg "platform architecture|Node.js|NestJS|MongoDB|Redis|Qdrant|OpenAI|RAG|OCR|security|CI/CD"
```

Expected:
- each command exits with code `0`
- the extracted text reflects the new Lexense positioning

- [ ] **Step 2: Review git diff**

Run:

```bash
git diff -- examples/cv/experience.tex examples/resume/experience.tex examples/cv-ats.tex
```

Expected:
- diff only shows the intended `Lexense` copy and date updates
