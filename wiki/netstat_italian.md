# [Linux] C Shell (csh) netstat Utilizzo: visualizzare le connessioni di rete

## Overview
Il comando `netstat` è utilizzato per visualizzare le connessioni di rete attive, le tabelle di routing e le statistiche delle interfacce di rete. È uno strumento utile per monitorare le attività di rete e diagnosticare problemi di connessione.

## Usage
La sintassi di base del comando `netstat` è la seguente:

```csh
netstat [opzioni] [argomenti]
```

## Common Options
Ecco alcune opzioni comuni per il comando `netstat`:

- `-a`: Mostra tutte le connessioni e le porte in ascolto.
- `-t`: Visualizza solo le connessioni TCP.
- `-u`: Visualizza solo le connessioni UDP.
- `-n`: Mostra gli indirizzi e le porte in formato numerico, senza risolvere i nomi.
- `-r`: Mostra la tabella di routing del kernel.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `netstat`:

1. Visualizzare tutte le connessioni attive:
   ```csh
   netstat -a
   ```

2. Visualizzare solo le connessioni TCP:
   ```csh
   netstat -t
   ```

3. Visualizzare solo le connessioni UDP:
   ```csh
   netstat -u
   ```

4. Visualizzare la tabella di routing:
   ```csh
   netstat -r
   ```

5. Visualizzare le connessioni in formato numerico:
   ```csh
   netstat -n
   ```

## Tips
- Utilizza l'opzione `-n` per velocizzare l'output, specialmente su reti grandi, evitando la risoluzione dei nomi.
- Combina le opzioni per ottenere informazioni più dettagliate, ad esempio `netstat -tun` per vedere le connessioni TCP e UDP in formato numerico.
- Controlla frequentemente le connessioni di rete per identificare eventuali attività sospette o problemi di connettività.