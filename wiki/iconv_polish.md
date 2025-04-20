# [Linux] C Shell (csh) iconv użycie: Konwersja kodowania znaków

## Overview
Polecenie `iconv` służy do konwersji tekstu między różnymi zestawami znaków. Umożliwia użytkownikom przekształcanie plików tekstowych, aby były zgodne z wymaganym kodowaniem, co jest szczególnie przydatne w przypadku pracy z danymi w różnych językach.

## Usage
Podstawowa składnia polecenia `iconv` jest następująca:

```csh
iconv [opcje] [argumenty]
```

## Common Options
- `-f, --from-code=KOD`: Określa kodowanie źródłowe.
- `-t, --to-code=KOD`: Określa kodowanie docelowe.
- `-o, --output=PLIK`: Zapisuje wynik do określonego pliku.
- `-c`: Pomija nieprawidłowe znaki.

## Common Examples
1. Konwersja pliku z kodowania UTF-8 na ISO-8859-1:
   ```csh
   iconv -f UTF-8 -t ISO-8859-1 plik_wejsciowy.txt -o plik_wyjsciowy.txt
   ```

2. Konwersja kodowania z Windows-1250 na UTF-8:
   ```csh
   iconv -f WINDOWS-1250 -t UTF-8 plik_wejsciowy.txt > plik_wyjsciowy.txt
   ```

3. Pomijanie nieprawidłowych znaków podczas konwersji:
   ```csh
   iconv -f UTF-8 -t ASCII//TRANSLIT plik_wejsciowy.txt -o plik_wyjsciowy.txt
   ```

## Tips
- Zawsze sprawdzaj, jakie kodowanie ma plik źródłowy, aby uniknąć błędów konwersji.
- Używaj opcji `-o`, aby zapisać wynik do nowego pliku, zamiast nadpisywać oryginał.
- Przetestuj konwersję na małym pliku przed zastosowaniem na dużych zbiorach danych, aby upewnić się, że wszystko działa poprawnie.