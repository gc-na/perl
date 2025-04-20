# [Linux] C Shell (csh) awk użycie: Przetwarzanie tekstu i danych

## Overview
`awk` to potężne narzędzie do przetwarzania tekstu, które umożliwia analizę i manipulację danymi w plikach tekstowych. Jest szczególnie przydatne do przetwarzania danych w formacie kolumnowym, co czyni go idealnym do pracy z plikami CSV i innymi strukturami danych.

## Usage
Podstawowa składnia polecenia `awk` jest następująca:

```bash
awk [opcje] [argumenty]
```

## Common Options
- `-F` : Ustawia separator pól, domyślnie jest to spacja.
- `-v` : Umożliwia przekazywanie zmiennych do skryptu `awk`.
- `-f` : Umożliwia załadowanie skryptu `awk` z pliku.

## Common Examples
1. **Wyświetlenie drugiej kolumny z pliku:**
   ```bash
   awk '{print $2}' plik.txt
   ```

2. **Użycie innego separatora (np. przecinek):**
   ```bash
   awk -F, '{print $1}' plik.csv
   ```

3. **Filtracja wierszy na podstawie warunku:**
   ```bash
   awk '$3 > 50 {print $1, $2}' plik.txt
   ```

4. **Zliczanie liczby wierszy w pliku:**
   ```bash
   awk 'END {print NR}' plik.txt
   ```

5. **Przekazywanie zmiennej do skryptu:**
   ```bash
   awk -v prog=10 '$1 > prog {print $0}' plik.txt
   ```

## Tips
- Używaj opcji `-F`, aby dostosować separator pól do formatu swojego pliku.
- Możesz łączyć wiele warunków w jednym poleceniu `awk`, co zwiększa jego elastyczność.
- Przechowuj często używane skrypty `awk` w plikach, aby móc je łatwo ponownie wykorzystać z opcją `-f`.