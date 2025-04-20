# [Linux] C Shell (csh) case: Gestione delle scelte condizionali

## Overview
Il comando `case` in C Shell (csh) è utilizzato per gestire le scelte condizionali. Permette di eseguire diverse azioni in base al valore di una variabile, facilitando la scrittura di script più complessi e interattivi.

## Usage
La sintassi di base del comando `case` è la seguente:

```
case [variabile] in
    [pattern1] ) [comandi1];;
    [pattern2] ) [comandi2];;
    ...
    * ) [comandi_predefiniti];;
esac
```

## Common Options
Il comando `case` non ha molte opzioni, ma è importante conoscere i seguenti elementi:

- `*`: rappresenta un pattern predefinito che corrisponde a qualsiasi valore non specificato nei pattern precedenti.
- `;;`: indica la fine di un blocco di comandi per un pattern specifico.

## Common Examples

### Esempio 1: Esempio di base
```csh
set var = "apple"
switch ($var)
    case "apple":
        echo "È una mela."
        breaksw
    case "banana":
        echo "È una banana."
        breaksw
    default:
        echo "Frutto sconosciuto."
endsw
```

### Esempio 2: Controllo del numero
```csh
set num = 2
switch ($num)
    case 1:
        echo "Uno"
        breaksw
    case 2:
        echo "Due"
        breaksw
    case 3:
        echo "Tre"
        breaksw
    default:
        echo "Numero non riconosciuto."
endsw
```

### Esempio 3: Esempio con più pattern
```csh
set fruit = "kiwi"
switch ($fruit)
    case "apple":
    case "banana":
        echo "Hai scelto un frutto comune."
        breaksw
    case "kiwi":
        echo "Hai scelto un kiwi."
        breaksw
    default:
        echo "Frutto sconosciuto."
endsw
```

## Tips
- Utilizza `case` per semplificare il codice quando hai molte condizioni da gestire.
- Ricorda di utilizzare `breaksw` per uscire dal blocco `switch` dopo aver eseguito i comandi per un pattern.
- Assicurati di includere un pattern predefinito (`*`) per gestire eventuali valori non previsti.