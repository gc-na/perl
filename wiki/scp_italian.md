# [Linux] C Shell (csh) scp utilizzo: Copia file in modo sicuro tra host

## Overview
Il comando `scp` (secure copy) è utilizzato per copiare file e directory in modo sicuro tra host su una rete. Utilizza il protocollo SSH per garantire la sicurezza durante il trasferimento dei dati.

## Usage
La sintassi di base del comando `scp` è la seguente:

```bash
scp [opzioni] [origine] [destinazione]
```

## Common Options
- `-r`: Copia ricorsivamente le directory.
- `-P`: Specifica la porta SSH da utilizzare (nota che è una maiuscola).
- `-i`: Specifica il file della chiave privata da utilizzare per l'autenticazione.
- `-v`: Abilita la modalità verbosa per il debug.

## Common Examples
Ecco alcuni esempi pratici di utilizzo del comando `scp`:

1. Copiare un file locale su un host remoto:
   ```bash
   scp file.txt utente@host_remoto:/percorso/destinazione/
   ```

2. Copiare un file da un host remoto a una macchina locale:
   ```bash
   scp utente@host_remoto:/percorso/file.txt /percorso/destinazione/
   ```

3. Copiare una directory in modo ricorsivo su un host remoto:
   ```bash
   scp -r /percorso/directory utente@host_remoto:/percorso/destinazione/
   ```

4. Copiare un file utilizzando una porta SSH specifica:
   ```bash
   scp -P 2222 file.txt utente@host_remoto:/percorso/destinazione/
   ```

## Tips
- Assicurati di avere i permessi necessari per accedere ai file e alle directory sia sulla macchina locale che su quella remota.
- Utilizza l'opzione `-v` per ottenere informazioni dettagliate sul processo di copia, utile per il debug.
- Considera di utilizzare chiavi SSH per un accesso più sicuro e senza password.