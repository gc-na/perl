# [Linux] C Shell (csh) chage <Utilizare echivalentă>: gestionarea expirării parolelor utilizatorilor

## Overview
Comanda `chage` este utilizată pentru a modifica informațiile de expirare a parolelor utilizatorilor în sistemele Unix/Linux. Aceasta permite administratorilor să configureze politici de securitate legate de parole, cum ar fi durata de valabilitate a parolei și notificările de expirare.

## Usage
Sintaxa de bază a comenzii `chage` este următoarea:

```bash
chage [opțiuni] [argumente]
```

## Common Options
- `-l, --list`: Afișează informațiile de expirare a parolei pentru un utilizator specificat.
- `-m, --mindays`: Setează numărul minim de zile între schimbările de parolă.
- `-M, --maxdays`: Setează numărul maxim de zile până la expirarea parolei.
- `-I, --inactive`: Setează numărul de zile după expirarea parolei în care contul rămâne activ.
- `-E, --expire`: Setează data de expirare a contului utilizatorului.

## Common Examples
1. **Afișarea informațiilor de expirare a parolei pentru un utilizator:**
   ```bash
   chage -l username
   ```

2. **Setarea numărului maxim de zile pentru expirarea parolei:**
   ```bash
   chage -M 90 username
   ```

3. **Setarea numărului minim de zile între schimbările de parolă:**
   ```bash
   chage -m 7 username
   ```

4. **Activarea unei parole inactive după expirare:**
   ```bash
   chage -I 30 username
   ```

5. **Setarea datei de expirare a contului utilizatorului:**
   ```bash
   chage -E 2023-12-31 username
   ```

## Tips
- Asigurați-vă că verificați periodic setările de expirare a parolelor pentru a menține securitatea sistemului.
- Utilizați opțiunea `-l` pentru a verifica informațiile curente înainte de a face modificări.
- Documentați schimbările efectuate pentru a avea un istoric al politicilor de securitate implementate.