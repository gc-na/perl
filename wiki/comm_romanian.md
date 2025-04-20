# [Linux] C Shell (csh) comm: compararea fișierelor

## Overview
Comanda `comm` este utilizată pentru a compara două fișiere sortate linie cu linie. Aceasta afișează liniile care sunt unice fie pentru primul fișier, fie pentru al doilea, precum și liniile comune între cele două fișiere.

## Usage
Sintaxa de bază a comenzii `comm` este următoarea:

```csh
comm [opțiuni] [fișier1] [fișier2]
```

## Common Options
- `-1`: Suprimă liniile unice din primul fișier.
- `-2`: Suprimă liniile unice din al doilea fișier.
- `-3`: Suprimă liniile comune între cele două fișiere.
- `-i`: Ignoră diferențele de caz (majuscule/mici) în timpul comparației.

## Common Examples
1. Compararea a două fișiere și afișarea tuturor liniilor:
   ```csh
   comm file1.txt file2.txt
   ```

2. Afișarea doar a liniilor unice din primul fișier:
   ```csh
   comm -13 file1.txt file2.txt
   ```

3. Afișarea liniilor comune între cele două fișiere:
   ```csh
   comm -12 file1.txt file2.txt
   ```

4. Compararea a două fișiere ignorând diferențele de caz:
   ```csh
   comm -i file1.txt file2.txt
   ```

## Tips
- Asigurați-vă că fișierele sunt sortate înainte de a utiliza comanda `comm`, deoarece aceasta funcționează corect doar cu fișierele sortate.
- Utilizați opțiunile `-1`, `-2` și `-3` împreună pentru a personaliza ieșirea în funcție de nevoile dvs.
- Puteți redirecționa ieșirea comenzii către un alt fișier pentru a salva rezultatele comparației, folosind `>`:
  ```csh
  comm file1.txt file2.txt > rezultat.txt
  ```