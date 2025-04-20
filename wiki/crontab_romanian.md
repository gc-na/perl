# [Linux] C Shell (csh) crontab utilizare: Programarea sarcinilor automate

## Overview
Comanda `crontab` este utilizată pentru a programa sarcini automate care să ruleze la intervale regulate pe un sistem Unix sau Linux. Aceasta permite utilizatorilor să definească comenzi sau scripturi care să fie executate automat la ore sau date specifice.

## Usage
Sintaxa de bază a comenzii `crontab` este următoarea:

```bash
crontab [opțiuni] [argumente]
```

## Common Options
- `-e`: Editează crontabul utilizatorului curent.
- `-l`: Listează sarcinile programate în crontabul utilizatorului curent.
- `-r`: Șterge crontabul utilizatorului curent.
- `-i`: Confirmă ștergerea crontabului (folosit împreună cu `-r`).

## Common Examples
1. **Editarea crontabului**:
   ```bash
   crontab -e
   ```
   Aceasta deschide editorul de text pentru a modifica sarcinile programate.

2. **Listarea sarcinilor programate**:
   ```bash
   crontab -l
   ```
   Aceasta va afișa toate sarcinile programate pentru utilizatorul curent.

3. **Ștergerea crontabului**:
   ```bash
   crontab -r
   ```
   Aceasta va șterge toate sarcinile programate fără confirmare.

4. **Programarea unei sarcini**:
   ```bash
   * * * * * /path/to/script.sh
   ```
   Aceasta va rula scriptul `script.sh` la fiecare minut.

5. **Programarea unei sarcini zilnice la ora 2 AM**:
   ```bash
   0 2 * * * /path/to/backup.sh
   ```
   Aceasta va rula scriptul `backup.sh` în fiecare zi la ora 2:00 AM.

## Tips
- Asigurați-vă că scripturile pe care le programați au permisiuni de execuție.
- Verificați periodic sarcinile programate pentru a evita suprasarcina sistemului.
- Utilizați căi absolute pentru scripturi pentru a evita problemele de localizare a fișierelor.