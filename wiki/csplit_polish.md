# [Linux] C Shell (csh) csplit <Podział plików tekstowych>: Dzieli plik tekstowy na mniejsze części

## Overview
Polecenie `csplit` w C Shell (csh) służy do dzielenia plików tekstowych na mniejsze fragmenty na podstawie określonych wzorców lub liczby linii. Jest to przydatne, gdy potrzebujesz podzielić duży plik na mniejsze, łatwiejsze do zarządzania części.

## Usage
Podstawowa składnia polecenia `csplit` wygląda następująco:

```bash
csplit [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla `csplit`:

- `-f PREFIX` - Umożliwia określenie prefiksu dla nazw plików wynikowych.
- `-n NUM` - Umożliwia określenie liczby cyfr w numerze pliku wynikowego.
- `-b SUFFIX` - Umożliwia określenie sufiksu dla nazw plików wynikowych.
- `-k` - Zachowuje pliki wynikowe nawet w przypadku błędów.

## Common Examples

### Przykład 1: Podział pliku na podstawie liczby linii
Aby podzielić plik `dane.txt` na części po 100 linijek, użyj:

```bash
csplit dane.txt 100
```

### Przykład 2: Podział pliku na podstawie wzorca
Aby podzielić plik `raport.txt` na części, gdzie występuje słowo "Rozdział", użyj:

```bash
csplit raport.txt /Rozdział/
```

### Przykład 3: Użycie prefiksu dla plików wynikowych
Aby podzielić plik `notatki.txt` na części i nadać im prefiks `czesc`, użyj:

```bash
csplit -f czesc notatki.txt 100
```

### Przykład 4: Zachowanie plików w przypadku błędów
Aby podzielić plik `log.txt` i zachować pliki nawet w przypadku błędów, użyj:

```bash
csplit -k log.txt /Błąd/
```

## Tips
- Zawsze przetestuj `csplit` na kopii pliku, aby uniknąć utraty danych.
- Używaj opcji `-n` dla lepszej organizacji plików wynikowych, zwłaszcza gdy dzielisz duże pliki.
- Sprawdź dokumentację `man csplit`, aby uzyskać więcej informacji o dostępnych opcjach i ich zastosowaniach.