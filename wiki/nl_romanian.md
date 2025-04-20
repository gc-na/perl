# [Linux] C Shell (csh) nl utilizare: numără liniile din fișiere

## Overview
Comanda `nl` este utilizată pentru a număra liniile din fișiere text. Aceasta adaugă numere de linie la începutul fiecărei linii din fișierul specificat, facilitând astfel citirea și referințele la anumite linii.

## Usage
Sintaxa de bază a comenzii `nl` este:

```csh
nl [opțiuni] [argumente]
```

## Common Options
- `-b` : Specifică modul de numerotare a liniilor (de exemplu, `-b a` pentru a număra toate liniile).
- `-f` : Specifică numărul de linii goale care nu trebuie numărate.
- `-n` : Specifică formatul numerelor (de exemplu, `-n ln` pentru a număra liniile fără zero-uri în față).
- `-w` : Specifică lățimea numerelor de linie.

## Common Examples
1. Numărarea liniilor dintr-un fișier:
   ```csh
   nl fisier.txt
   ```

2. Numărarea tuturor liniilor, inclusiv liniile goale:
   ```csh
   nl -b a fisier.txt
   ```

3. Numărarea liniilor, omis liniile goale:
   ```csh
   nl -b t fisier.txt
   ```

4. Utilizarea unui format specific pentru numerele de linie:
   ```csh
   nl -n ln -w 3 fisier.txt
   ```

## Tips
- Folosește opțiunea `-b` pentru a controla modul în care sunt numărate liniile, în funcție de nevoile tale.
- Verifică rezultatele cu `cat` pentru a compara ieșirea originală cu cea numerotată.
- Poți redirecționa ieșirea comenzii `nl` către un alt fișier folosind `>` pentru a salva rezultatul.