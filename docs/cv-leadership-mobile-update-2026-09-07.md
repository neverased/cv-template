# CV: zarządzanie liniowe i aplikacja Flutter

Po potwierdzeniu przez autora odpowiedzialności za ludzi oraz zbudowania całej aplikacji mobilnej Lexense od podstaw uzupełniono oba profile CV i ich warianty ATS.

## Wprowadzone informacje

- QA Lead / Test Manager: summary i Core Skills wprost wskazują line management, mentoring i rozwój zespołu.
- Pierwszy punkt Efectivo dotyczy zarządzania liniowego pięcioosobowym zespołem. Osobny punkt opisuje strategię, planowanie testów, standardy i gotowość do wydania. Raportowanie łączy narzędzia z komunikowaniem metryk jakości oraz ryzyka interesariuszom.
- W głównym CV przywrócono w Dolby test planning, test architecture oraz dashboardy dla interesariuszy, oparte na qTest, Excel i Confluence. Podstawą jest wcześniejsze CV, a nie nowa deklaracja o zarządzaniu liniowym w Dolby.
- Lexense: dodano stworzenie kompletnej aplikacji mobilnej od podstaw we Flutterze i Darcie dla iOS i Androida, wraz z odpowiedzialnością za architekturę, interfejs i integrację z backendem.
- Core Skills ma osobny wiersz Mobile Development: Flutter, Dart, iOS / Android apps, API integration. W głównym CV mobilny zakres jest też widoczny w summary.
- Warianty automatyzacji zawierają te same potwierdzone fakty o mentoringu i aplikacji mobilnej, zachowując pierwszeństwo automatyzacji testów w opisie doświadczenia.
- Wspólne deklaracje są w makrach `peopleLeadership` i `mobileAppDelivery` w `examples/shared/profile.tex`.

Autorstwo całej aplikacji oraz mentoring i rozwój wynikają z potwierdzenia autora w rozmowie. Flutter, Dart, platformy i zakres architektury aplikacji zweryfikowano w `ai-lawyer-mobile/AGENTS.md`, `README.md` i `pubspec.yaml` w lokalnym workspace Lexense. Nie dodano twierdzeń o publikacji w sklepach, liczbie użytkowników, rekrutacji, ocenach okresowych ani częstotliwości spotkań 1:1.

## Weryfikacja

- `make application-pdfs CC='/Library/TeX/texbin/lualatex -interaction=nonstopmode -halt-on-error'`: kod 0, wszystkie cztery PDF-y po dwie strony, bez ostrzeżeń, overfull/underfull boxes i brakujących znaków.
- Obejrzano osiem stron finalnych PDF-ów. Zachowano nominalny font 11 pt, dotychczasowe marginesy i zdjęcie w głównym CV.
- Poppler, pypdf i pdfplumber zwracają identyczny tekst po normalizacji białych znaków dla każdego pliku. Sprawdzono komplet nowych fraz, wcześniejsze daty, treść AI, granice stron oraz zgodność bajtową kopii w `output/pdf/`.
- Główne CV: 733 wyrazy (353 + 380), wcześniej 680. QA Lead ATS: 653. Oba warianty automatyzacji: 614 i identyczna treść.
- Log i SHA-256: `output/cv-leadership-mobile-build/build.log` oraz `verification.json` w tym samym katalogu.
- To korekta treści i eksportów; kod generatora listów nie został zmieniony. Nie powtarzano jego wcześniej zaliczonych testów jednostkowych. Nie testowano komercyjnego ATS.

Nadal nie rozstrzygnięto rozbieżnych metryk wyników Efectivo, poziomu CEFR języka angielskiego ani zakresu zarządzania liniowego w Dolby. Ta weryfikacja poprzedzała przygotowanie lokalnych commitów; nie wykonano pushowania.
