# [Linux] C Shell (csh) traceroute6 uso: Traccia il percorso dei pacchetti IPv6

## Overview
Il comando `traceroute6` è utilizzato per tracciare il percorso che i pacchetti IPv6 seguono per raggiungere un host di destinazione. Fornisce informazioni sui router intermedi e sui tempi di risposta, aiutando a diagnosticare problemi di rete.

## Usage
La sintassi di base del comando è la seguente:

```bash
traceroute6 [options] [arguments]
```

## Common Options
- `-m <max_ttl>`: Imposta il valore massimo di TTL (Time To Live) per i pacchetti.
- `-p <port>`: Specifica la porta da utilizzare per il tracciamento.
- `-q <nqueries>`: Imposta il numero di query per ogni hop.
- `-w <timeout>`: Definisce il timeout per le risposte.

## Common Examples
Ecco alcuni esempi pratici di utilizzo del comando `traceroute6`:

1. Tracciare il percorso verso un host specifico:
   ```bash
   traceroute6 google.com
   ```

2. Impostare un valore massimo di TTL di 30:
   ```bash
   traceroute6 -m 30 google.com
   ```

3. Utilizzare una porta specifica, ad esempio la porta 80:
   ```bash
   traceroute6 -p 80 google.com
   ```

4. Eseguire 5 query per ogni hop:
   ```bash
   traceroute6 -q 5 google.com
   ```

5. Impostare un timeout di 2 secondi:
   ```bash
   traceroute6 -w 2 google.com
   ```

## Tips
- Assicurati di avere i permessi necessari per eseguire `traceroute6`, poiché potrebbe richiedere privilegi elevati.
- Utilizza l'opzione `-m` per limitare il numero di hop e ottenere risultati più rapidi.
- Se stai diagnosticando problemi di rete, confronta i risultati di `traceroute6` con quelli di `ping` per avere un quadro più completo.