# [Linux] C Shell (csh) mount utilizare: Montarea sistemelor de fișiere

## Overview
Comanda `mount` este utilizată pentru a conecta un sistem de fișiere la un punct de montare din sistemul de operare. Aceasta permite accesarea fișierelor și directoarelor de pe dispozitive externe sau de pe alte partiții ale sistemului.

## Usage
Sintaxa de bază a comenzii `mount` este următoarea:

```
mount [opțiuni] [argumente]
```

## Common Options
- `-t <tip>`: Specifică tipul sistemului de fișiere (de exemplu, ext4, ntfs).
- `-o <opțiuni>`: Permite specificarea opțiunilor de montare, cum ar fi `ro` (read-only) sau `rw` (read-write).
- `-a`: Montează toate sistemele de fișiere specificate în fișierul `/etc/fstab`.
- `-r`: Montează sistemul de fișiere în modul read-only.

## Common Examples
1. Montarea unui sistem de fișiere ext4:
   ```bash
   mount -t ext4 /dev/sda1 /mnt/point
   ```

2. Montarea unui sistem de fișiere NTFS în modul read-write:
   ```bash
   mount -t ntfs -o rw /dev/sdb1 /mnt/usb
   ```

3. Montarea tuturor sistemelor de fișiere din `/etc/fstab`:
   ```bash
   mount -a
   ```

4. Montarea unui sistem de fișiere în modul read-only:
   ```bash
   mount -o ro /dev/sdc1 /mnt/read_only
   ```

## Tips
- Asigurați-vă că aveți permisiuni suficiente pentru a monta sistemele de fișiere.
- Verificați întotdeauna dacă punctul de montare este gol înainte de a monta un sistem de fișiere pentru a evita pierderea de date.
- Utilizați comanda `umount` pentru a de-monta sistemele de fișiere atunci când nu mai sunt necesare.