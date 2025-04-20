# [Linux] C Shell (csh) split użycie: Dzieli pliki na mniejsze części

## Overview
Polecenie `split` w C Shell (csh) służy do dzielenia dużych plików na mniejsze fragmenty. Jest to przydatne, gdy chcemy ułatwić zarządzanie dużymi plikami lub przesyłać je w mniejszych częściach.

## Usage
Podstawowa składnia polecenia `split` wygląda następująco:

```csh
split [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `split`:

- `-b [rozmiar]` - Dzieli plik na fragmenty o określonym rozmiarze (np. `-b 1M` dla 1 MB).
- `-l [liczba]` - Dzieli plik na fragmenty zawierające określoną liczbę linii.
- `-d` - Używa cyfr zamiast liter do nazewnictwa fragmentów.
- `--additional-suffix=[sufiks]` - Dodaje dodatkowy sufiks do nazw fragmentów.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `split`:

1. Dzieli plik `duzy_plik.txt` na fragmenty po 1000 linii:
   ```csh
   split -l 1000 duzy_plik.txt
   ```

2. Dzieli plik `duzy_plik.txt` na fragmenty o rozmiarze 1 MB:
   ```csh
   split -b 1M duzy_plik.txt
   ```

3. Dzieli plik `duzy_plik.txt` na fragmenty z numerami zamiast liter:
   ```csh
   split -d -l 500 duzy_plik.txt
   ```

4. Dzieli plik `duzy_plik.txt` na fragmenty z dodatkowym sufiksem `.part`:
   ```csh
   split --additional-suffix=.part -l 200 duzy_plik.txt
   ```

## Tips
- Używaj opcji `-d`, aby łatwiej zarządzać fragmentami, szczególnie gdy dzielisz duże pliki.
- Sprawdzaj rozmiar fragmentów, aby upewnić się, że są one odpowiednie do dalszego przetwarzania lub przesyłania.
- Zawsze przetestuj polecenie na mniejszych plikach, aby upewnić się, że działa zgodnie z oczekiwaniami, zanim zastosujesz je do dużych danych.