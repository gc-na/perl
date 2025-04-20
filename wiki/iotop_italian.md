# [Linux] C Shell (csh) iotop Uso: Monitorare l'uso del disco in tempo reale

## Overview
Il comando `iotop` è uno strumento utile per monitorare l'input/output delle operazioni su disco in tempo reale. Permette di visualizzare quali processi stanno utilizzando maggiormente le risorse del disco, facilitando l'identificazione di eventuali colli di bottiglia nel sistema.

## Usage
La sintassi di base del comando è la seguente:

```csh
iotop [options] [arguments]
```

## Common Options
- `-o`: Mostra solo i processi che stanno attualmente effettuando operazioni di I/O.
- `-b`: Esegue `iotop` in modalità batch, utile per l'output su file.
- `-n NUM`: Specifica il numero di aggiornamenti da visualizzare in modalità batch.
- `-d SECONDS`: Imposta l'intervallo di aggiornamento in secondi.

## Common Examples
Ecco alcuni esempi pratici di utilizzo di `iotop`:

1. **Visualizzare tutti i processi che utilizzano I/O:**
   ```csh
   iotop
   ```

2. **Mostrare solo i processi attivi:**
   ```csh
   iotop -o
   ```

3. **Eseguire `iotop` in modalità batch per 10 aggiornamenti:**
   ```csh
   iotop -b -n 10
   ```

4. **Impostare un intervallo di aggiornamento di 2 secondi:**
   ```csh
   iotop -d 2
   ```

## Tips
- Utilizza l'opzione `-o` per filtrare i processi e concentrarti solo su quelli che stanno effettivamente utilizzando il disco.
- In modalità batch, puoi reindirizzare l'output in un file per analisi successive, ad esempio: `iotop -b -n 10 > iotop_output.txt`.
- Se stai monitorando un sistema con molti processi, considera di usare `iotop` con privilegi elevati (ad esempio, come root) per ottenere informazioni complete.