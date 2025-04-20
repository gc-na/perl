# [Linux] C Shell (csh) parted uso: Gestire le partizioni del disco

## Overview
Il comando `parted` è uno strumento potente per gestire le partizioni del disco. Permette di creare, eliminare, ridimensionare e modificare le partizioni su dispositivi di memorizzazione, rendendolo essenziale per la gestione del sistema.

## Usage
La sintassi di base del comando `parted` è la seguente:

```bash
parted [options] [arguments]
```

## Common Options
- `-l` : Elenca tutte le partizioni disponibili.
- `mkpart` : Crea una nuova partizione.
- `rm` : Rimuove una partizione esistente.
- `resizepart` : Ridimensiona una partizione esistente.
- `print` : Mostra la tabella delle partizioni attuale.

## Common Examples

### Elencare le partizioni
Per elencare tutte le partizioni disponibili, usa il seguente comando:

```bash
parted -l
```

### Creare una nuova partizione
Per creare una nuova partizione, utilizza il comando:

```bash
parted /dev/sda mkpart primary ext4 1GB 5GB
```

### Rimuovere una partizione
Per rimuovere una partizione, esegui:

```bash
parted /dev/sda rm 1
```

### Ridimensionare una partizione
Per ridimensionare una partizione esistente, usa:

```bash
parted /dev/sda resizepart 1 10GB
```

### Visualizzare la tabella delle partizioni
Per visualizzare la tabella delle partizioni, utilizza:

```bash
parted /dev/sda print
```

## Tips
- Assicurati di avere un backup dei dati importanti prima di modificare le partizioni.
- Utilizza `parted` con i privilegi di superutente per garantire l'accesso ai dispositivi di memorizzazione.
- Controlla sempre la tabella delle partizioni dopo aver effettuato modifiche per confermare che tutto sia corretto.