# Lexense CV Positioning Design

## Goal

Update the `Lexense.ai` experience entry across CV variants so it positions the work as `CTO / platform architect` and `AI-native platform builder`, rather than as a generic startup description.

## Context

The current `Lexense` entry is too general. It states that the company is focused on legal document analysis and question answering, but it does not communicate:

- platform architecture ownership
- AI-native product design
- multi-product scope
- security and infrastructure design
- the main technical stack behind the system

As a result, the entry underrepresents the architectural and founding-CTO scope of the work.

## Positioning Direction

The preferred narrative is:

- `CTO / platform architect`
- `AI-native platform builder`

This should communicate that the candidate designed the platform end-to-end and made the key architectural decisions across product, platform, AI, and infrastructure layers.

## Messaging Principles

### 1. Lead with architecture ownership

The first bullet should establish end-to-end architecture ownership of an AI-native legal platform, not just product participation.

### 2. Show the platform is multi-product

The text should make clear that `Lexense` is not a single app. It spans:

- mobile app
- web workspace
- browser extension
- core backend
- knowledge / RAG service
- operational and documentation surfaces

The exact wording can be compressed, but the "platform" framing must be explicit.

### 3. Show AI-native depth without turning the entry into a stack dump

The entry should mention the core AI capabilities:

- OCR
- document analysis
- legal search / RAG
- streaming chat
- voice workflows

Technology names should be included selectively where they strengthen the positioning, especially in shorter / ATS-oriented variants.

### 4. Include platform and security credibility

The entry should show that the platform was designed with:

- self-hosted infrastructure
- observability
- CI/CD
- security-by-default
- encrypted handling of sensitive data

This is especially important because the domain is legal and deals with sensitive content.

### 5. Keep the entry readable

Do not paste the full stack into every variant.

- Full CV: 3 bullets
- Resume: 2 concise bullets
- ATS: 3 keyword-rich bullets

## Variant-Specific Design

### Full CV

Use 3 bullets:

1. AI-native legal platform architecture ownership across products and services.
2. Core platform and AI design covering backend, RAG/knowledge service, OCR, chat, and voice workflows.
3. Self-hosted infrastructure, observability, CI/CD, and security-by-default handling of sensitive legal data.

### Resume

Use 2 shorter bullets:

1. Architected an AI-native legal platform across mobile, web, extension, backend, and knowledge services.
2. Designed the platform around Node.js, AI/RAG workflows, and secure self-hosted infrastructure.

This version should sound more executive and compressed than the full CV.

### ATS

Use 3 bullets with explicit searchable keywords:

- `platform architecture`
- `Node.js`
- `NestJS`
- `MongoDB`
- `Redis`
- `Qdrant`
- `OpenAI`
- `RAG`
- `OCR`
- `streaming`
- `voice`
- `security`
- `observability`
- `CI/CD`

The ATS version should prioritize discoverability while remaining readable in plain text extraction.

## Additional Consistency Fix

The `Lexense` start date should be aligned everywhere to `Jan 2025 - Present`.
There is still a mismatch in the shorter resume variant where the date shows `Jan. 2026 - Present`.

## Out of Scope

- Expanding the `Lexense` entry into a full project case study
- Adding every infrastructure component and third-party integration
- Rewriting unrelated experience entries
- Restructuring the overall CV layout

## Acceptance Criteria

- `Lexense` is clearly positioned as platform architecture and AI-native product leadership.
- The entry no longer reads as a generic startup summary.
- Full CV, resume, and ATS use the same narrative with different compression levels.
- ATS includes the most important architecture and AI keywords.
- The `Jan 2025` start date is consistent across all variants.
