# [Linux] C Shell (csh) mkfs użycie: Tworzenie systemu plików

## Overview
Polecenie `mkfs` (make filesystem) służy do tworzenia systemów plików na urządzeniach pamięci masowej, takich jak dyski twarde, partycje czy pamięci USB. Umożliwia formatowanie urządzenia w określonym formacie systemu plików, co jest niezbędne przed jego użyciem do przechowywania danych.

## Usage
Podstawowa składnia polecenia `mkfs` jest następująca:

```csh
mkfs [opcje] [argumenty]
```

## Common Options
- `-t <typ>`: Określa typ systemu plików, np. ext4, vfat.
- `-L <etykieta>`: Ustala etykietę dla systemu plików.
- `-n`: Tworzy system plików bez zapisywania na nim danych (przydatne do testów).
- `-V`: Wyświetla szczegóły dotyczące procesu tworzenia systemu plików.

## Common Examples
Przykłady użycia polecenia `mkfs`:

1. Tworzenie systemu plików ext4 na urządzeniu `/dev/sdb1`:
   ```csh
   mkfs -t ext4 /dev/sdb1
   ```

2. Tworzenie systemu plików vfat z etykietą "DANE":
   ```csh
   mkfs -t vfat -L DANE /dev/sdc1
   ```

3. Tworzenie systemu plików bez zapisywania danych (test):
   ```csh
   mkfs -n -t ext4 /dev/sdd1
   ```

4. Wyświetlenie szczegółów tworzenia systemu plików:
   ```csh
   mkfs -V -t ext4 /dev/sde1
   ```

## Tips
- Zawsze upewnij się, że wybrane urządzenie jest poprawne, ponieważ `mkfs` usunie wszystkie dane na tym urządzeniu.
- Przed użyciem `mkfs`, warto zamontować urządzenie, aby sprawdzić, czy jest ono poprawnie rozpoznawane przez system.
- Używaj opcji `-n` do testowania procesu bez faktycznego formatowania, co może być przydatne w przypadku nauki lub testowania skryptów.