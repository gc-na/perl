# [Linux] C Shell (csh) strace utilizzo: Strumento per il tracciamento delle chiamate di sistema

## Overview
Il comando `strace` è uno strumento potente utilizzato per monitorare e diagnosticare le chiamate di sistema effettuate da un programma in esecuzione. Consente di vedere quali file vengono aperti, quali segnali vengono ricevuti e quali errori si verificano, fornendo così informazioni preziose per il debug delle applicazioni.

## Usage
La sintassi di base del comando `strace` è la seguente:

```csh
strace [opzioni] [argomenti]
```

## Common Options
Ecco alcune opzioni comuni per `strace` con brevi spiegazioni:

- `-c`: Riassume le statistiche delle chiamate di sistema.
- `-e`: Filtra le chiamate di sistema da tracciare (ad esempio, `-e trace=open` per tracciare solo le chiamate di apertura di file).
- `-o file`: Scrive l'output in un file specificato invece di stamparlo sul terminale.
- `-p PID`: Attacca un processo esistente identificato dal PID (Process ID).
- `-f`: Segue i processi figli creati da un processo tracciato.

## Common Examples
Ecco alcuni esempi pratici di utilizzo di `strace`:

1. Tracciare un comando semplice:
   ```csh
   strace ls
   ```

2. Scrivere l'output in un file:
   ```csh
   strace -o output.txt ls
   ```

3. Tracciare solo le chiamate di apertura di file:
   ```csh
   strace -e trace=open ls
   ```

4. Riassumere le statistiche delle chiamate di sistema:
   ```csh
   strace -c ls
   ```

5. Attaccare un processo esistente:
   ```csh
   strace -p 1234
   ```

## Tips
- Utilizza l'opzione `-o` per salvare l'output in un file, facilitando l'analisi successiva.
- Filtra le chiamate di sistema con `-e` per concentrarti su ciò che è più rilevante per il tuo debug.
- Ricorda che l'uso di `strace` può rallentare l'esecuzione del programma tracciato, quindi è meglio usarlo in ambienti di sviluppo o test.