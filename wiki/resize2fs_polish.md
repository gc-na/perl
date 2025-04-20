# [Linux] C Shell (csh) resize2fs użycie: Zmiana rozmiaru systemu plików ext2/ext3/ext4

## Przegląd
Polecenie `resize2fs` służy do zmiany rozmiaru systemu plików ext2, ext3 lub ext4. Umożliwia powiększanie lub zmniejszanie rozmiaru systemu plików, co jest przydatne w zarządzaniu przestrzenią dyskową.

## Użycie
Podstawowa składnia polecenia `resize2fs` wygląda następująco:

```bash
resize2fs [opcje] [argumenty]
```

## Częste opcje
- `-f`: Wymusza zmianę rozmiaru systemu plików, nawet jeśli nie jest to zalecane.
- `-p`: Wyświetla postęp operacji zmiany rozmiaru.
- `-s`: Zmienia rozmiar systemu plików do określonego rozmiaru, ale nie zmienia rozmiaru partycji.
- `-M`: Zmniejsza rozmiar systemu plików do minimalnego rozmiaru.

## Częste przykłady
1. Powiększenie systemu plików do maksymalnego rozmiaru dostępnego na partycji:
   ```bash
   resize2fs /dev/sda1
   ```

2. Zmniejszenie systemu plików do 20 GB:
   ```bash
   resize2fs -s 20G /dev/sda1
   ```

3. Wyświetlenie postępu podczas zmiany rozmiaru:
   ```bash
   resize2fs -p /dev/sda1
   ```

4. Wymuszenie zmiany rozmiaru systemu plików:
   ```bash
   resize2fs -f /dev/sda1
   ```

## Wskazówki
- Zawsze wykonuj kopię zapasową danych przed zmianą rozmiaru systemu plików, aby uniknąć utraty danych.
- Upewnij się, że system plików jest odmontowany przed jego zmniejszeniem.
- Sprawdź system plików za pomocą `e2fsck` przed i po zmianie rozmiaru, aby upewnić się, że nie ma błędów.