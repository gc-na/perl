# [Linux] C Shell (csh) du uso: Calcola l'uso del disco

## Overview
Il comando `du` (disk usage) è utilizzato per stimare e riportare l'uso dello spazio su disco di file e directory. È uno strumento utile per monitorare quanto spazio occupano i file sul tuo sistema.

## Usage
La sintassi di base del comando è la seguente:

```csh
du [options] [arguments]
```

## Common Options
Ecco alcune opzioni comuni per il comando `du`:

- `-h`: Mostra le dimensioni in un formato leggibile dall'uomo (ad esempio, KB, MB).
- `-s`: Riporta solo il totale per ogni argomento, senza elencare le dimensioni delle sottodirectory.
- `-a`: Include i file oltre alle directory nel report.
- `-c`: Fornisce un totale cumulativo alla fine dell'output.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `du`:

1. **Visualizzare l'uso del disco di una directory**:
   ```csh
   du /path/to/directory
   ```

2. **Visualizzare l'uso del disco in formato leggibile**:
   ```csh
   du -h /path/to/directory
   ```

3. **Ottenere solo il totale per una directory**:
   ```csh
   du -sh /path/to/directory
   ```

4. **Elencare l'uso del disco di tutti i file e le directory**:
   ```csh
   du -a /path/to/directory
   ```

5. **Ottenere un totale cumulativo**:
   ```csh
   du -ch /path/to/directory
   ```

## Tips
- Utilizza l'opzione `-h` per rendere l'output più comprensibile, specialmente quando lavori con directory di grandi dimensioni.
- Combina `du` con altri comandi come `sort` per ordinare l'output in base all'uso del disco.
- Controlla regolarmente l'uso del disco per identificare file o directory che occupano spazio eccessivo, aiutandoti a mantenere il tuo sistema in ordine.