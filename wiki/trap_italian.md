# [Linux] C Shell (csh) trap Utilizzo: Gestire i segnali nel terminale

## Overview
Il comando `trap` in C Shell (csh) viene utilizzato per gestire i segnali e le interruzioni nel terminale. Permette di specificare comandi da eseguire quando si ricevono determinati segnali, facilitando la gestione delle situazioni in cui uno script potrebbe essere interrotto o terminato in modo imprevisto.

## Usage
La sintassi di base del comando `trap` è la seguente:

```csh
trap [comando] [segnale]
```

## Common Options
Ecco alcune opzioni comuni per il comando `trap`:

- `SIGINT`: Interruzione (solitamente generata premendo Ctrl+C).
- `SIGTERM`: Richiesta di terminazione.
- `EXIT`: Eseguito quando lo script termina, indipendentemente dal motivo.

## Common Examples

### Esempio 1: Gestire l'interruzione
Per eseguire un comando specifico quando si riceve un segnale di interruzione (SIGINT):

```csh
trap 'echo "Interruzione ricevuta!"' SIGINT
```

### Esempio 2: Pulizia alla chiusura
Per eseguire un comando di pulizia quando lo script termina:

```csh
trap 'rm -f /tmp/tempfile' EXIT
```

### Esempio 3: Gestire più segnali
Per gestire più segnali con comandi diversi:

```csh
trap 'echo "Interruzione!"' SIGINT
trap 'echo "Terminazione!"' SIGTERM
```

## Tips
- Utilizza `trap` per garantire che le risorse vengano sempre liberate, anche in caso di interruzioni.
- Testa i tuoi script con `trap` in un ambiente sicuro per assicurarti che i comandi vengano eseguiti come previsto.
- Ricorda che i segnali possono essere inviati anche da altri processi, quindi considera l'impatto delle tue azioni.