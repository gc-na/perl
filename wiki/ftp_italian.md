# [Linux] C Shell (csh) ftp utilizzo: Comando per trasferire file tra computer

## Overview
Il comando `ftp` (File Transfer Protocol) viene utilizzato per trasferire file tra un computer locale e un server remoto. Consente di caricare e scaricare file in modo semplice e diretto.

## Usage
La sintassi di base del comando `ftp` è la seguente:

```csh
ftp [options] [arguments]
```

## Common Options
- `-i`: Disabilita la modalità interattiva, utile per trasferimenti batch.
- `-n`: Non tenta di effettuare il login automaticamente.
- `-v`: Abilita la modalità verbosa, mostrando dettagli sulle operazioni in corso.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `ftp`:

1. **Connessione a un server FTP:**
   ```csh
   ftp ftp.example.com
   ```

2. **Scaricare un file dal server:**
   ```csh
   get nomefile.txt
   ```

3. **Caricare un file sul server:**
   ```csh
   put nomefile.txt
   ```

4. **Scaricare un'intera directory:**
   ```csh
   mget *.txt
   ```

5. **Caricare più file:**
   ```csh
   mput file1.txt file2.txt
   ```

## Tips
- Assicurati di avere le credenziali corrette per accedere al server FTP.
- Utilizza l'opzione `-v` per diagnosticare eventuali problemi di connessione.
- Ricorda di utilizzare la modalità binaria (`binary`) per trasferire file non testuali, come immagini o eseguibili, per evitare la corruzione dei dati.