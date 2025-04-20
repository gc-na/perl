# [Linux] C Shell (csh) mpstat Utilizzo: Monitora le statistiche delle CPU

## Overview
Il comando `mpstat` è utilizzato per visualizzare le statistiche delle CPU in un sistema. Fornisce informazioni dettagliate sull'utilizzo della CPU, consentendo agli utenti di monitorare le prestazioni del sistema e identificare eventuali colli di bottiglia.

## Usage
La sintassi di base del comando `mpstat` è la seguente:

```csh
mpstat [options] [arguments]
```

## Common Options
- `-P ALL`: Mostra le statistiche per tutte le CPU.
- `-u`: Mostra l'utilizzo della CPU in percentuale.
- `-h`: Mostra l'output in un formato leggibile.
- `interval`: Specifica l'intervallo di tempo tra le misurazioni (in secondi).
- `count`: Numero di volte che il comando deve essere eseguito.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `mpstat`:

1. Visualizzare le statistiche della CPU per tutte le CPU:
   ```csh
   mpstat -P ALL
   ```

2. Monitorare l'utilizzo della CPU ogni 2 secondi per 5 volte:
   ```csh
   mpstat -u 2 5
   ```

3. Visualizzare le statistiche della CPU in un formato leggibile:
   ```csh
   mpstat -h
   ```

4. Mostrare le statistiche della CPU per una CPU specifica (ad esempio, CPU 0):
   ```csh
   mpstat -P 0
   ```

## Tips
- Utilizza l'opzione `-P ALL` per avere una visione completa dell'utilizzo delle CPU, specialmente in sistemi multi-core.
- Combina `mpstat` con altri strumenti di monitoraggio per ottenere un'analisi più approfondita delle prestazioni del sistema.
- Esegui `mpstat` in un terminale separato mentre esegui altre operazioni per monitorare in tempo reale l'impatto sulle prestazioni.