# [Linux] C Shell (csh) fsck użycie: Sprawdzanie systemu plików

## Przegląd
Polecenie `fsck` (file system check) służy do sprawdzania i naprawiania błędów w systemach plików. Jest to ważne narzędzie, które pomaga utrzymać integralność danych na dysku, zwłaszcza po nieprawidłowym zamknięciu systemu lub awarii sprzętu.

## Użycie
Podstawowa składnia polecenia `fsck` jest następująca:

```csh
fsck [opcje] [argumenty]
```

## Częste opcje
- `-a`: Automatycznie naprawia błędy bez interakcji z użytkownikiem.
- `-n`: Przeprowadza kontrolę bez wprowadzania jakichkolwiek zmian.
- `-y`: Odpowiada "tak" na wszystkie pytania, co oznacza, że wszystkie błędy zostaną naprawione automatycznie.
- `-t`: Wyświetla czas potrzebny na wykonanie sprawdzenia.

## Częste przykłady
1. Sprawdzenie systemu plików na określonym urządzeniu:
   ```csh
   fsck /dev/sda1
   ```

2. Automatyczna naprawa błędów:
   ```csh
   fsck -a /dev/sda1
   ```

3. Sprawdzenie systemu plików bez wprowadzania zmian:
   ```csh
   fsck -n /dev/sda1
   ```

4. Naprawa wszystkich błędów automatycznie:
   ```csh
   fsck -y /dev/sda1
   ```

## Wskazówki
- Zawsze wykonuj kopię zapasową ważnych danych przed użyciem `fsck`, aby uniknąć utraty danych.
- Używaj opcji `-n` do testowania, zanim zdecydujesz się na automatyczne naprawy.
- Wykonuj `fsck` w trybie jednego użytkownika, aby uniknąć problemów z plikami używanymi przez inne procesy.