# [Linux] C Shell (csh) at: Pianificazione di comandi

## Overview
Il comando `at` in C Shell (csh) viene utilizzato per pianificare l'esecuzione di comandi o script a un orario specifico in futuro. È utile per automatizzare attività che devono essere eseguite in un momento preciso.

## Usage
La sintassi di base del comando `at` è la seguente:

```
at [opzioni] [argomenti]
```

## Common Options
- `-f` : Specifica un file contenente i comandi da eseguire.
- `-m` : Invia un'email all'utente anche se non ci sono output.
- `-q` : Specifica una coda di lavoro.
- `-l` : Elenca i lavori pianificati.
- `-d` : Elimina un lavoro pianificato.

## Common Examples
Ecco alcuni esempi pratici di utilizzo del comando `at`:

1. Pianificare l'esecuzione di un comando per le 14:00:

   ```csh
   echo "echo 'Ciao, mondo!'" | at 14:00
   ```

2. Pianificare un comando per domani alle 9:30:

   ```csh
   echo "backup.sh" | at 9:30 tomorrow
   ```

3. Pianificare l'esecuzione di uno script da un file:

   ```csh
   at -f /path/to/script.sh 15:00
   ```

4. Elencare i lavori pianificati:

   ```csh
   at -l
   ```

5. Eliminare un lavoro pianificato (supponendo che l'ID del lavoro sia 5):

   ```csh
   at -d 5
   ```

## Tips
- Assicurati che il demone `atd` sia in esecuzione per poter utilizzare il comando `at`.
- Utilizza l'opzione `-m` se desideri ricevere una notifica via email dopo l'esecuzione del comando.
- Controlla frequentemente i lavori pianificati con `at -l` per tenere traccia delle tue attività programmate.