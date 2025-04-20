# [Linux] C Shell (csh) bzip2 Użycie: Kompresja plików

## Overview
Polecenie `bzip2` służy do kompresji plików, zmniejszając ich rozmiar, co ułatwia przechowywanie i przesyłanie. Używa algorytmu kompresji Burrows-Wheeler, który jest skuteczny w redukcji rozmiaru danych.

## Usage
Podstawowa składnia polecenia `bzip2` jest następująca:

```
bzip2 [opcje] [argumenty]
```

## Common Options
- `-d` lub `--decompress`: Dekompresuje plik.
- `-k` lub `--keep`: Zachowuje oryginalny plik po kompresji.
- `-f` lub `--force`: Wymusza nadpisanie istniejących plików.
- `-v` lub `--verbose`: Wyświetla szczegółowe informacje o postępie kompresji.

## Common Examples
- Kompresja pliku:
  ```bash
  bzip2 plik.txt
  ```
- Dekompresja pliku:
  ```bash
  bzip2 -d plik.txt.bz2
  ```
- Kompresja z zachowaniem oryginalnego pliku:
  ```bash
  bzip2 -k plik.txt
  ```
- Wymuszenie nadpisania istniejącego pliku:
  ```bash
  bzip2 -f plik.txt
  ```
- Wyświetlenie szczegółowych informacji podczas kompresji:
  ```bash
  bzip2 -v plik.txt
  ```

## Tips
- Zawsze sprawdzaj, czy masz wystarczająco dużo miejsca na dysku przed kompresją dużych plików.
- Używaj opcji `-k`, jeśli chcesz zachować oryginał pliku, aby uniknąć przypadkowej utraty danych.
- Regularnie dekompresuj pliki, aby upewnić się, że proces kompresji działa poprawnie i pliki są nienaruszone.