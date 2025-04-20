# [Linux] C Shell (csh) mkdir Uso: Crea directory nel file system

## Overview
Il comando `mkdir` è utilizzato per creare nuove directory nel file system. È uno strumento fondamentale per organizzare file e cartelle in modo strutturato.

## Usage
La sintassi di base del comando è la seguente:

```
mkdir [opzioni] [argomenti]
```

## Common Options
- `-p`: Crea directory genitore se non esistono già.
- `-m`: Imposta i permessi della directory al valore specificato.
- `-v`: Mostra un messaggio per ogni directory creata.

## Common Examples
Ecco alcuni esempi pratici di utilizzo del comando `mkdir`:

1. Creare una singola directory:
   ```csh
   mkdir nuova_cartella
   ```

2. Creare più directory contemporaneamente:
   ```csh
   mkdir cartella1 cartella2 cartella3
   ```

3. Creare una directory con directory genitore:
   ```csh
   mkdir -p genitore/figlio
   ```

4. Creare una directory con permessi specifici:
   ```csh
   mkdir -m 755 cartella_pubblica
   ```

5. Creare una directory e visualizzare un messaggio:
   ```csh
   mkdir -v cartella_visibile
   ```

## Tips
- Utilizza l'opzione `-p` per evitare errori quando crei directory annidate.
- Controlla sempre i permessi delle directory create, specialmente se stai lavorando in ambienti condivisi.
- Usa `mkdir -v` per confermare che le directory siano state create correttamente.