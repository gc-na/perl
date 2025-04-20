# [Linux] C Shell (csh) od: wyświetlanie zawartości plików w różnych formatach

## Overview
Polecenie `od` (octal dump) służy do wyświetlania zawartości plików w różnych formatach, takich jak ósemkowy, szesnastkowy, dziesiętny czy ASCII. Jest to przydatne narzędzie do analizy danych binarnych i tekstowych.

## Usage
Podstawowa składnia polecenia `od` jest następująca:

```bash
od [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `od`:

- `-A, --address-radix=RADIX` - Ustawia system liczbowy dla adresów (np. d dla dziesiętnego, o dla ósemkowego, x dla szesnastkowego).
- `-t, --format=TYPE` - Określa format wyjścia (np. a dla ASCII, o dla ósemkowego, x dla szesnastkowego).
- `-N, --read-bytes=N` - Odczytuje tylko pierwsze N bajtów z pliku.
- `-v, --output-duplicates` - Wyświetla wszystkie dane, w tym duplikaty.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `od`:

1. Wyświetlenie zawartości pliku w formacie szesnastkowym:
   ```bash
   od -x plik.txt
   ```

2. Odczytanie pierwszych 16 bajtów pliku w formacie ósemkowym:
   ```bash
   od -N 16 -o plik.bin
   ```

3. Wyświetlenie zawartości pliku w formacie ASCII:
   ```bash
   od -t a plik.txt
   ```

4. Ustawienie systemu liczbowego na dziesiętny i wyświetlenie adresów:
   ```bash
   od -A d plik.bin
   ```

## Tips
- Używaj opcji `-v`, aby upewnić się, że wszystkie dane są wyświetlane, nawet jeśli są duplikatami.
- Eksperymentuj z różnymi formatami wyjścia, aby lepiej zrozumieć zawartość plików binarnych.
- Pamiętaj, że `od` jest szczególnie przydatne do analizy plików, które nie są przeznaczone do bezpośredniego odczytu przez użytkownika.