# [Linux] C Shell (csh) last utilizare: Afișează ultimele sesiuni de conectare

## Overview
Comanda `last` este utilizată pentru a afișa o listă a utilizatorilor care s-au conectat la sistem, împreună cu informații despre timpul și durata sesiunilor lor. Aceasta este utilă pentru monitorizarea activității utilizatorilor și pentru a verifica cine a accesat sistemul.

## Usage
Sintaxa de bază a comenzii `last` este următoarea:

```
last [opțiuni] [argumente]
```

## Common Options
- `-n [număr]`: Afișează ultimele `număr` de sesiuni de conectare.
- `-f [fișier]`: Specifică un fișier diferit de jurnal pentru a citi informațiile despre conectare.
- `-R`: Oprește afișarea numelui gazdelor.
- `-x`: Afișează și sesiunile de shutdown și reboot.

## Common Examples
1. Afișarea tuturor sesiunilor de conectare:
   ```csh
   last
   ```

2. Afișarea ultimelor 5 sesiuni de conectare:
   ```csh
   last -n 5
   ```

3. Afișarea sesiunilor dintr-un fișier specific:
   ```csh
   last -f /var/log/wtmp.1
   ```

4. Afișarea sesiunilor fără numele gazdelor:
   ```csh
   last -R
   ```

5. Afișarea sesiunilor de shutdown și reboot:
   ```csh
   last -x
   ```

## Tips
- Folosiți opțiunea `-n` pentru a limita numărul de rezultate afișate, ceea ce poate fi util pe sisteme cu un istoric lung de sesiuni.
- Verificați periodic sesiunile de conectare pentru a identifica activități neobișnuite sau accesuri neautorizate.
- Puteți combina `last` cu comanda `grep` pentru a căuta sesiuni specifice ale unui utilizator:
  ```csh
  last | grep username
  ```