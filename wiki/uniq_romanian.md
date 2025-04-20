# [Linux] C Shell (csh) uniq Utilizare: Elimină liniile duplicate dintr-un fișier

## Overview
Comanda `uniq` este utilizată pentru a elimina liniile duplicate dintr-un fișier sau dintr-o ieșire a unei comenzi. Aceasta este utilă în special atunci când se lucrează cu date care conțin repetări, permițându-vă să obțineți o listă curată și concisă.

## Usage
Sintaxa de bază a comenzii `uniq` este următoarea:

```csh
uniq [opțiuni] [argumente]
```

## Common Options
- `-c`: Numără liniile duplicate și le afișează împreună cu numărul de apariții.
- `-d`: Afișează doar liniile care sunt duplicate.
- `-u`: Afișează doar liniile unice, care nu sunt duplicate.
- `-i`: Ignoră diferențele dintre literele mari și mici.

## Common Examples
1. **Eliminarea liniilor duplicate dintr-un fișier:**
   ```csh
   uniq fisier.txt
   ```

2. **Numărarea aparițiilor fiecărei linii:**
   ```csh
   uniq -c fisier.txt
   ```

3. **Afișarea doar a liniilor duplicate:**
   ```csh
   uniq -d fisier.txt
   ```

4. **Afișarea doar a liniilor unice:**
   ```csh
   uniq -u fisier.txt
   ```

5. **Ignorarea diferențelor de caz:**
   ```csh
   uniq -i fisier.txt
   ```

## Tips
- Asigurați-vă că fișierul de intrare este sortat înainte de a utiliza `uniq`, deoarece aceasta funcționează cel mai bine pe datele sortate.
- Puteți combina `uniq` cu comanda `sort` pentru a elimina duplicatele dintr-o listă nesortată:
  ```csh
  sort fisier.txt | uniq
  ```
- Folosiți opțiunea `-c` pentru a obține un raport despre frecvența liniilor, ceea ce poate fi util în analiza datelor.