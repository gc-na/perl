# [Linux] C Shell (csh) xz użycie: Kompresja i dekompresja plików

## Overview
Polecenie `xz` służy do kompresji i dekompresji plików przy użyciu algorytmu LZMA. Jest to narzędzie, które pozwala na znaczne zmniejszenie rozmiaru plików, co jest przydatne w przypadku przechowywania lub przesyłania danych.

## Usage
Podstawowa składnia polecenia `xz` jest następująca:

```csh
xz [options] [arguments]
```

## Common Options
- `-d`, `--decompress`: Dekompresuje plik.
- `-k`, `--keep`: Zachowuje oryginalny plik po kompresji.
- `-f`, `--force`: Wymusza nadpisanie istniejących plików.
- `-v`, `--verbose`: Wyświetla szczegółowe informacje podczas kompresji lub dekompresji.
- `-z`, `--compress`: Kompresuje plik (domyślna opcja).

## Common Examples
Kompresja pliku:

```csh
xz myfile.txt
```

Dekompresja pliku:

```csh
xz -d myfile.txt.xz
```

Kompresja pliku z zachowaniem oryginału:

```csh
xz -k myfile.txt
```

Wyświetlenie szczegółowych informacji podczas kompresji:

```csh
xz -v myfile.txt
```

## Tips
- Używaj opcji `-k`, jeśli chcesz zachować oryginalny plik po kompresji.
- Sprawdzaj rozmiar plików przed i po kompresji, aby ocenić efektywność.
- Zwracaj uwagę na pliki, które są już skompresowane (np. pliki `.zip`), ponieważ dalsza kompresja może nie przynieść znaczących oszczędności.