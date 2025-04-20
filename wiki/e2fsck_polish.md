# [Linux] C Shell (csh) e2fsck użycie: Sprawdzanie i naprawa systemów plików ext2/ext3/ext4

## Overview
Polecenie `e2fsck` służy do sprawdzania i naprawy systemów plików w formacie ext2, ext3 oraz ext4. Pomaga w identyfikacji i naprawie błędów, które mogą wystąpić na dyskach twardych lub innych nośnikach danych.

## Usage
Podstawowa składnia polecenia `e2fsck` jest następująca:

```shell
e2fsck [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla `e2fsck`:

- `-f`: Wymusza sprawdzenie systemu plików, nawet jeśli wydaje się, że jest on czysty.
- `-n`: Uruchamia sprawdzenie w trybie tylko do odczytu, nie wprowadza żadnych zmian.
- `-y`: Automatycznie odpowiada "tak" na wszystkie pytania, co przyspiesza proces naprawy.
- `-c`: Sprawdza, czy na dysku występują błędy, używając testu powierzchniowego.

## Common Examples
Oto kilka praktycznych przykładów użycia `e2fsck`:

1. Sprawdzenie systemu plików na urządzeniu `/dev/sda1`:
   ```shell
   e2fsck /dev/sda1
   ```

2. Wymuszenie sprawdzenia systemu plików, nawet jeśli jest czysty:
   ```shell
   e2fsck -f /dev/sda1
   ```

3. Sprawdzenie systemu plików w trybie tylko do odczytu:
   ```shell
   e2fsck -n /dev/sda1
   ```

4. Automatyczne naprawianie błędów:
   ```shell
   e2fsck -y /dev/sda1
   ```

5. Sprawdzenie błędów na dysku z testem powierzchniowym:
   ```shell
   e2fsck -c /dev/sda1
   ```

## Tips
- Zawsze wykonuj kopię zapasową danych przed użyciem `e2fsck`, aby uniknąć utraty danych w przypadku poważnych błędów.
- Używaj opcji `-n` na początku, aby zobaczyć, jakie zmiany będą wprowadzone, zanim zdecydujesz się na ich zastosowanie.
- Regularnie sprawdzaj systemy plików, aby zapobiegać problemom, zanim staną się poważne.