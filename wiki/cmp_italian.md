# [Linux] C Shell (csh) cmp Uso: Confronta file byte per byte

## Overview
Il comando `cmp` in C Shell (csh) viene utilizzato per confrontare due file byte per byte. Se i file sono identici, `cmp` non produce alcun output; in caso contrario, indica la posizione del primo byte differente.

## Usage
La sintassi di base del comando è la seguente:

```csh
cmp [options] [file1] [file2]
```

## Common Options
- `-l`: Elenca i byte differenti in formato numerico.
- `-s`: Non produce output, ma restituisce un codice di uscita che indica se i file sono identici o meno.
- `-i OFFSET`: Inizia il confronto a partire dall'offset specificato.
- `-n N`: Confronta solo i primi N byte dei file.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `cmp`:

1. Confrontare due file e visualizzare le differenze:
   ```csh
   cmp file1.txt file2.txt
   ```

2. Confrontare due file senza output, solo il codice di uscita:
   ```csh
   cmp -s file1.txt file2.txt
   ```

3. Elencare i byte differenti tra due file:
   ```csh
   cmp -l file1.txt file2.txt
   ```

4. Confrontare solo i primi 100 byte di due file:
   ```csh
   cmp -n 100 file1.txt file2.txt
   ```

## Tips
- Utilizza l'opzione `-s` se desideri solo sapere se i file sono identici senza visualizzare le differenze.
- Quando lavori con file di grandi dimensioni, considera di usare l'opzione `-n` per limitare il confronto a una parte specifica del file.
- Ricorda che `cmp` è sensibile alle differenze di maiuscole e minuscole, quindi fai attenzione quando confronti nomi di file.