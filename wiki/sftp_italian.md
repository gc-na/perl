# [Linux] C Shell (csh) sftp utilizzo: trasferimento sicuro di file

## Overview
Il comando `sftp` (SSH File Transfer Protocol) è utilizzato per trasferire file in modo sicuro tra un client e un server. Utilizza il protocollo SSH per garantire che i dati siano criptati durante il trasferimento, rendendolo una scelta sicura per la gestione dei file su reti non sicure.

## Usage
La sintassi di base del comando `sftp` è la seguente:

```csh
sftp [opzioni] [utente@host]
```

## Common Options
Ecco alcune opzioni comuni per il comando `sftp`:

- `-o`: Specifica un'opzione da passare al client SSH.
- `-b`: Permette di eseguire comandi batch da un file.
- `-P`: Specifica la porta da utilizzare per la connessione.
- `-v`: Abilita la modalità verbose per visualizzare informazioni dettagliate sulla connessione.

## Common Examples
Ecco alcuni esempi pratici di utilizzo del comando `sftp`:

1. **Connessione a un server SFTP:**
   ```csh
   sftp user@hostname
   ```

2. **Trasferire un file dal client al server:**
   ```csh
   put localfile.txt
   ```

3. **Scaricare un file dal server al client:**
   ```csh
   get remotefile.txt
   ```

4. **Elencare i file nella directory remota:**
   ```csh
   ls
   ```

5. **Eseguire comandi batch da un file:**
   ```csh
   sftp -b batchfile.txt user@hostname
   ```

## Tips
- Assicurati di avere le autorizzazioni appropriate per accedere ai file sul server.
- Usa la modalità verbose (`-v`) per diagnosticare eventuali problemi di connessione.
- Considera di utilizzare chiavi SSH per una connessione più sicura e senza password.
- Controlla sempre la directory remota con il comando `ls` prima di trasferire file per evitare sovrascritture accidentali.