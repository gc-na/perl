# [Linux] C Shell (csh) basename utilizare: Extrage numele fișierului dintr-un path

## Overview
Comanda `basename` este utilizată pentru a extrage numele fișierului dintr-un path complet, eliminând orice prefix de director. Aceasta este utilă atunci când doriți să obțineți doar numele fișierului fără a include calea completă.

## Usage
Sintaxa de bază a comenzii este următoarea:
```
basename [options] [arguments]
```

## Common Options
- `-a`: Acceptă mai multe argumente și returnează numele de bază pentru fiecare.
- `-s`: Specifică un sufix care va fi eliminat din numele fișierului.

## Common Examples
1. Extrageți numele fișierului dintr-un path:
   ```csh
   basename /usr/local/bin/script.sh
   ```
   Output: `script.sh`

2. Utilizați opțiunea `-s` pentru a elimina un sufix specific:
   ```csh
   basename myfile.txt .txt
   ```
   Output: `myfile`

3. Extrageți numele de bază pentru mai multe fișiere:
   ```csh
   basename -a /path/to/file1.txt /path/to/file2.txt
   ```
   Output:
   ```
   file1.txt
   file2.txt
   ```

## Tips
- Folosiți `basename` în scripturi pentru a simplifica manipularea fișierelor.
- Combinați `basename` cu alte comenzi, cum ar fi `find`, pentru a obține numele fișierelor dintr-o structură de directoare complexă.