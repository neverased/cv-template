# Główne CV: AI, agenci, RAG i weryfikacja

Na życzenie autora rozbudowano główne CV QA Lead / Test Manager (`examples/cv.tex` i `examples/cv.pdf`) o doświadczenie AI z Lexense oraz przywrócono istniejące zdjęcie `examples/profile-wb.png`. Eksport do aplikowania: `output/pdf/Wojciech_Bajer_QA_Lead_CV.pdf`.

## Treść

- Nagłówek łączy QA Lead / Test Manager z automatyzacją i jakością AI.
- Summary przedstawia Lexense, agentów LLM, RAG i weryfikację źródeł.
- Kompetencje obejmują osobne grupy AI & Agents oraz RAG & AI Verification.
- Lexense otwiera drugą stronę jako AI Engineering & Verification: architektura platformy, narzędzia agentów, OpenAI APIs, kontekst i prompty, OCR, chunking, embeddings, Qdrant, wyszukiwanie hybrydowe, reranking, walidacja cytowań i dokładnych cytatów, brakujące dowody, ewaluacja oraz utrzymanie usług.
- Wymieniono istniejące miary i mechanizmy ewaluacji: Recall@k, MRR, nDCG, pokrycie dowodów, niepoparte cytowania oraz kryteria kosztu i opóźnienia. Nie dopisano niezmierzonych wyników ani gwarancji jakości odpowiedzi.
- Starsze stanowiska i edukację skompresowano, zachowując oddzielne okresy Dolby i kontrakty Volvo Cars / Polestar. Całość nadal ma dwie strony.

Opisy sprawdzono w aktualnym lokalnym kodzie Lexense, a nie wyłącznie w planach projektu. Przykładowe źródła w `/Users/neverased/Codebase/Lexense/ai-lawyer-backend/`:

- `ai-lawyer-backend/src/chat/chat.service.ts` i `ai-lawyer-backend/src/realtime-voice/realtime-voice.service.ts`: orkiestracja wywołań narzędzi i kontekst agenta głosowego.
- `knowledge-service/src/modules/rag/rag-hybrid-search.service.ts`, `rag-reranker.service.ts` i `knowledge-service/README.md`: retrieval, embeddings, przetwarzanie dokumentów i Qdrant.
- `ai-lawyer-backend/src/chat/services/chat-citation-guard.service.ts`: kontrola źródła, adresu, tytułu, niepopartych odniesień i dokładnych cytatów.
- `knowledge-service/src/modules/rag/legal-rag-eval.service.ts`: miary retrieval, pokrycia dowodów i cytowań.
- `ai-lawyer-backend/src/chat/evaluation/legal-answer-cascade-gate.ts`: kryteria ewaluacji odpowiedzi, kosztu i opóźnienia.

To kontrola zgodności opisu CV z implementacją; nie nowy audyt skuteczności produktu ani potwierdzenie wdrożenia wszystkich mechanizmów na produkcji.

## Weryfikacja eksportu

- Kompilacja: `make cv.pdf CC='/Library/TeX/texbin/lualatex -interaction=nonstopmode -halt-on-error'`, kod 0; brak ostrzeżeń, overfull/underfull boxes i brakujących znaków.
- Obejrzano obie strony finalnego PDF-u. Zdjęcie występuje wyłącznie na pierwszej stronie; brak obciętej lub nakładającej się treści.
- Poppler, pypdf i pdfplumber zwracają identyczny tekst po normalizacji białych znaków. 680 wyrazów, po 339 i 341 na stronę.
- Sprawdzono słowa i frazy AI, daty, dane kontaktowe, działające schematy linków i położenie tekstu w granicach stron.
- Pozostałe trzy PDF-y zachowano bez zmian, co potwierdzono porównaniem SHA-256 z poprzednią weryfikacją. Wcześniejszy skrypt sprawdzający identyczną treść pary CV/ATS nie dotyczy już rozszerzonego głównego CV.
- Wynik odczytu i SHA-256: `output/cv-ai-build/verification.json`; log: `output/cv-ai-build/build.log`.

Rozbieżne metryki Efectivo, poziom języka angielskiego i szczegóły formalnego zarządzania zespołem nadal wymagają potwierdzenia autora. Nie dodano ich w tej zmianie. Ta weryfikacja poprzedzała przygotowanie lokalnych commitów; nie wykonano pushowania.
