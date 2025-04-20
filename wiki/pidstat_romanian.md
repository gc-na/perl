# [Linux] C Shell (csh) pidstat: Monitorizarea utilizării proceselor

## Overview
Comanda `pidstat` este utilizată pentru a monitoriza utilizarea resurselor de către procesele din sistem. Aceasta oferă informații detaliate despre utilizarea CPU, memorie și alte resurse pentru procesele active.

## Usage
Sintaxa de bază a comenzii `pidstat` este următoarea:

```csh
pidstat [options] [arguments]
```

## Common Options
- `-h`: Afișează un antet mai prietenos pentru utilizator.
- `-r`: Afișează utilizarea memoriei pentru procese.
- `-u`: Afișează utilizarea CPU pentru procese.
- `-p <pid>`: Monitorizează un anumit proces specificat prin PID.
- `-t`: Afișează informații despre toate thread-urile din procese.

## Common Examples
1. **Monitorizarea utilizării CPU pentru toate procesele:**
   ```csh
   pidstat -u 1
   ```
   Aceasta va afișa utilizarea CPU pentru toate procesele la fiecare 1 secundă.

2. **Monitorizarea utilizării memoriei pentru un proces specific:**
   ```csh
   pidstat -r -p 1234 1
   ```
   Înlocuiți `1234` cu PID-ul procesului dorit. Aceasta va afișa utilizarea memoriei pentru procesul specificat la fiecare 1 secundă.

3. **Afișarea informațiilor despre toate thread-urile dintr-un proces:**
   ```csh
   pidstat -t -p 5678 1
   ```
   Înlocuiți `5678` cu PID-ul procesului dorit. Aceasta va afișa informații despre thread-urile procesului specificat.

## Tips
- Utilizați opțiunea `-h` pentru a obține o ieșire mai ușor de citit.
- Combinați opțiunile pentru a obține informații detaliate despre utilizarea resurselor.
- Monitorizați procesele în timp real pentru a identifica problemele de performanță sau utilizarea excesivă a resurselor.