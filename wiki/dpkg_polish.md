# [Linux] C Shell (csh) dpkg użycie: Zarządzanie pakietami w systemie Debian

## Overview
Polecenie `dpkg` jest narzędziem do zarządzania pakietami w systemach opartych na Debianie. Umożliwia instalację, usuwanie oraz zarządzanie pakietami .deb, a także sprawdzanie ich statusu.

## Usage
Podstawowa składnia polecenia `dpkg` jest następująca:

```
dpkg [opcje] [argumenty]
```

## Common Options
- `-i` : Instalacja pakietu .deb.
- `-r` : Usunięcie zainstalowanego pakietu.
- `-l` : Wyświetlenie listy zainstalowanych pakietów.
- `-s` : Wyświetlenie statusu określonego pakietu.
- `-L` : Wyświetlenie plików zainstalowanych przez dany pakiet.

## Common Examples
- Instalacja pakietu:
    ```bash
    dpkg -i nazwa_pakietu.deb
    ```

- Usunięcie pakietu:
    ```bash
    dpkg -r nazwa_pakietu
    ```

- Wyświetlenie listy zainstalowanych pakietów:
    ```bash
    dpkg -l
    ```

- Sprawdzenie statusu pakietu:
    ```bash
    dpkg -s nazwa_pakietu
    ```

- Wyświetlenie plików zainstalowanych przez pakiet:
    ```bash
    dpkg -L nazwa_pakietu
    ```

## Tips
- Zawsze sprawdzaj zależności pakietów przed ich instalacją, aby uniknąć problemów.
- Używaj `dpkg` w połączeniu z `apt` dla lepszej obsługi zależności.
- Regularnie aktualizuj listę pakietów, aby mieć dostęp do najnowszych wersji.