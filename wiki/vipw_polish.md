# [Linux] C Shell (csh) vipw użycie: Edytowanie pliku haseł

## Overview
Polecenie `vipw` służy do bezpiecznego edytowania pliku haseł systemu. Umożliwia użytkownikom modyfikację pliku `/etc/passwd` oraz `/etc/shadow` w sposób, który minimalizuje ryzyko uszkodzenia tych krytycznych plików.

## Usage
Podstawowa składnia polecenia `vipw` jest następująca:

```
vipw [opcje]
```

## Common Options
- `-s` : Edytuje plik `/etc/shadow` zamiast `/etc/passwd`.
- `-c` : Sprawdza poprawność pliku haseł przed zapisaniem zmian.

## Common Examples
1. Edytowanie pliku haseł:
   ```bash
   vipw
   ```

2. Edytowanie pliku haseł z użyciem opcji `-s`:
   ```bash
   vipw -s
   ```

3. Edytowanie pliku haseł i sprawdzanie poprawności:
   ```bash
   vipw -c
   ```

## Tips
- Zawsze używaj `vipw` zamiast edytorów tekstowych, aby uniknąć uszkodzenia pliku haseł.
- Przed wprowadzeniem zmian, upewnij się, że masz kopię zapasową pliku haseł.
- Po zakończeniu edycji, sprawdź, czy wszystkie zmiany zostały poprawnie zapisane i czy nie wystąpiły żadne błędy.