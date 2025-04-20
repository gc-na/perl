# [Linux] C Shell (csh) killall użycie: Zakończ procesy na podstawie nazwy

## Przegląd
Polecenie `killall` w C Shell (csh) służy do zakończenia wszystkich procesów o określonej nazwie. Jest to przydatne, gdy chcesz szybko zamknąć wiele instancji programu, które mogą działać w tle.

## Użycie
Podstawowa składnia polecenia `killall` jest następująca:

```
killall [opcje] [argumenty]
```

## Częste opcje
- `-9`: Wymusza natychmiastowe zakończenie procesów.
- `-u [użytkownik]`: Zakończ procesy tylko dla określonego użytkownika.
- `-r`: Użyj wyrażenia regularnego do dopasowania nazw procesów.

## Częste przykłady
Zakończenie wszystkich procesów o nazwie `firefox`:

```csh
killall firefox
```

Wymuszenie zakończenia wszystkich procesów o nazwie `gedit`:

```csh
killall -9 gedit
```

Zakończenie wszystkich procesów `python` dla konkretnego użytkownika:

```csh
killall -u username python
```

Zakończenie procesów, które pasują do wyrażenia regularnego (np. `java`):

```csh
killall -r java.*
```

## Wskazówki
- Używaj opcji `-9` ostrożnie, ponieważ wymusza natychmiastowe zakończenie procesów, co może prowadzić do utraty danych.
- Zawsze sprawdzaj, które procesy będą zakończone, zanim użyjesz `killall`, aby uniknąć przypadkowego zamknięcia ważnych aplikacji.
- Możesz użyć polecenia `ps` przed `killall`, aby zobaczyć, które procesy są uruchomione i upewnić się, że chcesz je zakończyć.