# [Linux] C Shell (csh) top utilizzo: visualizza i processi in esecuzione

## Overview
Il comando `top` è uno strumento utile per monitorare i processi in esecuzione sul sistema. Mostra in tempo reale informazioni sui processi, come l'utilizzo della CPU e della memoria, consentendo agli utenti di identificare quali processi stanno consumando più risorse.

## Usage
La sintassi di base del comando `top` è la seguente:

```csh
top [options] [arguments]
```

## Common Options
Ecco alcune opzioni comuni per il comando `top`:

- `-d <seconds>`: Imposta il tempo di aggiornamento in secondi.
- `-n <number>`: Specifica il numero di aggiornamenti da eseguire prima di terminare.
- `-p <pid>`: Monitora solo il processo con l'ID specificato.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `top`:

1. Avvia `top` con l'aggiornamento ogni 5 secondi:
   ```csh
   top -d 5
   ```

2. Monitora un processo specifico con ID 1234:
   ```csh
   top -p 1234
   ```

3. Esegui `top` per 10 aggiornamenti e poi termina:
   ```csh
   top -n 10
   ```

## Tips
- Per uscire da `top`, premi `q`.
- Puoi ordinare i processi in base all'utilizzo della CPU premendo `Shift + P` o in base all'utilizzo della memoria premendo `Shift + M`.
- Usa `h` all'interno di `top` per visualizzare la guida e le scorciatoie da tastiera disponibili.