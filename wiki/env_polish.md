# [Linux] C Shell (csh) env <Użycie: zarządzanie zmiennymi środowiskowymi>

## Overview
Polecenie `env` w C Shell (csh) służy do wyświetlania lub ustawiania zmiennych środowiskowych. Umożliwia uruchamianie programów w zmodyfikowanym środowisku, co jest przydatne w wielu scenariuszach, takich jak testowanie lub uruchamianie aplikacji z określonymi ustawieniami.

## Usage
Podstawowa składnia polecenia `env` jest następująca:

```csh
env [opcje] [argumenty]
```

## Common Options
- `-i`: Uruchamia polecenie w całkowicie pustym środowisku, bez żadnych zmiennych środowiskowych.
- `-u VAR`: Usuwa zmienną środowiskową o nazwie VAR przed uruchomieniem polecenia.
- `VAR=value`: Ustawia zmienną środowiskową VAR na wartość `value` przed uruchomieniem polecenia.

## Common Examples
1. Wyświetlenie wszystkich zmiennych środowiskowych:
   ```csh
   env
   ```

2. Uruchomienie programu z określoną zmienną środowiskową:
   ```csh
   env MY_VAR=example ./my_program
   ```

3. Usunięcie zmiennej środowiskowej przed uruchomieniem programu:
   ```csh
   env -u MY_VAR ./my_program
   ```

4. Uruchomienie polecenia w pustym środowisku:
   ```csh
   env -i ./my_program
   ```

## Tips
- Używaj opcji `-i`, gdy chcesz mieć pewność, że program nie korzysta z żadnych istniejących zmiennych środowiskowych.
- Możesz ustawiać wiele zmiennych środowiskowych przed uruchomieniem polecenia, oddzielając je spacjami:
  ```csh
  env VAR1=value1 VAR2=value2 ./my_program
  ```
- Sprawdzaj zmienne środowiskowe za pomocą `echo $VAR`, aby upewnić się, że są poprawnie ustawione przed uruchomieniem programu.