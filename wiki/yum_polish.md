# [Linux] C Shell (csh) yum użycie: Zarządzanie pakietami w systemie Linux

## Overview
Polecenie `yum` (Yellowdog Updater Modified) jest narzędziem do zarządzania pakietami w systemach opartych na Red Hat, takich jak CentOS czy Fedora. Umożliwia instalację, aktualizację i usuwanie oprogramowania, a także zarządzanie repozytoriami.

## Usage
Podstawowa składnia polecenia `yum` jest następująca:

```
yum [opcje] [argumenty]
```

## Common Options
- `install`: Instaluje pakiet.
- `remove`: Usuwa pakiet.
- `update`: Aktualizuje zainstalowane pakiety.
- `search`: Wyszukuje pakiety w repozytoriach.
- `info`: Wyświetla informacje o pakiecie.
- `list`: Wyświetla listę dostępnych pakietów.

## Common Examples
Przykłady użycia polecenia `yum`:

1. Instalacja pakietu:
   ```bash
   yum install nazwa_pakietu
   ```

2. Usuwanie pakietu:
   ```bash
   yum remove nazwa_pakietu
   ```

3. Aktualizacja wszystkich zainstalowanych pakietów:
   ```bash
   yum update
   ```

4. Wyszukiwanie pakietu:
   ```bash
   yum search nazwa_pakietu
   ```

5. Wyświetlanie informacji o pakiecie:
   ```bash
   yum info nazwa_pakietu
   ```

6. Wyświetlanie listy dostępnych pakietów:
   ```bash
   yum list available
   ```

## Tips
- Zawsze sprawdzaj dostępność aktualizacji przed instalacją nowych pakietów, aby uniknąć konfliktów.
- Używaj opcji `-y`, aby automatycznie potwierdzić instalację lub usunięcie pakietu, co przyspiesza proces.
- Regularnie aktualizuj repozytoria, aby mieć dostęp do najnowszych wersji oprogramowania.