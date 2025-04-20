# [Linux] C Shell (csh) hwclock: Ustawianie i wyświetlanie czasu sprzętowego

## Overview
Polecenie `hwclock` służy do odczytywania i ustawiania czasu sprzętowego (RTC - Real Time Clock) w systemie. Czas sprzętowy jest niezależny od systemu operacyjnego i jest przechowywany w pamięci, nawet gdy komputer jest wyłączony.

## Usage
Podstawowa składnia polecenia `hwclock` jest następująca:

```csh
hwclock [options] [arguments]
```

## Common Options
- `--show`: Wyświetla aktualny czas sprzętowy.
- `--set`: Ustawia czas sprzętowy na wartość podaną w argumentach.
- `--hctosys`: Ustawia czas systemowy na czas sprzętowy.
- `--systohc`: Ustawia czas sprzętowy na czas systemowy.
- `--utc`: Używa czasu UTC (Coordinated Universal Time) zamiast lokalnego czasu.

## Common Examples
1. **Wyświetlenie aktualnego czasu sprzętowego:**
   ```csh
   hwclock --show
   ```

2. **Ustawienie czasu sprzętowego na określoną datę i godzinę:**
   ```csh
   hwclock --set --date="2023-10-01 12:00:00"
   ```

3. **Ustawienie czasu systemowego na czas sprzętowy:**
   ```csh
   hwclock --hctosys
   ```

4. **Ustawienie czasu sprzętowego na czas systemowy:**
   ```csh
   hwclock --systohc
   ```

5. **Wyświetlenie czasu sprzętowego w formacie UTC:**
   ```csh
   hwclock --show --utc
   ```

## Tips
- Zawsze upewnij się, że czas systemowy jest poprawny przed ustawieniem czasu sprzętowego.
- Używaj opcji `--utc`, jeśli twój system operacyjny wymaga czasu w formacie UTC.
- Regularnie synchronizuj czas sprzętowy z czasem systemowym, aby uniknąć rozbieżności.