# [Linux] C Shell (csh) mkdir utilizare: Crearea de directoare

## Overview
Comanda `mkdir` este utilizată pentru a crea directoare noi în sistemul de fișiere. Aceasta permite utilizatorilor să organizeze fișierele și subdirectoarele într-o structură ierarhică.

## Usage
Sintaxa de bază a comenzii `mkdir` este următoarea:

```csh
mkdir [opțiuni] [argumente]
```

## Common Options
Iată câteva opțiuni comune pentru `mkdir`:

- `-p`: Creează directoare părinte, dacă acestea nu există deja.
- `-m`: Setează permisiunile pentru noul director, specificând un mod numeric.
- `-v`: Afișează un mesaj pentru fiecare director creat.

## Common Examples
Iată câteva exemple practice de utilizare a comenzii `mkdir`:

1. Crearea unui singur director:
   ```csh
   mkdir nou_director
   ```

2. Crearea mai multor directoare simultan:
   ```csh
   mkdir director1 director2 director3
   ```

3. Crearea unui director părinte și a unui subdirector:
   ```csh
   mkdir -p parinte/subdirector
   ```

4. Crearea unui director cu permisiuni specifice:
   ```csh
   mkdir -m 755 director_permisiuni
   ```

5. Crearea unui director și afișarea unui mesaj:
   ```csh
   mkdir -v director_afisat
   ```

## Tips
- Folosiți opțiunea `-p` pentru a evita erorile atunci când creați un director într-o structură de directoare complexă.
- Verificați permisiunile directorului creat folosind comanda `ls -l` pentru a vă asigura că sunt setate corect.
- Utilizați `mkdir` în scripturi pentru a automatiza procesul de organizare a fișierelor.