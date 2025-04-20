# [Linux] C Shell (csh) if utilizare: Evaluarea condițiilor

## Overview
Comanda `if` din C Shell (csh) este utilizată pentru a evalua condiții și a executa comenzi în funcție de rezultatul evaluării. Aceasta permite utilizatorilor să controleze fluxul de execuție al scripturilor prin verificarea unor condiții specifice.

## Usage
Sintaxa de bază a comenzii `if` este următoarea:

```
if (condiție) then
    comenzi
endif
```

## Common Options
- `then`: Indică începutul blocului de comenzi care urmează a fi executat dacă condiția este adevărată.
- `endif`: Marchează sfârșitul blocului `if`.

## Common Examples

1. **Verificarea existenței unui fișier:**
   ```csh
   if (-e "fisier.txt") then
       echo "Fișierul există."
   endif
   ```

2. **Compararea valorilor:**
   ```csh
   set a = 5
   set b = 10
   if ($a < $b) then
       echo "$a este mai mic decât $b."
   endif
   ```

3. **Verificarea unui director:**
   ```csh
   if (-d "folder") then
       echo "Folderul există."
   else
       echo "Folderul nu există."
   endif
   ```

4. **Combinații de condiții:**
   ```csh
   if (-e "fisier.txt" && -r "fisier.txt") then
       echo "Fișierul există și este citibil."
   endif
   ```

## Tips
- Asigurați-vă că folosiți paranteze corecte pentru condiții complexe.
- Utilizați `else` pentru a gestiona cazurile în care condiția nu este adevărată.
- Testați întotdeauna scripturile pentru a verifica dacă logica condițiilor funcționează așa cum este de așteptat.