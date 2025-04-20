# [Linux] C Shell (csh) users utilizzo: visualizzare gli utenti connessi

## Overview
Il comando `users` in C Shell (csh) è utilizzato per visualizzare gli utenti attualmente connessi al sistema. Mostra semplicemente i nomi degli utenti in sessione, rendendo facile identificare chi è attivo.

## Usage
La sintassi di base del comando `users` è la seguente:

```csh
users [options] [arguments]
```

## Common Options
- `-n`: Mostra solo il numero di utenti connessi.
- `-r`: Mostra solo gli utenti che hanno una sessione attiva.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `users`:

1. Visualizzare gli utenti attualmente connessi:
   ```csh
   users
   ```

2. Visualizzare solo il numero di utenti connessi:
   ```csh
   users -n
   ```

3. Visualizzare solo gli utenti con sessioni attive:
   ```csh
   users -r
   ```

## Tips
- Utilizza il comando `who` per ottenere informazioni più dettagliate sugli utenti connessi, come l'orario di accesso e il terminale utilizzato.
- Se desideri monitorare gli accessi in tempo reale, considera di combinare `users` con altri comandi come `watch`.
- Ricorda che il comando `users` mostra solo gli utenti attivi nella sessione corrente e non fornisce informazioni storiche.