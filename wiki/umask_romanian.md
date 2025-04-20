# [Linux] C Shell (csh) umask utilizare: Setează permisiunile implicite pentru fișiere

## Overview
Comanda `umask` în C Shell (csh) este utilizată pentru a stabili permisiunile implicite pentru fișierele și directoarele create de utilizatori. Aceasta definește un "mask" care determină ce permisiuni vor fi eliminate din permisiunile implicite ale fișierelor și directoarelor.

## Usage
Sintaxa de bază a comenzii `umask` este următoarea:

```csh
umask [opțiuni] [argumente]
```

## Common Options
- `-S`: Afișează umask-ul în format simbolic.
- `-p`: Afișează umask-ul curent fără a-l modifica.

## Common Examples
1. **Verificarea umask-ului curent:**
   ```csh
   umask
   ```

2. **Setarea umask-ului la 022:**
   ```csh
   umask 022
   ```

3. **Afișarea umask-ului în format simbolic:**
   ```csh
   umask -S
   ```

4. **Setarea umask-ului la 007:**
   ```csh
   umask 007
   ```

## Tips
- Este recomandat să verificați umask-ul curent înainte de a crea fișiere sau directoare pentru a înțelege ce permisiuni vor fi aplicate.
- Folosiți umask-ul 027 pentru a permite accesul doar utilizatorului și grupului, protejându-vă astfel fișierele de accesul altor utilizatori.
- Modificările aduse umask-ului se aplică doar pentru sesiunea curentă; pentru a le face permanente, adăugați comanda în fișierul de configurare al shell-ului, cum ar fi `.cshrc`.