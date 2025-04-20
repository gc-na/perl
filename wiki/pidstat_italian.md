# [Linux] C Shell (csh) pidstat: Monitora le statistiche dei processi

## Overview
Il comando `pidstat` è uno strumento utile per monitorare le statistiche di utilizzo delle risorse dei processi in esecuzione su un sistema. Fornisce informazioni dettagliate su CPU, memoria e altre metriche di performance per ogni processo, permettendo agli utenti di analizzare il comportamento dei processi in tempo reale.

## Usage
La sintassi di base del comando `pidstat` è la seguente:

```bash
pidstat [options] [arguments]
```

## Common Options
- `-h`: Mostra l'intestazione delle colonne in modo più leggibile.
- `-r`: Visualizza l'utilizzo della memoria.
- `-u`: Mostra l'utilizzo della CPU.
- `-p <pid>`: Specifica il PID del processo da monitorare.
- `-t`: Mostra le statistiche per i thread.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `pidstat`:

1. **Monitorare l'utilizzo della CPU di tutti i processi**:
   ```bash
   pidstat -u 1
   ```
   Questo comando mostra l'utilizzo della CPU per tutti i processi ogni secondo.

2. **Monitorare l'utilizzo della memoria per un processo specifico**:
   ```bash
   pidstat -r -p 1234 1
   ```
   Sostituisci `1234` con il PID del processo che desideri monitorare. Questo comando mostra l'utilizzo della memoria ogni secondo.

3. **Visualizzare le statistiche per i thread di un processo**:
   ```bash
   pidstat -t -p 5678 1
   ```
   Qui, `5678` è il PID del processo di cui vuoi vedere le statistiche dei thread.

4. **Mostrare le statistiche in un formato leggibile**:
   ```bash
   pidstat -h -u 1
   ```
   Questo comando mostra le statistiche di utilizzo della CPU con intestazioni più chiare.

## Tips
- Utilizza l'opzione `-h` per migliorare la leggibilità delle intestazioni delle colonne.
- Esegui `pidstat` in combinazione con altri strumenti di monitoraggio per avere una visione più completa delle prestazioni del sistema.
- Considera di salvare l'output in un file per analisi successive utilizzando la redirezione, ad esempio: `pidstat -u 1 > output.txt`.