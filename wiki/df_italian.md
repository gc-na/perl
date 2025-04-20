# [Linux] C Shell (csh) df Utilizzo: visualizzare lo spazio su disco disponibile

## Overview
Il comando `df` è utilizzato per visualizzare informazioni sullo spazio su disco disponibile e utilizzato sui file system montati. Fornisce un riepilogo utile per monitorare l'uso del disco e gestire lo spazio disponibile.

## Usage
La sintassi di base del comando è la seguente:

```csh
df [options] [arguments]
```

## Common Options
- `-h`: Mostra le dimensioni in un formato leggibile dall'uomo (es. KB, MB, GB).
- `-T`: Mostra il tipo di file system.
- `-a`: Include i file system con zero blocchi utilizzati.
- `-i`: Mostra l'uso degli inode invece dello spazio su disco.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `df`:

1. Visualizzare lo spazio su disco in formato leggibile:
   ```csh
   df -h
   ```

2. Mostrare il tipo di file system per ogni montaggio:
   ```csh
   df -T
   ```

3. Includere file system con zero blocchi utilizzati:
   ```csh
   df -a
   ```

4. Controllare l'uso degli inode:
   ```csh
   df -i
   ```

## Tips
- Utilizza l'opzione `-h` per ottenere un output più comprensibile, specialmente su sistemi con grandi capacità di archiviazione.
- Controlla regolarmente lo spazio su disco per evitare problemi di spazio insufficiente, soprattutto su server e sistemi di produzione.
- Puoi combinare più opzioni per ottenere informazioni più dettagliate, ad esempio `df -hT`.