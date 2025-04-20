# [Linux] C Shell (csh) ss utilizare: Afișează socket-uri de rețea

## Overview
Comanda `ss` este utilizată pentru a afișa informații despre socket-urile de rețea. Aceasta oferă detalii despre conexiunile active, socket-urile de ascultare și alte informații relevante despre rețea, fiind o alternativă mai rapidă și mai eficientă la comanda `netstat`.

## Usage
Sintaxa de bază a comenzii `ss` este următoarea:

```csh
ss [opțiuni] [argumente]
```

## Common Options
Iată câteva opțiuni comune pentru comanda `ss`:

- `-t`: Afișează doar conexiunile TCP.
- `-u`: Afișează doar conexiunile UDP.
- `-l`: Afișează socket-urile de ascultare.
- `-p`: Afișează informații despre procesele care utilizează socket-urile.
- `-n`: Afișează adresele și porturile în format numeric, fără a le rezolva în nume.

## Common Examples
Iată câteva exemple practice de utilizare a comenzii `ss`:

1. Afișarea tuturor conexiunilor TCP active:
   ```csh
   ss -t
   ```

2. Afișarea socket-urilor de ascultare:
   ```csh
   ss -l
   ```

3. Afișarea conexiunilor UDP:
   ```csh
   ss -u
   ```

4. Afișarea informațiilor despre procesele care utilizează socket-urile:
   ```csh
   ss -p
   ```

5. Afișarea tuturor socket-urilor, inclusiv TCP și UDP:
   ```csh
   ss -tul
   ```

## Tips
- Utilizați opțiunea `-n` pentru a obține rezultate mai rapide, evitând rezolvarea numelui gazdelor.
- Comanda `ss` poate fi combinată cu alte comenzi pentru a filtra rezultatele, cum ar fi `grep`, pentru a căuta un anumit port sau adresă IP.
- Familiarizați-vă cu opțiunile disponibile prin rularea `ss --help` pentru a explora toate funcționalitățile comenzii.