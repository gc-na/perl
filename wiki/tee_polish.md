# [Linux] C Shell (csh) tee użycie: Zapisz dane do pliku i wyświetl je na standardowym wyjściu

## Overview
Polecenie `tee` w C Shell (csh) jest używane do odczytywania danych ze standardowego wejścia i jednoczesnego zapisywania ich do jednego lub więcej plików. Dzięki temu można zobaczyć dane na ekranie, a jednocześnie zapisać je do pliku.

## Usage
Podstawowa składnia polecenia `tee` wygląda następująco:

```
tee [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `tee`:

- `-a` - dodaje dane do istniejącego pliku zamiast go nadpisywać.
- `-i` - ignoruje sygnał przerwania (SIGINT), co pozwala na kontynuowanie działania polecenia.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `tee`:

1. Zapisz dane do pliku i wyświetl je na ekranie:
   ```csh
   echo "Hello, World!" | tee output.txt
   ```

2. Dodaj dane do istniejącego pliku:
   ```csh
   echo "Nowa linia" | tee -a output.txt
   ```

3. Użyj `tee` w potoku, aby zapisać wynik innego polecenia:
   ```csh
   ls -l | tee directory_list.txt
   ```

4. Ignoruj sygnał przerwania podczas zapisywania danych:
   ```csh
   some_command | tee -i output.txt
   ```

## Tips
- Używaj opcji `-a`, gdy chcesz dodać dane do pliku, aby uniknąć przypadkowego nadpisania ważnych informacji.
- Możesz używać `tee` w połączeniu z innymi poleceniami w potokach, aby lepiej zarządzać danymi.
- Sprawdź zawartość pliku po użyciu `tee`, aby upewnić się, że dane zostały zapisane poprawnie.