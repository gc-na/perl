# [Linux] C Shell (csh) cmp utilizare: Compararea fișierelor binare

## Overview
Comanda `cmp` este utilizată pentru a compara două fișiere binare sau textuale. Aceasta determină dacă fișierele sunt identice și, în cazul în care nu sunt, indică prima poziție la care diferă.

## Usage
Sintaxa de bază a comenzii `cmp` este următoarea:

```csh
cmp [opțiuni] [fișiere]
```

## Common Options
Iată câteva opțiuni comune pentru comanda `cmp`:

- `-l`: Afișează toate byte-urile diferite între cele două fișiere.
- `-s`: Nu afișează nimic, doar returnează un cod de ieșire care indică dacă fișierele sunt identice sau nu.
- `-i`: Specifică o valoare de offset pentru a începe comparația de la un anumit byte.

## Common Examples

1. Compararea a două fișiere:
   ```csh
   cmp fisier1.txt fisier2.txt
   ```

2. Compararea a două fișiere fără a afișa ieșirea:
   ```csh
   cmp -s fisier1.txt fisier2.txt
   ```

3. Afișarea pozițiilor byte-urilor diferite:
   ```csh
   cmp -l fisier1.bin fisier2.bin
   ```

4. Compararea a două fișiere începând de la un anumit byte:
   ```csh
   cmp -i 10 fisier1.txt fisier2.txt
   ```

## Tips
- Folosește opțiunea `-s` pentru a verifica rapid dacă fișierele sunt identice fără a genera ieșiri inutile.
- Când compari fișiere mari, opțiunea `-l` poate fi foarte utilă pentru a identifica rapid diferențele.
- Asigură-te că specifici corect calea fișierelor pentru a evita erorile de comparație.