# [Linux] C Shell (csh) gunzip utilizare: Dezarhivează fișierele comprimate

## Overview
Comanda `gunzip` este utilizată pentru a dezarhiva fișierele comprimate în format gzip. Aceasta elimină compresia și restabilește fișierele originale, făcându-le disponibile pentru utilizare.

## Usage
Sintaxa de bază a comenzii `gunzip` este următoarea:

```
gunzip [opțiuni] [argumente]
```

## Common Options
- `-c`: Scrie rezultatul pe stdout (standard output) în loc să suprascrie fișierul original.
- `-f`: Forțează dezarhivarea fișierelor, chiar dacă acestea sunt deja dezarhivate.
- `-k`: Păstrează fișierul original după dezarhivare.
- `-r`: Dezarchivează recursiv fișierele din directoare.

## Common Examples
1. Dezarhivarea unui fișier gzip:
   ```bash
   gunzip fisier.txt.gz
   ```

2. Dezarhivarea și păstrarea fișierului original:
   ```bash
   gunzip -k fisier.txt.gz
   ```

3. Scrierea rezultatului pe stdout:
   ```bash
   gunzip -c fisier.txt.gz > fisier_dezarhivat.txt
   ```

4. Dezarhivarea recursivă a tuturor fișierelor gzip dintr-un director:
   ```bash
   gunzip -r /cale/catre/director
   ```

## Tips
- Verificați întotdeauna dacă aveți suficient spațiu pe disc înainte de a dezarhiva fișiere mari.
- Utilizați opțiunea `-k` dacă doriți să păstrați fișierul comprimat pentru utilizări viitoare.
- Dacă lucrați cu fișiere multiple, luați în considerare utilizarea wildcard-urilor pentru a simplifica comanda.