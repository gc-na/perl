# [Linux] C Shell (csh) df Utilizare: Afișează informații despre sistemul de fișiere

## Overview
Comanda `df` este utilizată pentru a afișa informații despre utilizarea sistemului de fișiere, inclusiv spațiul total, spațiul utilizat și spațiul disponibil pe fiecare sistem de fișiere montat.

## Usage
Sintaxa de bază a comenzii `df` este următoarea:

```
df [options] [arguments]
```

## Common Options
- `-h`: Afișează dimensiunile într-un format ușor de citit (ex. K, M, G).
- `-T`: Afișează tipul sistemului de fișiere.
- `-i`: Afișează informații despre inode-uri în loc de blocuri.
- `-a`: Include sistemele de fișiere care au dimensiunea 0.

## Common Examples
1. **Afișarea informațiilor de bază despre sistemele de fișiere:**
   ```shell
   df
   ```

2. **Afișarea informațiilor într-un format ușor de citit:**
   ```shell
   df -h
   ```

3. **Afișarea tipului sistemului de fișiere:**
   ```shell
   df -T
   ```

4. **Afișarea informațiilor despre inode-uri:**
   ```shell
   df -i
   ```

5. **Afișarea tuturor sistemelor de fișiere, inclusiv cele cu dimensiunea 0:**
   ```shell
   df -a
   ```

## Tips
- Utilizați opțiunea `-h` pentru a face datele mai ușor de interpretat, mai ales când lucrați cu dimensiuni mari.
- Verificați periodic utilizarea sistemului de fișiere pentru a evita problemele de spațiu.
- Comanda `df` poate fi combinată cu alte comenzi, cum ar fi `grep`, pentru a filtra rezultatele. De exemplu:
  ```shell
  df -h | grep /dev/sda1
  ```