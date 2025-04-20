# [Linux] C Shell (csh) printf utilizare: Afișează formatat text

## Overview
Comanda `printf` în C Shell (csh) este utilizată pentru a afișa text formatat pe ecran. Aceasta permite utilizatorilor să controleze modul în care informațiile sunt prezentate, inclusiv formatarea numerelor, a stringurilor și a altor tipuri de date.

## Usage
Sintaxa de bază a comenzii `printf` este următoarea:

```csh
printf [opțiuni] [argumente]
```

## Common Options
- `%s`: Afișează un string.
- `%d`: Afișează un număr întreg.
- `%f`: Afișează un număr în format zecimal.
- `\n`: Adaugă o linie nouă.
- `\t`: Adaugă un tab.

## Common Examples
1. Afișarea unui string:
   ```csh
   printf "Salut, lume!\n"
   ```

2. Afișarea unui număr întreg:
   ```csh
   printf "Numărul este: %d\n" 42
   ```

3. Afișarea unui număr în format zecimal:
   ```csh
   printf "Valoarea este: %.2f\n" 3.14159
   ```

4. Afișarea mai multor argumente:
   ```csh
   printf "Numele: %s, Vârsta: %d\n" "Ion" 30
   ```

5. Utilizarea tab-urilor și a liniilor noi:
   ```csh
   printf "Coloana 1\tColoana 2\nValoare 1\tValoare 2\n"
   ```

## Tips
- Folosește `%s` pentru a formata stringuri și `%d` pentru numere întregi pentru a evita erorile de tip.
- Verifică întotdeauna formatul specificat în `printf` pentru a te asigura că se potrivește cu tipul de date pe care îl afișezi.
- Poți combina mai multe formate într-o singură comandă pentru a crea ieșiri complexe.