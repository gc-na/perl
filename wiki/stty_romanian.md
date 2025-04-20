# [Linux] C Shell (csh) stty utilizare: Configurează terminalul

## Overview
Comanda `stty` este utilizată pentru a modifica și a vizualiza parametrii terminalului. Aceasta permite utilizatorilor să ajusteze setările de intrare și ieșire ale terminalului, cum ar fi controlul caracterelor, comportamentul terminalului și multe altele.

## Usage
Sintaxa de bază a comenzii `stty` este următoarea:

```bash
stty [opțiuni] [argumente]
```

## Common Options
- `-a`: Afișează toate setările curente ale terminalului.
- `-g`: Afișează setările terminalului într-un format care poate fi utilizat ulterior cu `stty`.
- `erase [caracter]`: Setează caracterul de ștergere (de obicei, Backspace).
- `kill [caracter]`: Setează caracterul de ștergere a liniei (de obicei, Ctrl+U).
- `intr [caracter]`: Setează caracterul de întrerupere (de obicei, Ctrl+C).

## Common Examples
1. **Afișarea setărilor curente ale terminalului:**
   ```bash
   stty -a
   ```

2. **Setarea caracterului de ștergere la Backspace:**
   ```bash
   stty erase ^H
   ```

3. **Setarea caracterului de întrerupere la Ctrl+C:**
   ```bash
   stty intr ^C
   ```

4. **Salvarea setărilor curente pentru utilizare ulterioară:**
   ```bash
   stty -g > setari_terminal.txt
   ```

5. **Restaurarea setărilor dintr-un fișier:**
   ```bash
   stty `cat setari_terminal.txt`
   ```

## Tips
- Verificați setările terminalului înainte de a face modificări pentru a evita comportamente neașteptate.
- Utilizați opțiunea `-g` pentru a salva setările curente, astfel încât să le puteți restaura ușor mai târziu.
- Fiți atenți la caracterele speciale, asigurați-vă că le introduceți corect pentru a evita erorile de configurare.