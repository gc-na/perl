# [Linux] C Shell (csh) comm: confronta file riga per riga

## Overview
Il comando `comm` è utilizzato per confrontare due file di testo riga per riga. Esso produce un output che mostra le righe uniche di ciascun file e le righe comuni. Questo è utile per analizzare differenze e somiglianze tra file.

## Usage
La sintassi di base del comando è la seguente:

```csh
comm [options] [file1] [file2]
```

## Common Options
- `-1`: Sopprime le righe uniche del primo file.
- `-2`: Sopprime le righe uniche del secondo file.
- `-3`: Sopprime le righe comuni a entrambi i file.
- `-i`: Ignora la distinzione tra maiuscole e minuscole.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `comm`:

1. **Confrontare due file e visualizzare tutte le righe:**
   ```csh
   comm file1.txt file2.txt
   ```

2. **Visualizzare solo le righe comuni:**
   ```csh
   comm -12 file1.txt file2.txt
   ```

3. **Visualizzare solo le righe uniche del primo file:**
   ```csh
   comm -13 file1.txt file2.txt
   ```

4. **Visualizzare solo le righe uniche del secondo file:**
   ```csh
   comm -23 file1.txt file2.txt
   ```

5. **Confrontare due file ignorando la distinzione tra maiuscole e minuscole:**
   ```csh
   comm -i file1.txt file2.txt
   ```

## Tips
- Assicurati che i file siano ordinati prima di utilizzare `comm`, poiché il comando funziona correttamente solo su file ordinati.
- Puoi combinare più opzioni per personalizzare l'output secondo le tue esigenze.
- Utilizza `sort` per ordinare i file prima di confrontarli, se necessario:
  ```csh
  sort file1.txt > sorted_file1.txt
  sort file2.txt > sorted_file2.txt
  comm sorted_file1.txt sorted_file2.txt
  ```