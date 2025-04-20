# [Linux] C Shell (csh) sqlite3 Uso: Interagire con database SQLite

## Overview
Il comando `sqlite3` è uno strumento da riga di comando utilizzato per interagire con i database SQLite. Permette di eseguire query SQL, gestire tabelle e manipolare i dati all'interno di un database SQLite.

## Usage
La sintassi di base del comando `sqlite3` è la seguente:

```csh
sqlite3 [opzioni] [argomenti]
```

## Common Options
- `-help`: Mostra un elenco di tutte le opzioni disponibili.
- `-version`: Mostra la versione di SQLite in uso.
- `-init <file>`: Esegue i comandi SQL contenuti nel file specificato all'avvio.
- `-batch`: Esegue in modalità batch, utile per script.

## Common Examples
Ecco alcuni esempi pratici di utilizzo del comando `sqlite3`:

1. **Creare un nuovo database**:
   ```csh
   sqlite3 mio_database.db
   ```

2. **Eseguire una query SQL per creare una tabella**:
   ```csh
   sqlite3 mio_database.db "CREATE TABLE utenti (id INTEGER PRIMARY KEY, nome TEXT, email TEXT);"
   ```

3. **Inserire dati nella tabella**:
   ```csh
   sqlite3 mio_database.db "INSERT INTO utenti (nome, email) VALUES ('Mario Rossi', 'mario@example.com');"
   ```

4. **Selezionare dati dalla tabella**:
   ```csh
   sqlite3 mio_database.db "SELECT * FROM utenti;"
   ```

5. **Esportare i dati in un file CSV**:
   ```csh
   sqlite3 -header -csv mio_database.db "SELECT * FROM utenti;" > utenti.csv
   ```

## Tips
- Utilizza l'opzione `-init` per caricare automaticamente script SQL all'avvio di `sqlite3`.
- Ricorda di utilizzare le virgolette per racchiudere le query SQL che contengono spazi o caratteri speciali.
- Per una migliore leggibilità, puoi utilizzare l'opzione `-header` per visualizzare i nomi delle colonne nei risultati delle query.