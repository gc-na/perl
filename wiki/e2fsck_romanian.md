# [Linux] C Shell (csh) e2fsck utilizare: Verificarea sistemului de fișiere ext2/ext3/ext4

## Overview
Comanda `e2fsck` este utilizată pentru a verifica și repara sistemele de fișiere de tip ext2, ext3 și ext4. Aceasta asigură integritatea datelor și corectează eventualele erori care pot apărea în structura sistemului de fișiere.

## Usage
Sintaxa de bază a comenzii `e2fsck` este următoarea:

```bash
e2fsck [options] [arguments]
```

## Common Options
- `-p`: Verificare rapidă a sistemului de fișiere, fără a solicita confirmarea utilizatorului.
- `-f`: Forțează verificarea sistemului de fișiere, chiar dacă acesta pare a fi curat.
- `-y`: Răspunde automat „da” la toate întrebările, acceptând toate modificările.
- `-c`: Verifică blocurile de date pentru erori, marcându-le ca defecte.
- `-n`: Efectuează verificarea fără a face modificări, util pentru diagnosticare.

## Common Examples
1. Verificarea unui sistem de fișiere specific:
   ```bash
   e2fsck /dev/sda1
   ```

2. Verificare rapidă fără confirmare:
   ```bash
   e2fsck -p /dev/sda1
   ```

3. Forțarea verificării sistemului de fișiere:
   ```bash
   e2fsck -f /dev/sda1
   ```

4. Verificarea și acceptarea automată a modificărilor:
   ```bash
   e2fsck -y /dev/sda1
   ```

5. Verificarea blocurilor defecte:
   ```bash
   e2fsck -c /dev/sda1
   ```

## Tips
- Asigurați-vă că sistemul de fișiere pe care doriți să-l verificați nu este montat. Este recomandat să efectuați verificarea dintr-un mediu de recuperare sau dintr-un sistem live.
- Faceți o copie de rezervă a datelor importante înainte de a rula `e2fsck`, mai ales dacă utilizați opțiuni care modifică sistemul de fișiere.
- Utilizați opțiunea `-n` pentru a verifica sistemul de fișiere fără a face modificări, în scopuri de diagnosticare.