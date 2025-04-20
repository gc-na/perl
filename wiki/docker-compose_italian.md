# [Linux] C Shell (csh) docker-compose utilizzo: Gestire applicazioni Docker multi-contenitore

## Overview
Il comando `docker-compose` è uno strumento per definire e gestire applicazioni Docker multi-contenitore. Permette di configurare i servizi, le reti e i volumi necessari in un file di configurazione, semplificando il processo di avvio e gestione delle applicazioni.

## Usage
La sintassi di base del comando `docker-compose` è la seguente:

```bash
docker-compose [options] [arguments]
```

## Common Options
Ecco alcune opzioni comuni per `docker-compose`:

- `up`: Avvia i contenitori definiti nel file `docker-compose.yml`.
- `down`: Ferma e rimuove i contenitori, le reti e i volumi creati da `up`.
- `build`: Costruisce o ricostruisce i servizi.
- `logs`: Mostra i log dei contenitori.
- `ps`: Elenca i contenitori in esecuzione.

## Common Examples
Ecco alcuni esempi pratici di utilizzo di `docker-compose`:

### Avviare i contenitori
```bash
docker-compose up
```

### Avviare i contenitori in modalità staccata
```bash
docker-compose up -d
```

### Fermare e rimuovere i contenitori
```bash
docker-compose down
```

### Costruire i servizi
```bash
docker-compose build
```

### Visualizzare i log
```bash
docker-compose logs
```

### Elencare i contenitori in esecuzione
```bash
docker-compose ps
```

## Tips
- Utilizza il flag `-d` con `up` per eseguire i contenitori in background.
- Assicurati di avere un file `docker-compose.yml` ben configurato per evitare errori durante l'avvio.
- Usa `docker-compose logs -f` per seguire i log in tempo reale.
- Considera di utilizzare variabili d'ambiente nel tuo file `docker-compose.yml` per una configurazione più flessibile.