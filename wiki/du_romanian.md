# [Linux] C Shell (csh) du utilizare: Afișează dimensiunea fișierelor și directoarelor

## Overview
Comanda `du` (disk usage) este utilizată pentru a estima și a afișa dimensiunea fișierelor și directoarelor din sistemul de fișiere. Aceasta ajută utilizatorii să înțeleagă cât spațiu pe disc ocupă anumite fișiere sau directoare.

## Usage
Sintaxa de bază a comenzii `du` este următoarea:

```
du [opțiuni] [argumente]
```

## Common Options
- `-h`: Afișează dimensiunile într-un format ușor de citit (ex. KB, MB, GB).
- `-s`: Afișează doar totalul pentru fiecare argument, fără a detalia subdirectoarele.
- `-a`: Afișează dimensiunea tuturor fișierelor, nu doar a directoarelor.
- `-c`: Afișează un total cumulativ la sfârșitul listării.

## Common Examples
1. Afișarea dimensiunii unui director:
   ```bash
   du /cale/catre/director
   ```

2. Afișarea dimensiunii într-un format ușor de citit:
   ```bash
   du -h /cale/catre/director
   ```

3. Afișarea totalului pentru un director:
   ```bash
   du -sh /cale/catre/director
   ```

4. Afișarea dimensiunii tuturor fișierelor dintr-un director:
   ```bash
   du -ah /cale/catre/director
   ```

5. Afișarea dimensiunii pentru mai multe directoare și un total cumulativ:
   ```bash
   du -ch /cale/catre/director1 /cale/catre/director2
   ```

## Tips
- Folosește opțiunea `-h` pentru a face rezultatele mai ușor de interpretat.
- Combină opțiunile `-s` și `-c` pentru a obține un total rapid al dimensiunii mai multor directoare.
- Verifică periodic dimensiunea directoarelor mari pentru a gestiona eficient spațiul pe disc.