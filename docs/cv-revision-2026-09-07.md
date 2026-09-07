# Poprawki CV po audycie, 7 września 2026

Ten zapis opisuje pierwszy etap poprawek. Późniejsza [rozbudowa głównego CV o AI i przywrócenie zdjęcia](cv-ai-update-2026-09-07.md) zmieniła treść głównego CV; zgodność jego treści z wariantem ATS oraz liczba 600 wyrazów poniżej dotyczą wcześniejszego eksportu.

Wdrożono korektę dwóch profili: QA Lead / Test Manager oraz Senior QA Automation Engineer. Każdy ma wersję z dyskretnym akcentem kolorystycznym oraz wariant monochromatyczny ATS. Oba warianty danego profilu mają identyczną treść i układ jednej kolumny.

## Co zmieniono

- Wszystkie cztery PDF-y mają dwie strony; przebudowano także pliki w `examples/`, żeby źródła i eksporty były zgodne.
- Zastosowano tekstowy układ oparty na istniejącym podejściu wersji ATS (`article`), bez tabel do rozmieszczania treści, zdjęcia, ikon, cytatu, adresu mieszkania i daty wydruku. Klasa Awesome CV używana przez listy motywacyjne pozostała bez zmian.
- Ujednolicono imię i nazwisko, zwiększono tekst główny do nominalnych 11 pt i kontakt do 10 pt; dodano metadane autora i tytułu.
- Skrócono summary i opisy doświadczenia, dodano języki programowania w głównym profilu oraz opis już deklarowanej pracy z LLM w obu profilach.
- Zachowano osobne stanowiska i okresy pracy w Dolby oraz osobno datowane kontrakty Volvo Cars i Polestar przez HiQ. Wyróżniono Lexense jako projekt dodatkowy, także w wariancie automatyzacji.
- Skrócono edukację, pozostawiono ISTQB CTFL i szkolenie Scrum Master. Pominięto kurs wymowy, SEP i CLAD, których znaczenie lub aktualny status nie były potwierdzone dla docelowych ról. Materiały dawnych prezentacji i aktywności nie są włączane do CV.
- Strona główna autora, skupiona na szerszych usługach consultingowych, nie jest już linkowana z CV. Zachowano LinkedIn, GitHub i e-mail.
- Wspólne tytuły, daty, nazwa autora, języki i opis wpływu na regresję znajdują się w `examples/shared/profile.tex`. Starsze doświadczenie, edukacja i certyfikaty także są współdzielone. Cztery główne pliki nie przechowują już osobnych kopii tych samych faktów.
- Nagłówek i otwarcie generatora listów dostosowano do QA Lead; adres WWW generatora ma pełny schemat HTTPS, a cytat usunięto z jego profilu. Nie przebudowywano istniejących listów do konkretnych firm.
- Dodano `make application-pdfs`, które odświeża CV i zapisuje jednoznacznie nazwane kopie w `output/pdf/`.

## Dane pozostawione do potwierdzenia

Nie wybrano arbitralnie między 80%/50% a ponad jednym dniem/30%+. Do czasu potwierdzenia zakresu i podstawy pomiaru wszystkie warianty opisują skrócenie regresji i zmniejszenie ręcznej weryfikacji bez liczb. Zachowano wspólny, już deklarowany fakt kilku wydań miesięcznie i pięcioosobowego zespołu.

Nie dopisano niepotwierdzonych szczegółów mentoringu, rekrutacji, onboardingu, formalnego sign-off, UAT ani poziomu CEFR języka angielskiego. Zostawiono `Polish; English`. Tytuł QA Engineer / QA Lead w Dolby zachowano wyłącznie przy roku 2021, zgodnie z pełnym źródłem. Zakres line management w tej roli oraz relacja działalności consultingowej do kontraktów pozostają do doprecyzowania przez autora.

Są to pozostałe ograniczenia treści, a nie błędy kompilacji. PDF-y nie zawierają placeholderów ani uwag redakcyjnych.

## Weryfikacja

- `make application-pdfs CC='/Library/TeX/texbin/lualatex -interaction=nonstopmode -halt-on-error'`: zakończone kodem 0, cztery PDF-y po dwie strony. Końcowy log nie zawiera ostrzeżeń, brakujących znaków ani overfull/underfull boxes.
- Obejrzano osiem stron finalnych czterech PDF-ów po ostatniej zmianie składu.
- Poppler 26.09.0, pypdf 6.10.0 i pdfplumber 0.11.9 przy ustawieniach domyślnych zwracają identyczny tekst po normalizacji białych znaków. Profil QA Lead: 600 wyrazów/tokenów oddzielonych białymi znakami; profil automatyzacji: 574. Dodatkowo potwierdzono identyczną treść wariantów kolorowego i ATS.
- Sprawdzono pełne nazwy stanowisk, daty, kontakt, technologie, języki, CTFL, metadane, adresy linków, brak tekstu poza stroną oraz zgodność bajtową nazwanych kopii z eksportami w `examples/`.
- Ustawienia fontu eliminują dwa odtworzone problemy: sklejanie słów przez pdfplumber oraz rozdzielanie `TypeScript` i `TestRail` przez pypdf na skutek kerningu.
- Istniejące testy generatora: `python3 -m unittest discover -s tests -v`, 2/2 przeszły. Dodatkowo wygenerowano testowy list QA Lead bez kompilacji i sprawdzono nową narrację.
- `git diff --check`: bez błędów. Ta weryfikacja poprzedzała przygotowanie lokalnych commitów; nie wykonano pushowania.

Wyniki i skróty SHA-256 są zapisane w [verification.json](/Users/neverased/Codebase/cv-template/output/cv-revision-build/verification.json), a log kompilacji w [final-build.log](/Users/neverased/Codebase/cv-template/output/cv-revision-build/final-build.log). To lokalna kontrola odczytu i składu; nie test komercyjnego ATS ani gwarancja rankingu rekrutacyjnego. Dokumenty nie mają tagów struktury PDF.
