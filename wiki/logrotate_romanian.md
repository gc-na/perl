# [Linux] C Shell (csh) logrotate utilizare: Gestionarea fișierelor de jurnal

## Overview
Comanda `logrotate` este utilizată pentru a gestiona fișierele de jurnal (log) ale sistemului. Aceasta permite rotirea, comprimarea, ștergerea și trimiterea prin e-mail a fișierelor de jurnal, asigurându-se că acestea nu devin prea mari și că informațiile importante sunt păstrate într-un mod organizat.

## Usage
Sintaxa de bază a comenzii `logrotate` este următoarea:

```bash
logrotate [opțiuni] [argumente]
```

## Common Options
- `-f`: Forțează rotirea fișierelor de jurnal, indiferent de configurația curentă.
- `-s`: Specifică un fișier de stare diferit pentru a urmări rotațiile anterioare.
- `-v`: Activează modul verbose, afișând informații detaliate despre procesul de rotație.
- `-d`: Rulează în modul de simulare, fără a efectua efectiv rotația.

## Common Examples
1. **Rotirea fișierelor de jurnal conform configurației implicite:**
   ```bash
   logrotate /etc/logrotate.conf
   ```

2. **Forțarea rotației fișierelor de jurnal:**
   ```bash
   logrotate -f /etc/logrotate.conf
   ```

3. **Afișarea informațiilor detaliate despre rotație:**
   ```bash
   logrotate -v /etc/logrotate.conf
   ```

4. **Utilizarea unui fișier de stare personalizat:**
   ```bash
   logrotate -s /path/to/custom/state/file /etc/logrotate.conf
   ```

## Tips
- Asigurați-vă că configurația din `/etc/logrotate.conf` este corectă pentru a evita pierderea datelor din fișierele de jurnal.
- Utilizați modul verbose (`-v`) pentru a verifica dacă rotația funcționează conform așteptărilor.
- Programați `logrotate` să ruleze periodic prin adăugarea sa în crontab pentru a menține fișierele de jurnal gestionate automat.