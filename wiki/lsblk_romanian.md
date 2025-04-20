# [Linux] C Shell (csh) lsblk utilizare: Afișează informații despre dispozitivele de bloc

## Overview
Comanda `lsblk` este utilizată pentru a lista informațiile despre dispozitivele de bloc disponibile pe sistem. Aceasta oferă o vizualizare clară a structurilor de stocare, cum ar fi hard disk-urile, SSD-urile și partițiile, inclusiv dimensiunile și punctele de montare.

## Usage
Sintaxa de bază a comenzii `lsblk` este următoarea:

```bash
lsblk [options] [arguments]
```

## Common Options
- `-a`, `--all`: Afișează toate dispozitivele, inclusiv cele care nu sunt montate.
- `-f`, `--fs`: Afișează informații despre sistemul de fișiere al dispozitivelor.
- `-l`, `--list`: Afișează rezultatele într-un format de listă, nu într-un format de arbore.
- `-o`, `--output`: Specifică coloanele care trebuie afișate.
- `-p`, `--paths`: Afișează căile complete ale dispozitivelor.

## Common Examples
1. **Listarea dispozitivelor de bloc**:
   ```bash
   lsblk
   ```

2. **Listarea tuturor dispozitivelor, inclusiv cele neutilizate**:
   ```bash
   lsblk -a
   ```

3. **Afișarea informațiilor despre sistemul de fișiere**:
   ```bash
   lsblk -f
   ```

4. **Afișarea rezultatelor într-un format de listă**:
   ```bash
   lsblk -l
   ```

5. **Afișarea unor coloane specifice**:
   ```bash
   lsblk -o NAME,SIZE,TYPE,MOUNTPOINT
   ```

## Tips
- Folosește opțiunea `-f` pentru a verifica rapid tipul sistemului de fișiere al fiecărui dispozitiv.
- Comanda `lsblk` poate fi combinată cu alte comenzi, cum ar fi `grep`, pentru a filtra rezultatele.
- Verifică periodic dispozitivele de bloc pentru a te asigura că toate sunt montate corect și funcționează așa cum trebuie.