# [Linux] C Shell (csh) iotop utilizare: Monitorizarea utilizării I/O a proceselor

## Overview
Comanda `iotop` este un instrument util pentru monitorizarea utilizării resurselor de intrare/ieșire (I/O) ale proceselor în sistemele Linux. Aceasta oferă o interfață similară cu `top`, dar se concentrează pe activitatea de I/O, permițând utilizatorilor să observe care procese consumă cel mai mult resurse de I/O.

## Usage
Sintaxa de bază a comenzii `iotop` este următoarea:

```bash
iotop [options] [arguments]
```

## Common Options
- `-o` sau `--only`: Afișează doar procesele care efectuează activitate de I/O.
- `-b` sau `--batch`: Rulează `iotop` în modul batch, util pentru redirecționarea ieșirii către un fișier.
- `-d <sec>`: Setează intervalul de actualizare în secunde.
- `-p <pid>`: Monitorizează doar procesul specificat prin ID-ul său de proces (PID).

## Common Examples
1. **Monitorizarea activității de I/O în timp real:**
   ```bash
   iotop
   ```

2. **Afișarea doar a proceselor active:**
   ```bash
   iotop -o
   ```

3. **Rularea `iotop` în modul batch cu actualizări la fiecare 5 secunde:**
   ```bash
   iotop -b -d 5
   ```

4. **Monitorizarea unui proces specific prin PID:**
   ```bash
   iotop -p 1234
   ```

## Tips
- Utilizați opțiunea `-o` pentru a filtra rapid procesele care generează activitate de I/O, economisind timp în analiza datelor.
- Rulați `iotop` cu privilegii de administrator (de exemplu, folosind `sudo`) pentru a obține informații complete despre toate procesele.
- Combinați `iotop` cu alte comenzi de monitorizare a sistemului pentru o imagine de ansamblu mai bună asupra performanței sistemului.