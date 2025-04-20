# [Linux] C Shell (csh) wget Utilizzo: Scarica file da URL

## Overview
Il comando `wget` è uno strumento da riga di comando utilizzato per scaricare file da internet. Supporta vari protocolli, tra cui HTTP, HTTPS e FTP, ed è particolarmente utile per scaricare file in modo ricorsivo o per riprendere download interrotti.

## Usage
La sintassi di base del comando `wget` è la seguente:

```csh
wget [opzioni] [argomenti]
```

## Common Options
- `-r`: Scarica in modo ricorsivo.
- `-c`: Riprende un download interrotto.
- `-P [directory]`: Specifica la directory di destinazione per i file scaricati.
- `--limit-rate=[velocità]`: Limita la velocità di download.
- `-q`: Esegue il download in modalità silenziosa, senza output.

## Common Examples
Ecco alcuni esempi pratici di utilizzo del comando `wget`:

1. Scaricare un file da un URL specifico:
   ```csh
   wget https://example.com/file.zip
   ```

2. Scaricare un file e salvarlo in una directory specifica:
   ```csh
   wget -P /path/to/directory https://example.com/file.zip
   ```

3. Riprendere un download interrotto:
   ```csh
   wget -c https://example.com/file.zip
   ```

4. Scaricare un intero sito web in modo ricorsivo:
   ```csh
   wget -r https://example.com
   ```

5. Limitare la velocità di download a 200 KB/s:
   ```csh
   wget --limit-rate=200k https://example.com/file.zip
   ```

## Tips
- Utilizza l'opzione `-q` per evitare output eccessivo durante il download di file di grandi dimensioni.
- Se scarichi file da un sito web, verifica sempre i termini di servizio per assicurarti di non violare alcuna regola.
- Puoi utilizzare `wget` in uno script per automatizzare il download di file regolarmente.