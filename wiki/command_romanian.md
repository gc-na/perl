# [Linux] C Shell (csh) command `echo`: Afișează text pe ecran

## Overview
Comanda `echo` este utilizată în C Shell pentru a afișa text sau variabile pe ecran. Este o comandă simplă, dar extrem de utilă, folosită frecvent pentru a verifica valori sau pentru a oferi informații utilizatorului.

## Usage
Sintaxa de bază a comenzii `echo` este următoarea:

```
echo [opțiuni] [text]
```

## Common Options
- `-n`: Nu adaugă un caracter de linie nouă la sfârșitul ieșirii.
- `-e`: Activează interpretarea secvențelor de escape (de exemplu, `\n` pentru o nouă linie).
- `-E`: Dezactivează interpretarea secvențelor de escape (comportamentul implicit).

## Common Examples
1. Afișarea unui mesaj simplu:
   ```csh
   echo "Salut, lume!"
   ```

2. Afișarea valorii unei variabile:
   ```csh
   set nume = "Ion"
   echo "Numele meu este $nume"
   ```

3. Afișarea unui mesaj fără linie nouă la final:
   ```csh
   echo -n "Acesta este un mesaj fără linie nouă."
   ```

4. Afișarea unui mesaj cu secvențe de escape:
   ```csh
   echo -e "Primul rând\nAl doilea rând"
   ```

## Tips
- Folosește `echo` pentru a verifica rapid valorile variabilelor în scripturi.
- Când folosești secvențe de escape, asigură-te că opțiunea `-e` este activată pentru a obține rezultatul dorit.
- Evită utilizarea `echo` pentru a afișa informații sensibile, deoarece ieșirea poate fi vizibilă în terminal.