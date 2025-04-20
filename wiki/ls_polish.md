# [Linux] C Shell (csh) ls użycie: wyświetlanie zawartości katalogu

## Overview
Polecenie `ls` w C Shell (csh) służy do wyświetlania zawartości katalogu. Umożliwia użytkownikom przeglądanie plików i folderów znajdujących się w określonym katalogu.

## Usage
Podstawowa składnia polecenia `ls` jest następująca:

```
ls [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `ls`:

- `-l`: Wyświetla szczegółowy widok plików, w tym uprawnienia, właściciela, rozmiar i datę modyfikacji.
- `-a`: Wyświetla wszystkie pliki, w tym ukryte (zaczynające się od kropki).
- `-h`: Wyświetla rozmiary plików w formacie czytelnym dla ludzi (np. KB, MB).
- `-R`: Rekurencyjnie wyświetla zawartość wszystkich podkatalogów.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `ls`:

1. Wyświetlenie zawartości bieżącego katalogu:
   ```csh
   ls
   ```

2. Wyświetlenie szczegółowego widoku plików:
   ```csh
   ls -l
   ```

3. Wyświetlenie wszystkich plików, w tym ukrytych:
   ```csh
   ls -a
   ```

4. Wyświetlenie zawartości katalogu z rozmiarami plików w formacie czytelnym:
   ```csh
   ls -lh
   ```

5. Rekurencyjne wyświetlenie zawartości katalogu i jego podkatalogów:
   ```csh
   ls -R
   ```

## Tips
- Używaj opcji `-l` w połączeniu z `-h`, aby uzyskać szczegółowe informacje o plikach w czytelnym formacie.
- Aby szybko sprawdzić, które pliki są ukryte, użyj opcji `-a`.
- Możesz łączyć różne opcje, na przykład `ls -la` wyświetli szczegółowy widok wszystkich plików, w tym ukrytych.