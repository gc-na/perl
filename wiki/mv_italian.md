# [Linux] C Shell (csh) mv Utilizzo: Spostare o rinominare file e directory

## Overview
Il comando `mv` in C Shell (csh) viene utilizzato per spostare o rinominare file e directory. È uno strumento fondamentale per la gestione dei file nel sistema operativo.

## Usage
La sintassi di base del comando `mv` è la seguente:

```csh
mv [opzioni] [argomenti]
```

## Common Options
- `-i`: Chiede conferma prima di sovrascrivere un file esistente.
- `-u`: Sposta solo i file che sono più recenti rispetto ai file di destinazione o che non esistono.
- `-v`: Mostra i dettagli delle operazioni eseguite.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `mv`:

1. **Spostare un file in un'altra directory:**
   ```csh
   mv documento.txt /home/utente/documenti/
   ```

2. **Rinominare un file:**
   ```csh
   mv vecchio_nome.txt nuovo_nome.txt
   ```

3. **Spostare più file in una directory:**
   ```csh
   mv file1.txt file2.txt /home/utente/documenti/
   ```

4. **Spostare un file e chiedere conferma prima di sovrascrivere:**
   ```csh
   mv -i documento.txt /home/utente/documenti/
   ```

5. **Spostare solo file più recenti:**
   ```csh
   mv -u documento.txt /home/utente/documenti/
   ```

## Tips
- Utilizza l'opzione `-i` per evitare di sovrascrivere accidentalmente file importanti.
- Controlla sempre il percorso di destinazione per assicurarti che i file vengano spostati nella directory corretta.
- Usa l'opzione `-v` per avere un feedback visivo delle operazioni che stai eseguendo, specialmente quando sposti più file.