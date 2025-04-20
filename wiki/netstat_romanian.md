# [Linux] C Shell (csh) netstat Utilizare: Afișează conexiunile de rețea

## Overview
Comanda `netstat` este utilizată pentru a afișa informații despre conexiunile de rețea, tabelele de rutare și statisticile interfețelor de rețea. Aceasta este un instrument esențial pentru diagnosticarea problemelor de rețea și monitorizarea activităților de rețea ale sistemului.

## Usage
Sintaxa de bază a comenzii `netstat` este următoarea:

```bash
netstat [options] [arguments]
```

## Common Options
- `-a`: Afișează toate conexiunile și porturile de ascultare.
- `-n`: Afișează adresele IP și numerele de port în format numeric, fără a le rezolva în nume de gazde.
- `-t`: Afișează doar conexiunile TCP.
- `-u`: Afișează doar conexiunile UDP.
- `-l`: Afișează doar porturile care sunt în stare de ascultare.
- `-p`: Afișează procesul care utilizează fiecare conexiune.

## Common Examples
1. Afișarea tuturor conexiunilor active și a porturilor de ascultare:
   ```bash
   netstat -a
   ```

2. Afișarea conexiunilor TCP în format numeric:
   ```bash
   netstat -tn
   ```

3. Afișarea conexiunilor UDP:
   ```bash
   netstat -u
   ```

4. Afișarea porturilor în stare de ascultare:
   ```bash
   netstat -l
   ```

5. Afișarea proceselor asociate cu fiecare conexiune:
   ```bash
   netstat -p
   ```

## Tips
- Utilizați opțiunea `-n` pentru a obține rezultate mai rapide, evitând rezolvarea numelui gazdelor.
- Combinați opțiunile pentru a obține informații mai detaliate, de exemplu, `netstat -tunlp` pentru a vedea toate conexiunile TCP și UDP, împreună cu procesele asociate.
- Rulați comanda cu privilegii de administrator pentru a obține informații complete despre toate conexiunile de rețea.