# [Linux] C Shell (csh) paste uso equivalente: Unire file riga per riga

## Overview
Il comando `paste` in C Shell (csh) è utilizzato per unire file di testo riga per riga. Questo comando combina le righe di due o più file, separandole con un delimitatore specificato, creando così un output tabellare.

## Usage
La sintassi di base del comando `paste` è la seguente:

```csh
paste [options] [arguments]
```

## Common Options
- `-d DELIMITER`: Specifica un delimitatore personalizzato per separare le colonne.
- `-s`: Unisce le righe di ogni file in un'unica riga, separando le righe con un delimitatore.
- `-z`: Tratta il delimitatore come una stringa vuota, unendo le righe senza alcun separatore.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `paste`:

1. **Unire due file riga per riga con un delimitatore predefinito (tabulazione):**
   ```csh
   paste file1.txt file2.txt
   ```

2. **Unire due file utilizzando una virgola come delimitatore:**
   ```csh
   paste -d ',' file1.txt file2.txt
   ```

3. **Unire le righe di un file in un'unica riga:**
   ```csh
   paste -s file1.txt
   ```

4. **Unire più file e utilizzare un delimitatore personalizzato:**
   ```csh
   paste -d '|' file1.txt file2.txt file3.txt
   ```

## Tips
- Assicurati che i file che stai unendo abbiano lo stesso numero di righe per evitare output imprevisti.
- Puoi combinare `paste` con altri comandi come `sort` o `uniq` per elaborare ulteriormente l'output.
- Utilizza l'opzione `-s` se desideri una visualizzazione più compatta delle righe di un singolo file.