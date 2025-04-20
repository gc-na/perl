# [Linux] C Shell (csh) if: Esegue comandi condizionali

## Overview
Il comando `if` nel C Shell (csh) viene utilizzato per eseguire comandi in base a condizioni specifiche. Permette di controllare se una certa condizione è vera e, in tal caso, eseguire un blocco di comandi.

## Usage
La sintassi di base del comando `if` è la seguente:

```
if (condizione) then
    comandi
endif
```

## Common Options
- `then`: Indica l'inizio del blocco di comandi da eseguire se la condizione è vera.
- `endif`: Segna la fine del blocco di comandi condizionali.

## Common Examples

### Esempio 1: Controllo di un file
Verifica se un file esiste e, in caso affermativo, stampa un messaggio.

```csh
if (-e "file.txt") then
    echo "Il file esiste."
endif
```

### Esempio 2: Controllo di una variabile
Controlla se una variabile è uguale a un certo valore.

```csh
set var = "test"
if ("$var" == "test") then
    echo "La variabile è uguale a test."
endif
```

### Esempio 3: Controllo di un numero
Verifica se un numero è maggiore di un altro.

```csh
set num = 5
if ($num > 3) then
    echo "Il numero è maggiore di 3."
endif
```

## Tips
- Assicurati di utilizzare le parentesi tonde per racchiudere la condizione.
- Ricorda di chiudere sempre il blocco `if` con `endif`.
- Puoi annidare più comandi `if` per controllare condizioni multiple.