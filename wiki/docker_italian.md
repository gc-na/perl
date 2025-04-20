# [Linux] C Shell (csh) docker uso: Gestire contenitori e immagini Docker

## Overview
Il comando `docker` è uno strumento fondamentale per gestire contenitori e immagini Docker. Permette di creare, eseguire e gestire applicazioni in contenitori, facilitando lo sviluppo e il deployment di software in ambienti isolati.

## Usage
La sintassi di base del comando `docker` è la seguente:

```csh
docker [options] [arguments]
```

## Common Options
Ecco alcune opzioni comuni per il comando `docker`:

- `run`: Esegue un nuovo contenitore.
- `ps`: Mostra i contenitori in esecuzione.
- `images`: Elenca le immagini disponibili localmente.
- `rm`: Rimuove uno o più contenitori.
- `rmi`: Rimuove una o più immagini.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `docker`:

1. **Eseguire un contenitore**:
   ```csh
   docker run hello-world
   ```

2. **Elencare i contenitori in esecuzione**:
   ```csh
   docker ps
   ```

3. **Elencare tutte le immagini**:
   ```csh
   docker images
   ```

4. **Rimuovere un contenitore**:
   ```csh
   docker rm nome_contenitore
   ```

5. **Rimuovere un'immagine**:
   ```csh
   docker rmi nome_immagine
   ```

## Tips
- Assicurati di avere i permessi necessari per eseguire i comandi Docker, potresti dover usare `sudo` in alcuni casi.
- Utilizza `docker-compose` per gestire applicazioni multi-contenitore in modo più semplice.
- Controlla regolarmente le immagini e i contenitori non utilizzati per liberare spazio sul disco.