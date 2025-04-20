# [Linux] C Shell (csh) parted użycie: Zarządzanie partycjami dysku

## Overview
Polecenie `parted` jest narzędziem do zarządzania partycjami dysku. Umożliwia tworzenie, usuwanie, zmienianie rozmiaru oraz formatowanie partycji na dyskach twardych i innych nośnikach danych. Dzięki `parted` można łatwo zarządzać strukturą partycji w systemie.

## Usage
Podstawowa składnia polecenia `parted` jest następująca:

```bash
parted [opcje] [argumenty]
```

## Common Options
- `-l` - Wyświetla listę dostępnych dysków i ich partycji.
- `mklabel` - Tworzy nową tablicę partycji (np. msdos, gpt).
- `mkpart` - Tworzy nową partycję.
- `rm` - Usuwa istniejącą partycję.
- `resizepart` - Zmienia rozmiar istniejącej partycji.
- `print` - Wyświetla szczegóły dotyczące partycji na wybranym dysku.

## Common Examples
1. **Wyświetlenie listy dysków i partycji:**
   ```bash
   parted -l
   ```

2. **Tworzenie nowej tablicy partycji:**
   ```bash
   parted /dev/sda mklabel gpt
   ```

3. **Tworzenie nowej partycji:**
   ```bash
   parted /dev/sda mkpart primary ext4 1MiB 100MiB
   ```

4. **Usuwanie partycji:**
   ```bash
   parted /dev/sda rm 1
   ```

5. **Zmiana rozmiaru partycji:**
   ```bash
   parted /dev/sda resizepart 1 200MiB
   ```

6. **Wyświetlenie szczegółów partycji:**
   ```bash
   parted /dev/sda print
   ```

## Tips
- Zawsze wykonuj kopię zapasową danych przed modyfikacją partycji, aby uniknąć utraty danych.
- Używaj opcji `print` przed i po dokonaniu zmian, aby upewnić się, że operacje zostały przeprowadzone prawidłowo.
- Upewnij się, że nie masz otwartych plików lub systemów plików na partycjach, które zamierzasz modyfikować.