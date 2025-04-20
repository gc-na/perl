# [Linux] C Shell (csh) mount użycie: Montowanie systemów plików

## Overview
Polecenie `mount` służy do montowania systemów plików w systemie operacyjnym. Umożliwia dostęp do danych przechowywanych na różnych nośnikach, takich jak dyski twarde, pamięci USB czy inne urządzenia.

## Usage
Podstawowa składnia polecenia `mount` jest następująca:

```
mount [opcje] [argumenty]
```

## Common Options
- `-t <typ>`: Określa typ systemu plików, który ma być zamontowany (np. ext4, ntfs).
- `-o <opcje>`: Umożliwia podanie dodatkowych opcji montowania, takich jak `ro` (tylko do odczytu) lub `rw` (do odczytu i zapisu).
- `-a`: Montuje wszystkie systemy plików wymienione w pliku `/etc/fstab`.
- `-r`: Montuje system plików w trybie tylko do odczytu.

## Common Examples
1. Montowanie systemu plików z urządzenia `/dev/sdb1` do katalogu `/mnt`:
   ```bash
   mount /dev/sdb1 /mnt
   ```

2. Montowanie systemu plików NTFS z dodatkową opcją tylko do odczytu:
   ```bash
   mount -t ntfs -o ro /dev/sdc1 /mnt/usb
   ```

3. Montowanie wszystkich systemów plików z pliku `/etc/fstab`:
   ```bash
   mount -a
   ```

4. Montowanie systemu plików z opcją do odczytu i zapisu:
   ```bash
   mount -o rw /dev/sda1 /mnt/data
   ```

## Tips
- Zawsze upewnij się, że katalog, do którego montujesz system plików, istnieje.
- Sprawdź, czy masz odpowiednie uprawnienia do montowania urządzeń, zazwyczaj wymaga to uprawnień administratora.
- Po zakończeniu pracy z zamontowanym systemem plików, pamiętaj o jego odmontowaniu za pomocą polecenia `umount`, aby uniknąć utraty danych.