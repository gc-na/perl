# [Linux] C Shell (csh) script Użycie: rejestrowanie sesji terminala

## Overview
Polecenie `script` w C Shell (csh) służy do rejestrowania sesji terminala. Umożliwia tworzenie plików tekstowych, które zawierają wszystkie wprowadzone polecenia oraz ich wyniki, co jest przydatne do dokumentacji lub analizy.

## Usage
Podstawowa składnia polecenia `script` jest następująca:

```
script [opcje] [argumenty]
```

## Common Options
- `-a`: Dodaje dane do istniejącego pliku zamiast go nadpisywać.
- `-f`: Natychmiastowo zapisuje dane do pliku, co może być przydatne w przypadku długich sesji.
- `-q`: Włącza tryb cichy, nie wyświetlając komunikatów o rozpoczęciu i zakończeniu rejestrowania.

## Common Examples
Przykłady użycia polecenia `script`:

1. Rozpoczęcie rejestrowania sesji do pliku `output.txt`:
   ```csh
   script output.txt
   ```

2. Dodanie do istniejącego pliku `output.txt`:
   ```csh
   script -a output.txt
   ```

3. Rozpoczęcie rejestrowania w trybie cichym:
   ```csh
   script -q output.txt
   ```

4. Użycie opcji `-f` do natychmiastowego zapisywania:
   ```csh
   script -f output.txt
   ```

## Tips
- Zawsze sprawdzaj, czy plik, do którego chcesz zapisać, nie istnieje, aby uniknąć przypadkowego nadpisania ważnych danych.
- Używaj opcji `-a`, jeśli chcesz rejestrować wiele sesji w tym samym pliku.
- Po zakończeniu sesji, aby zakończyć rejestrowanie, wystarczy wpisać `exit` lub użyć skrótu klawiszowego `Ctrl+D`.