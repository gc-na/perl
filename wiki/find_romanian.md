# [Linux] C Shell (csh) find utilizare: găsirea numelui fișierelor

## Overview
Comanda `find` este utilizată pentru a căuta fișiere și directoare într-o ierarhie de directoare. Aceasta permite utilizatorilor să localizeze fișiere pe baza unor criterii specifice, cum ar fi numele, tipul, dimensiunea sau data ultimei modificări.

## Usage
Sintaxa de bază a comenzii `find` este următoarea:

```
find [opțiuni] [argumente]
```

## Common Options
- `-name`: caută fișiere după numele specificat.
- `-type`: filtrează rezultatele după tipul fișierului (de exemplu, `f` pentru fișiere obișnuite, `d` pentru directoare).
- `-size`: caută fișiere în funcție de dimensiune (de exemplu, `+100k` pentru fișiere mai mari de 100KB).
- `-mtime`: caută fișiere modificate în ultimele n zile (de exemplu, `-mtime -7` pentru fișiere modificate în ultima săptămână).
- `-exec`: permite executarea unei comenzi pe fiecare fișier găsit.

## Common Examples
1. Căutarea unui fișier după nume:
   ```csh
   find /cale/catre/director -name "fisier.txt"
   ```

2. Căutarea tuturor directoarelor:
   ```csh
   find /cale/catre/director -type d
   ```

3. Căutarea fișierelor mai mari de 1MB:
   ```csh
   find /cale/catre/director -size +1M
   ```

4. Căutarea fișierelor modificate în ultimele 5 zile:
   ```csh
   find /cale/catre/director -mtime -5
   ```

5. Executarea unei comenzi pe fiecare fișier găsit:
   ```csh
   find /cale/catre/director -name "*.log" -exec rm {} \;
   ```

## Tips
- Folosiți `-print` pentru a afișa rezultatele în cazul în care comanda nu le afișează implicit.
- Fiți atenți la utilizarea opțiunii `-exec`, deoarece poate modifica sau șterge fișierele.
- Testați comenzile cu `-print` înainte de a folosi `-exec` pentru a evita ștergerea accidentală a fișierelor.