# [Linux] C Shell (csh) curl Utilizzo: Strumento per trasferire dati da o verso un server

## Overview
Il comando `curl` è uno strumento da riga di comando utilizzato per trasferire dati da o verso un server. Supporta vari protocolli, tra cui HTTP, HTTPS, FTP e molti altri. È molto utile per testare API, scaricare file e inviare dati.

## Usage
La sintassi di base del comando `curl` è la seguente:

```csh
curl [options] [arguments]
```

## Common Options
Ecco alcune opzioni comuni per `curl`:

- `-X`: Specifica il metodo HTTP da utilizzare (GET, POST, PUT, DELETE, ecc.).
- `-d`: Invia dati nel corpo della richiesta (utilizzato principalmente con POST).
- `-H`: Aggiunge un'intestazione HTTP personalizzata.
- `-o`: Specifica il nome del file in cui salvare l'output.
- `-I`: Recupera solo le intestazioni della risposta.

## Common Examples
Ecco alcuni esempi pratici di utilizzo di `curl`:

1. **Scaricare un file:**
   ```csh
   curl -o file.txt http://example.com/file.txt
   ```

2. **Inviare una richiesta GET:**
   ```csh
   curl http://example.com/api/data
   ```

3. **Inviare una richiesta POST con dati:**
   ```csh
   curl -X POST -d "param1=value1&param2=value2" http://example.com/api/submit
   ```

4. **Aggiungere un'intestazione personalizzata:**
   ```csh
   curl -H "Authorization: Bearer token" http://example.com/api/protected
   ```

5. **Recuperare solo le intestazioni della risposta:**
   ```csh
   curl -I http://example.com
   ```

## Tips
- Utilizza l'opzione `-v` per attivare il verbose mode, che fornisce informazioni dettagliate sulla richiesta e sulla risposta.
- Ricorda di utilizzare le virgolette per i dati che contengono caratteri speciali o spazi.
- Se stai testando API, considera l'uso di strumenti come Postman per un'interfaccia grafica, ma `curl` è ottimo per script e automazione.