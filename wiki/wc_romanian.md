# [Linux] C Shell (csh) wc utilizare: Numără liniile, cuvintele și caracterele din fișiere

## Overview
Comanda `wc` (word count) este utilizată pentru a număra liniile, cuvintele și caracterele din fișiere. Este un instrument util pentru a obține rapid statistici despre conținutul textului.

## Usage
Sintaxa de bază a comenzii `wc` este următoarea:

```csh
wc [options] [arguments]
```

## Common Options
- `-l`: Numără doar liniile din fișier.
- `-w`: Numără doar cuvintele din fișier.
- `-c`: Numără doar caracterele din fișier.
- `-m`: Numără caracterele, inclusiv cele multibyte.
- `-L`: Afișează lungimea celei mai lungi linii.

## Common Examples
1. Numără liniile, cuvintele și caracterele dintr-un fișier:
   ```csh
   wc fisier.txt
   ```

2. Numără doar liniile dintr-un fișier:
   ```csh
   wc -l fisier.txt
   ```

3. Numără doar cuvintele dintr-un fișier:
   ```csh
   wc -w fisier.txt
   ```

4. Numără doar caracterele dintr-un fișier:
   ```csh
   wc -c fisier.txt
   ```

5. Afișează lungimea celei mai lungi linii dintr-un fișier:
   ```csh
   wc -L fisier.txt
   ```

## Tips
- Poți combina opțiunile pentru a obține mai multe statistici simultan. De exemplu, `wc -l -w fisier.txt` va număra atât liniile, cât și cuvintele.
- Folosește `wc` împreună cu alte comenzi prin pipe pentru a analiza ieșirea altor comenzi. De exemplu, `cat fisier.txt | wc -l` va număra liniile din fișierul specificat.
- Verifică documentația completă a comenzii `wc` pentru a explora opțiuni suplimentare și utilizări avansate.