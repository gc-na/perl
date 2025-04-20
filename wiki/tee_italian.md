# [Linux] C Shell (csh) tee utilizzo: Duplica l'output in più file

## Overview
Il comando `tee` in C Shell (csh) è utilizzato per leggere dall'input standard e scrivere sia sull'output standard che in uno o più file. Questo comando è particolarmente utile quando si desidera visualizzare l'output di un comando mentre lo si salva contemporaneamente in un file.

## Usage
La sintassi di base del comando `tee` è la seguente:

```
tee [options] [arguments]
```

## Common Options
- `-a`: Aggiunge l'output al file esistente invece di sovrascriverlo.
- `-i`: Ignora i segnali di interruzione.
- `-p`: Scrive l'output in più file.

## Common Examples
Ecco alcuni esempi pratici di utilizzo del comando `tee`:

1. **Scrivere l'output di un comando in un file:**
   ```csh
   ls -l | tee file.txt
   ```

2. **Aggiungere l'output a un file esistente:**
   ```csh
   echo "Nuova riga" | tee -a file.txt
   ```

3. **Scrivere l'output in più file:**
   ```csh
   echo "Ciao Mondo" | tee file1.txt file2.txt
   ```

4. **Ignorare i segnali di interruzione:**
   ```csh
   cat file.txt | tee -i output.txt
   ```

## Tips
- Utilizza l'opzione `-a` se desideri mantenere il contenuto esistente di un file e aggiungere nuove informazioni.
- Combinare `tee` con altri comandi può essere molto utile per il monitoraggio e la registrazione dell'output.
- Ricorda che `tee` scrive l'output in tempo reale, quindi puoi vedere immediatamente i risultati mentre vengono salvati.