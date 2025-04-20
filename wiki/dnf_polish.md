# [Linux] C Shell (csh) dnf użycie: zarządzanie pakietami

## Overview
Polecenie `dnf` (Dandified YUM) jest menedżerem pakietów dla systemów Linux, który umożliwia instalację, aktualizację i usuwanie oprogramowania. Jest to nowoczesna wersja YUM, oferująca lepszą wydajność i więcej funkcji.

## Usage
Podstawowa składnia polecenia `dnf` jest następująca:

```bash
dnf [opcje] [argumenty]
```

## Common Options
- `install`: Instalacja pakietu.
- `remove`: Usunięcie pakietu.
- `update`: Aktualizacja zainstalowanych pakietów.
- `search`: Wyszukiwanie pakietów w repozytoriach.
- `info`: Wyświetlenie informacji o pakiecie.

## Common Examples
- Instalacja pakietu:
  ```bash
  dnf install nazwa_pakietu
  ```

- Usunięcie pakietu:
  ```bash
  dnf remove nazwa_pakietu
  ```

- Aktualizacja wszystkich zainstalowanych pakietów:
  ```bash
  dnf update
  ```

- Wyszukiwanie pakietu:
  ```bash
  dnf search nazwa_pakietu
  ```

- Wyświetlenie informacji o pakiecie:
  ```bash
  dnf info nazwa_pakietu
  ```

## Tips
- Zawsze sprawdzaj dostępność aktualizacji przed instalacją nowych pakietów, aby zapewnić zgodność.
- Używaj opcji `-y`, aby automatycznie potwierdzać wszystkie pytania podczas instalacji lub aktualizacji.
- Regularnie przeglądaj zainstalowane pakiety, aby utrzymać system w czystości i porządku.