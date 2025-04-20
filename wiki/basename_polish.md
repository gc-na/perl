# [Linux] C Shell (csh) basename użycie: Zwraca nazwę pliku bez ścieżki

## Overview
Polecenie `basename` służy do zwracania nazwy pliku bez jego ścieżki. Jest to przydatne, gdy chcesz uzyskać samą nazwę pliku z pełnej ścieżki.

## Usage
Podstawowa składnia polecenia `basename` jest następująca:

```csh
basename [opcje] [argumenty]
```

## Common Options
- `-a`: Przetwarza wiele argumentów i zwraca nazwę dla każdego z nich.
- `-s`: Usuwa podany sufiks z nazwy pliku.

## Common Examples
1. Zwrócenie nazwy pliku z pełnej ścieżki:
   ```csh
   basename /home/użytkownik/dokumenty/plik.txt
   ```
   Wynik: `plik.txt`

2. Usunięcie sufiksu z nazwy pliku:
   ```csh
   basename plik.txt .txt
   ```
   Wynik: `plik`

3. Przetwarzanie wielu plików:
   ```csh
   basename -a /home/użytkownik/dokumenty/plik1.txt /home/użytkownik/dokumenty/plik2.txt
   ```
   Wynik:
   ```
   plik1.txt
   plik2.txt
   ```

## Tips
- Używaj opcji `-s`, aby łatwo usunąć rozszerzenia plików, co może być przydatne w skryptach.
- Możesz używać `basename` w połączeniu z innymi poleceniami, aby dynamicznie przetwarzać nazwy plików w skryptach powłoki.