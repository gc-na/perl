# [Linux] C Shell (csh) last użycie: wyświetlanie ostatnich logowań użytkowników

## Overview
Polecenie `last` w C Shell (csh) służy do wyświetlania listy ostatnich logowań użytkowników na systemie. Informacje te są pobierane z pliku `/var/log/wtmp`, który rejestruje wszystkie logowania i wylogowania.

## Usage
Podstawowa składnia polecenia `last` jest następująca:

```
last [opcje] [argumenty]
```

## Common Options
- `-n <liczba>`: Wyświetla określoną liczbę ostatnich logowań.
- `-R`: Nie wyświetla nazwy hosta.
- `-f <plik>`: Używa podanego pliku zamiast domyślnego `/var/log/wtmp`.

## Common Examples
- Aby wyświetlić wszystkie ostatnie logowania:
  ```csh
  last
  ```

- Aby wyświetlić ostatnie 5 logowań:
  ```csh
  last -n 5
  ```

- Aby wyświetlić logowania bez nazw hostów:
  ```csh
  last -R
  ```

- Aby użyć innego pliku z logami:
  ```csh
  last -f /path/to/your/logfile
  ```

## Tips
- Regularnie sprawdzaj logi, aby monitorować aktywność użytkowników w systemie.
- Używaj opcji `-n`, aby ograniczyć wyświetlane logi do najbardziej istotnych informacji.
- Zrozumienie logów może pomóc w identyfikacji nieautoryzowanych prób logowania.