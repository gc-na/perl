# [Linux] C Shell (csh) switch utilizzo: Cambiare tra diverse opzioni

## Overview
Il comando `switch` in C Shell (csh) è utilizzato per eseguire un'istruzione condizionale che consente di selezionare tra diverse opzioni in base al valore di una variabile. È simile a un'istruzione `case` in altri linguaggi di programmazione.

## Usage
La sintassi di base del comando `switch` è la seguente:

```csh
switch (espressione)
    case valore1:
        # comandi da eseguire se l'espressione corrisponde a valore1
        breaksw
    case valore2:
        # comandi da eseguire se l'espressione corrisponde a valore2
        breaksw
    default:
        # comandi da eseguire se nessun valore corrisponde
        breaksw
end
```

## Common Options
Il comando `switch` non ha molte opzioni, ma è importante notare i seguenti elementi:

- `case valore:`: specifica il valore da confrontare con l'espressione.
- `breaksw`: termina l'istruzione `switch` e salta al di fuori di essa.
- `default:`: definisce il blocco di codice da eseguire se nessun caso corrisponde.

## Common Examples

### Esempio 1: Utilizzo di switch per controllare un giorno della settimana
```csh
set giorno = "Lunedì"
switch ($giorno)
    case "Lunedì":
        echo "Inizio della settimana!"
        breaksw
    case "Venerdì":
        echo "Quasi fine settimana!"
        breaksw
    default:
        echo "Un giorno qualsiasi."
        breaksw
end
```

### Esempio 2: Controllo del numero
```csh
set numero = 2
switch ($numero)
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
        breaksw
end
```

### Esempio 3: Verifica del tipo di file
```csh
set tipo_file = "test.txt"
switch ($tipo_file)
    case *.txt:
        echo "È un file di testo."
        breaksw
    case *.jpg:
        echo "È un file immagine."
        breaksw
    default:
        echo "Tipo di file sconosciuto."
        breaksw
end
```

## Tips
- Assicurati di utilizzare `breaksw` per evitare che il controllo passi ai casi successivi.
- Utilizza `default` per gestire eventuali casi non previsti.
- Ricorda che l'espressione deve essere racchiusa tra parentesi tonde.