# [Linux] C Shell (csh) pr: Stampa file in un formato leggibile

## Overview
Il comando `pr` in C Shell (csh) viene utilizzato per formattare e stampare file di testo in un modo che è più leggibile. Questo comando è particolarmente utile per preparare documenti per la stampa, poiché organizza il contenuto in pagine e colonne.

## Usage
La sintassi di base del comando `pr` è la seguente:

```
pr [opzioni] [argomenti]
```

## Common Options
Ecco alcune opzioni comuni per il comando `pr`:

- `-l [numero]`: Imposta il numero di righe per pagina.
- `-w [numero]`: Imposta la larghezza della pagina in caratteri.
- `-t`: Non aggiunge intestazioni e numeri di pagina.
- `-s [carattere]`: Specifica un carattere di separazione tra le colonne.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `pr`:

1. **Stampare un file con intestazioni e numeri di pagina**:
   ```bash
   pr documento.txt
   ```

2. **Impostare il numero di righe per pagina a 50**:
   ```bash
   pr -l 50 documento.txt
   ```

3. **Stampare senza intestazioni**:
   ```bash
   pr -t documento.txt
   ```

4. **Impostare la larghezza della pagina a 100 caratteri**:
   ```bash
   pr -w 100 documento.txt
   ```

5. **Stampare due file affiancati**:
   ```bash
   pr file1.txt file2.txt
   ```

## Tips
- Quando si utilizza `pr`, è utile visualizzare l'output su schermo prima di stampare, per assicurarsi che la formattazione sia corretta.
- Sperimenta con le opzioni `-l` e `-w` per trovare la configurazione che meglio si adatta alle tue esigenze di stampa.
- Se stai preparando documenti per la stampa, considera di utilizzare l'opzione `-s` per migliorare la leggibilità delle colonne.