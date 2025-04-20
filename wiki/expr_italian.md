# [Linux] C Shell (csh) expr Utilizzo: Valutazione di espressioni

## Overview
Il comando `expr` in C Shell (csh) viene utilizzato per valutare espressioni e calcolare valori. È utile per eseguire operazioni aritmetiche, confronti e manipolazioni di stringhe.

## Usage
La sintassi di base del comando è la seguente:

```csh
expr [options] [arguments]
```

## Common Options
- `+` : Somma due numeri.
- `-` : Sottrae il secondo numero dal primo.
- `*` : Moltiplica due numeri.
- `/` : Divide il primo numero per il secondo.
- `%` : Restituisce il resto della divisione.
- `=` : Confronta se due valori sono uguali.
- `!=` : Confronta se due valori non sono uguali.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `expr`:

### Esempio 1: Somma di due numeri
```csh
expr 5 + 3
```
Output: `8`

### Esempio 2: Sottrazione di due numeri
```csh
expr 10 - 4
```
Output: `6`

### Esempio 3: Moltiplicazione di due numeri
```csh
expr 7 \* 6
```
Output: `42`

### Esempio 4: Divisione di due numeri
```csh
expr 20 / 4
```
Output: `5`

### Esempio 5: Confronto di due valori
```csh
expr 5 = 5
```
Output: `1` (vero)

### Esempio 6: Controllo di disuguaglianza
```csh
expr 5 != 3
```
Output: `1` (vero)

## Tips
- Ricorda di usare il carattere di escape `\` per l'operatore di moltiplicazione `*`, altrimenti verrà interpretato come un carattere jolly.
- Usa le parentesi per raggruppare le espressioni e controllare l'ordine delle operazioni.
- `expr` restituisce `0` per falso e `1` per vero quando si utilizzano le operazioni di confronto.