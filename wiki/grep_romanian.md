# [Linux] C Shell (csh) grep utilizare: Căutare de text în fișiere

## Overview
Comanda `grep` este utilizată pentru a căuta un text specific în fișiere. Aceasta returnează liniile care conțin șirul de căutare, fiind un instrument esențial pentru analiza și filtrarea datelor.

## Usage
Sintaxa de bază a comenzii `grep` este următoarea:
```
grep [opțiuni] [argumente]
```

## Common Options
- `-i`: Ignoră diferențele dintre literele mari și mici.
- `-v`: Afișează liniile care nu conțin șirul de căutare.
- `-r`: Caută recursiv în directoare.
- `-n`: Afișează numerele liniilor în care apare șirul de căutare.
- `-l`: Afișează doar numele fișierelor care conțin șirul de căutare.

## Common Examples
1. Căutarea unui șir de text într-un fișier:
   ```bash
   grep "text_cautat" fisier.txt
   ```

2. Căutarea unui șir de text ignorând literele mari și mici:
   ```bash
   grep -i "text_cautat" fisier.txt
   ```

3. Căutarea recursivă a unui șir de text în toate fișierele dintr-un director:
   ```bash
   grep -r "text_cautat" /cale/catre/director
   ```

4. Afișarea liniilor care nu conțin un anumit șir:
   ```bash
   grep -v "text_cautat" fisier.txt
   ```

5. Afișarea numărului liniilor în care apare un șir:
   ```bash
   grep -n "text_cautat" fisier.txt
   ```

## Tips
- Folosește opțiunea `-i` pentru a face căutările mai flexibile, mai ales când nu ești sigur de capitalizarea textului.
- Combină `grep` cu alte comenzi folosind pipe (`|`) pentru a filtra rezultatele. De exemplu, `cat fisier.txt | grep "text_cautat"`.
- Salvează rezultatele căutărilor într-un fișier folosind redirecționarea: `grep "text_cautat" fisier.txt > rezultate.txt`.