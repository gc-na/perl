# [Linux] C Shell (csh) timedatectl Utilizzo: Gestire data e ora di sistema

## Overview
Il comando `timedatectl` è utilizzato per visualizzare e modificare le impostazioni di data e ora del sistema. Permette di gestire anche il fuso orario e la sincronizzazione dell'orologio di sistema.

## Usage
La sintassi di base del comando è la seguente:

```csh
timedatectl [opzioni] [argomenti]
```

## Common Options
- `status`: Mostra lo stato attuale della data e ora del sistema.
- `set-time`: Imposta la data e l'ora del sistema.
- `set-timezone`: Cambia il fuso orario del sistema.
- `set-ntp`: Abilita o disabilita la sincronizzazione automatica dell'orologio di sistema tramite NTP (Network Time Protocol).

## Common Examples
Ecco alcuni esempi pratici dell'uso di `timedatectl`:

1. **Visualizzare lo stato attuale della data e ora:**
   ```csh
   timedatectl status
   ```

2. **Impostare una data e ora specifica:**
   ```csh
   timedatectl set-time '2023-10-01 12:00:00'
   ```

3. **Cambiare il fuso orario a 'Europe/Rome':**
   ```csh
   timedatectl set-timezone Europe/Rome
   ```

4. **Abilitare la sincronizzazione NTP:**
   ```csh
   timedatectl set-ntp true
   ```

## Tips
- Assicurati di avere i permessi di amministratore per modificare le impostazioni di data e ora.
- Controlla sempre il fuso orario corretto per evitare confusione con gli orari.
- Utilizza `timedatectl list-timezones` per visualizzare un elenco di tutti i fusi orari disponibili.