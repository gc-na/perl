# [Linux] C Shell (csh) sha256sum utilizzo: Calcolare checksum SHA-256

## Overview
Il comando `sha256sum` calcola e verifica il checksum SHA-256 di file. È utile per garantire l'integrità dei dati, confrontando il checksum di un file originale con quello di una copia.

## Usage
La sintassi di base del comando è la seguente:

```csh
sha256sum [options] [arguments]
```

## Common Options
- `-b`: Esegue il calcolo su file binari.
- `-c`: Controlla i checksum contro un file di checksum.
- `--quiet`: Non mostra il messaggio di errore per file non corrispondenti.
- `--tag`: Produce un output compatibile con il formato BSD.

## Common Examples
Ecco alcuni esempi pratici dell'uso di `sha256sum`:

1. **Calcolare il checksum di un file**:
   ```csh
   sha256sum file.txt
   ```

2. **Calcolare il checksum di più file**:
   ```csh
   sha256sum file1.txt file2.txt
   ```

3. **Salvare il checksum in un file**:
   ```csh
   sha256sum file.txt > checksum.txt
   ```

4. **Verificare i checksum da un file**:
   ```csh
   sha256sum -c checksum.txt
   ```

5. **Calcolare il checksum di un file binario**:
   ```csh
   sha256sum -b file.bin
   ```

## Tips
- Assicurati di utilizzare `sha256sum` su file di dimensioni appropriate, poiché file molto grandi possono richiedere tempo per il calcolo.
- È buona prassi generare e conservare i file di checksum in un luogo sicuro per future verifiche.
- Utilizza l'opzione `-c` per confrontare i checksum in modo efficiente, specialmente quando lavori con più file.