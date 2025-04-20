# [Linux] C Shell (csh) pr: formatowanie plików tekstowych

## Overview
Polecenie `pr` służy do formatowania plików tekstowych, przygotowując je do wydruku. Umożliwia podział tekstu na strony, dodawanie nagłówków oraz numerów stron, co ułatwia przeglądanie i drukowanie dokumentów.

## Usage
Podstawowa składnia polecenia `pr` jest następująca:

```
pr [opcje] [argumenty]
```

## Common Options
- `-h` : Umożliwia dodanie nagłówka do każdej strony.
- `-l` : Ustala długość strony w liniach.
- `-w` : Ustala szerokość strony w znakach.
- `-s` : Umożliwia dodanie separatora między kolumnami.

## Common Examples
1. **Podstawowe formatowanie pliku:**
   ```csh
   pr dokument.txt
   ```

2. **Dodanie nagłówka do każdej strony:**
   ```csh
   pr -h "Mój dokument" dokument.txt
   ```

3. **Ustalenie długości strony na 50 linii:**
   ```csh
   pr -l 50 dokument.txt
   ```

4. **Formatowanie z wieloma kolumnami:**
   ```csh
   pr -s " | " -w 80 dokument.txt
   ```

## Tips
- Używaj opcji `-h`, aby dodać kontekst do wydruku, co może być przydatne w przypadku dłuższych dokumentów.
- Eksperymentuj z różnymi wartościami opcji `-l` i `-w`, aby dostosować formatowanie do swoich potrzeb.
- Sprawdź wynik formatowania w terminalu przed wydrukiem, aby upewnić się, że wszystko wygląda zgodnie z oczekiwaniami.