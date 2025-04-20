# [Linux] C Shell (csh) sort utilizare: Sortează liniile de text

## Overview
Comanda `sort` este utilizată pentru a organiza liniile de text dintr-un fișier sau dintr-o intrare standard într-o ordine specificată, de obicei în ordine alfabetică sau numerică.

## Usage
Sintaxa de bază a comenzii `sort` este următoarea:
```
sort [opțiuni] [argumente]
```

## Common Options
- `-r`: Sortează în ordine inversă.
- `-n`: Sortează numeric, nu alfabetically.
- `-k`: Specifică o coloană sau un câmp pentru sortare.
- `-u`: Elimină duplicatele din rezultatul sortării.
- `-o`: Scrie rezultatul sortării într-un fișier specificat.

## Common Examples
1. **Sortarea unui fișier text în ordine alfabetică:**
   ```csh
   sort fisier.txt
   ```

2. **Sortarea în ordine inversă:**
   ```csh
   sort -r fisier.txt
   ```

3. **Sortarea numerică a unui fișier:**
   ```csh
   sort -n numere.txt
   ```

4. **Sortarea pe baza unei coloane specifice:**
   ```csh
   sort -k 2 fisier.txt
   ```

5. **Eliminarea liniilor duplicate și sortarea rezultatelor:**
   ```csh
   sort -u fisier.txt
   ```

6. **Scrierea rezultatelor sortării într-un nou fișier:**
   ```csh
   sort fisier.txt -o fisier_sortat.txt
   ```

## Tips
- Asigurați-vă că fișierele pe care doriți să le sortați sunt accesibile și nu sunt blocate de alte procese.
- Utilizați opțiunea `-k` pentru a sortare pe baza unor coloane specifice, ceea ce poate fi foarte util în fișierele CSV.
- Combinați opțiunile pentru a obține rezultate mai precise, de exemplu, `sort -n -r` pentru a obține o sortare numerică inversă.