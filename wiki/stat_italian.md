# [Linux] C Shell (csh) stat Uso: Visualizza informazioni sui file

## Overview
Il comando `stat` in C Shell (csh) viene utilizzato per visualizzare informazioni dettagliate sui file e sulle directory. Fornisce dati come la dimensione del file, le date di accesso e modifica, e i permessi di accesso.

## Usage
La sintassi di base del comando `stat` è la seguente:

```csh
stat [options] [arguments]
```

## Common Options
- `-c` : Specifica un formato di output personalizzato.
- `-f` : Mostra informazioni sul file in un formato specifico.
- `-L` : Segue i collegamenti simbolici per mostrare le informazioni del file di destinazione.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `stat`:

1. Visualizzare le informazioni di base su un file:
   ```csh
   stat nomefile.txt
   ```

2. Usare un formato personalizzato per visualizzare solo la dimensione e la data di modifica:
   ```csh
   stat -c '%s %y' nomefile.txt
   ```

3. Ottenere informazioni su un collegamento simbolico seguendo il collegamento:
   ```csh
   stat -L collegamento_simbolico
   ```

4. Visualizzare informazioni su una directory:
   ```csh
   stat /percorso/directory
   ```

## Tips
- Utilizza l'opzione `-c` per personalizzare l'output e ottenere solo le informazioni necessarie.
- Ricorda che `stat` può fornire informazioni utili per il debug e la gestione dei file.
- Verifica i permessi di accesso per assicurarti di avere i diritti necessari per visualizzare le informazioni sui file.