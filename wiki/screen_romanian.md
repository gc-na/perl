# [Linux] C Shell (csh) screen utilizare: Gestionarea sesiunilor terminal

## Overview
Comanda `screen` este un utilitar puternic care permite utilizatorilor să creeze sesiuni terminale multiple, să le gestioneze și să revină la ele chiar și după deconectare. Aceasta este utilă în special pentru utilizatorii care lucrează pe servere sau care doresc să ruleze procese pe termen lung fără a fi nevoie să mențină o conexiune activă.

## Usage
Sintaxa de bază a comenzii `screen` este următoarea:

```bash
screen [options] [arguments]
```

## Common Options
- `-S <name>`: Atribuie un nume specific sesiunii, facilitând identificarea acesteia.
- `-d -r`: Deconectează sesiunea curentă și o reatașează la terminalul curent.
- `-list`: Afișează o listă cu toate sesiunile disponibile.
- `-X <command>`: Trimite un comandă specifică către o sesiune existentă.

## Common Examples
1. **Crearea unei sesiuni noi**:
   ```bash
   screen
   ```

2. **Crearea unei sesiuni cu un nume specific**:
   ```bash
   screen -S sesiune_mea
   ```

3. **Deconectarea de la o sesiune**:
   Apăsați `Ctrl-a` urmat de `d`.

4. **Reatașarea la o sesiune existentă**:
   ```bash
   screen -r sesiune_mea
   ```

5. **Listarea sesiunilor active**:
   ```bash
   screen -list
   ```

6. **Trimiterea unei comenzi către o sesiune**:
   ```bash
   screen -S sesiune_mea -X quit
   ```

## Tips
- Folosiți nume descriptive pentru sesiunile `screen` pentru a le identifica mai ușor.
- Dacă lucrați cu sesiuni lungi, asigurați-vă că salvați progresul regulat, mai ales înainte de a deconecta.
- Familiarizați-vă cu comenzile rapide de la tastatură pentru a naviga mai eficient între sesiuni.