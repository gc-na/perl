# [Linux] C Shell (csh) journalctl utilizare: Vizualizarea jurnalelor de sistem

## Overview
Comanda `journalctl` este utilizată pentru a vizualiza jurnalele de sistem stocate de systemd. Aceasta permite utilizatorilor să acceseze și să filtreze informațiile despre evenimentele de sistem, erorile și mesajele de logare, oferind o modalitate eficientă de a diagnostica problemele.

## Usage
Sintaxa de bază a comenzii `journalctl` este următoarea:

```csh
journalctl [options] [arguments]
```

## Common Options
- `-b`: Afișează jurnalele de la ultima repornire a sistemului.
- `-f`: Urmărește în timp real jurnalele, similar cu comanda `tail -f`.
- `--since`: Afișează jurnalele începând cu o dată și oră specificate.
- `--until`: Afișează jurnalele până la o dată și oră specificate.
- `-p`: Filtrează jurnalele după prioritate (ex. `-p err` pentru erori).

## Common Examples
1. Afișarea tuturor jurnalelor:
   ```csh
   journalctl
   ```

2. Afișarea jurnalelor de la ultima repornire:
   ```csh
   journalctl -b
   ```

3. Urmărirea jurnalelor în timp real:
   ```csh
   journalctl -f
   ```

4. Afișarea jurnalelor dintr-o anumită perioadă:
   ```csh
   journalctl --since "2023-10-01" --until "2023-10-10"
   ```

5. Afișarea doar a erorilor:
   ```csh
   journalctl -p err
   ```

## Tips
- Folosiți opțiunea `-b` pentru a verifica rapid problemele apărute după o repornire.
- Combinarea opțiunilor, cum ar fi `-f` cu `-p`, poate ajuta la monitorizarea erorilor în timp real.
- Filtrarea jurnalelor pe baza timpului vă poate ajuta să identificați problemele care au apărut în intervale specifice.