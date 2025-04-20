# [Linux] C Shell (csh) who uso: visualizza gli utenti connessi

## Overview
Il comando `who` in C Shell (csh) viene utilizzato per visualizzare gli utenti attualmente connessi al sistema. Mostra informazioni come il nome dell'utente, il terminale utilizzato, la data e l'ora di accesso.

## Usage
La sintassi di base del comando `who` è la seguente:

```csh
who [options] [arguments]
```

## Common Options
Ecco alcune opzioni comuni per il comando `who`:

- `-a`: Mostra tutte le informazioni disponibili, inclusi gli utenti disconnessi.
- `-b`: Mostra l'ora dell'ultimo riavvio del sistema.
- `-q`: Mostra solo i nomi degli utenti connessi e il conteggio totale.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `who`:

1. Visualizzare gli utenti attualmente connessi:
   ```csh
   who
   ```

2. Visualizzare tutte le informazioni disponibili sugli utenti:
   ```csh
   who -a
   ```

3. Visualizzare l'ora dell'ultimo riavvio del sistema:
   ```csh
   who -b
   ```

4. Visualizzare solo i nomi degli utenti connessi e il conteggio totale:
   ```csh
   who -q
   ```

## Tips
- Utilizza `who` regolarmente per monitorare chi è connesso al tuo sistema, specialmente in ambienti condivisi.
- Combinare `who` con altri comandi come `grep` può aiutarti a filtrare informazioni specifiche, ad esempio:
  ```csh
  who | grep nome_utente
  ```
- Ricorda che il comando `who` può fornire informazioni sensibili, quindi usalo con cautela in ambienti pubblici o condivisi.