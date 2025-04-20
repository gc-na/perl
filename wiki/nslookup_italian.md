# [Linux] C Shell (csh) nslookup Utilizzo: Ricerca di indirizzi IP e nomi di dominio

## Overview
Il comando `nslookup` è uno strumento utilizzato per interrogare i server DNS al fine di ottenere informazioni sui nomi di dominio e gli indirizzi IP. È utile per diagnosticare problemi di rete e per verificare la configurazione DNS.

## Usage
La sintassi di base del comando è la seguente:

```csh
nslookup [opzioni] [argomenti]
```

## Common Options
- `-type=tipo`: Specifica il tipo di record DNS da cercare (ad esempio, A, AAAA, MX).
- `-timeout=secondi`: Imposta il tempo di attesa per la risposta dal server DNS.
- `-debug`: Abilita la modalità di debug per visualizzare informazioni dettagliate sulla richiesta.

## Common Examples
Ecco alcuni esempi pratici dell'uso di `nslookup`:

1. **Cercare l'indirizzo IP di un dominio:**

   ```csh
   nslookup www.example.com
   ```

2. **Cercare un record MX per un dominio:**

   ```csh
   nslookup -type=MX example.com
   ```

3. **Specificare un server DNS diverso:**

   ```csh
   nslookup www.example.com 8.8.8.8
   ```

4. **Visualizzare informazioni dettagliate:**

   ```csh
   nslookup -debug www.example.com
   ```

## Tips
- Utilizza `nslookup` per verificare se un dominio è correttamente configurato nel DNS.
- Prova a cambiare il server DNS se non ottieni risposte soddisfacenti.
- Ricorda che i record DNS possono essere memorizzati nella cache, quindi potresti non vedere immediatamente le modifiche apportate.