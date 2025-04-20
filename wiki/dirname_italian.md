# [Linux] C Shell (csh) dirname Uso: Estrae il nome della directory da un percorso

## Overview
Il comando `dirname` è utilizzato per estrarre il nome della directory da un percorso di file. Questo è utile quando si desidera ottenere solo la parte della directory di un percorso completo, ignorando il nome del file.

## Usage
La sintassi di base del comando è la seguente:

```csh
dirname [opzioni] [argomenti]
```

## Common Options
- Non ci sono opzioni comuni per il comando `dirname`, poiché il suo utilizzo è piuttosto semplice e diretto.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `dirname`:

1. Estrazione della directory da un percorso completo:
   ```csh
   dirname /home/utente/documenti/file.txt
   ```
   **Output:** `/home/utente/documenti`

2. Estrazione della directory da un percorso relativo:
   ```csh
   dirname ./progetti/codice/main.c
   ```
   **Output:** `./progetti/codice`

3. Utilizzo di `dirname` in una pipeline:
   ```csh
   echo "/var/log/syslog" | dirname
   ```
   **Output:** `/var/log`

## Tips
- Utilizza `dirname` in combinazione con altri comandi per automatizzare la gestione dei file.
- Ricorda che `dirname` restituisce sempre un percorso, quindi se il percorso fornito è solo un nome di file, restituirà un punto (`.`) se non ci sono directory.
- Puoi utilizzare `dirname` in script per facilitare la manipolazione dei percorsi di file.