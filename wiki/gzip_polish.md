# [Linux] C Shell (csh) gzip użycie: Kompresja plików

## Overview
Polecenie `gzip` służy do kompresji plików, zmniejszając ich rozmiar, co ułatwia przechowywanie i przesyłanie danych. `gzip` jest powszechnie używane w systemach Unix i Linux do kompresji plików tekstowych i binarnych.

## Usage
Podstawowa składnia polecenia `gzip` jest następująca:

```
gzip [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `gzip`:

- `-d` lub `--decompress`: Dekompresuje plik.
- `-k` lub `--keep`: Zachowuje oryginalny plik po kompresji.
- `-v` lub `--verbose`: Wyświetla szczegółowe informacje o procesie kompresji.
- `-r` lub `--recursive`: Kompresuje pliki w katalogach rekurencyjnie.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `gzip`:

1. Kompresja pliku:
   ```bash
   gzip plik.txt
   ```

2. Dekomprensja pliku:
   ```bash
   gzip -d plik.txt.gz
   ```

3. Kompresja pliku z zachowaniem oryginału:
   ```bash
   gzip -k plik.txt
   ```

4. Kompresja wszystkich plików w katalogu:
   ```bash
   gzip *.txt
   ```

5. Kompresja rekurencyjna w katalogu:
   ```bash
   gzip -r katalog/
   ```

## Tips
- Używaj opcji `-v`, aby monitorować postęp kompresji i uzyskać informacje o rozmiarze plików.
- Zawsze sprawdzaj, czy masz wystarczająco dużo miejsca na dysku przed kompresją dużych plików.
- Pamiętaj, że pliki skompresowane za pomocą `gzip` mają rozszerzenie `.gz`, co ułatwia ich identyfikację.