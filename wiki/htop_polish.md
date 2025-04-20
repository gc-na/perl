# [Linux] C Shell (csh) htop użycie: Monitorowanie procesów systemowych

## Overview
Polecenie `htop` to interaktywne narzędzie do monitorowania procesów w systemie Linux. Umożliwia użytkownikom przeglądanie i zarządzanie uruchomionymi procesami w bardziej przyjazny sposób niż tradycyjne `top`, oferując kolorowe wyświetlenie oraz możliwość łatwego sortowania i filtrowania.

## Usage
Podstawowa składnia polecenia `htop` jest następująca:

```bash
htop [opcje] [argumenty]
```

## Common Options
- `-h`, `--help`: Wyświetla pomoc i dostępne opcje.
- `-v`, `--version`: Wyświetla wersję programu.
- `-C`, `--no-color`: Uruchamia htop bez kolorów.
- `-s`, `--sort`: Umożliwia sortowanie procesów według określonego kryterium, np. CPU lub pamięci.

## Common Examples
- Aby uruchomić `htop` w domyślnym trybie, wystarczy wpisać:

```bash
htop
```

- Aby uruchomić `htop` bez kolorów:

```bash
htop -C
```

- Aby uzyskać pomoc dotyczącą opcji:

```bash
htop -h
```

- Aby posortować procesy według użycia CPU:

```bash
htop -s PERCENT_CPU
```

## Tips
- Użyj klawiszy strzałek do nawigacji po procesach i `F9`, aby zakończyć wybrany proces.
- Możesz filtrować procesy, naciskając `F3` i wpisując nazwę procesu.
- Aby zmienić priorytet procesu, wybierz go i naciśnij `F7` (zwiększenie priorytetu) lub `F8` (zmniejszenie priorytetu).