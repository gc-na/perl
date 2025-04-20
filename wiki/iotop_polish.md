# [Linux] C Shell (csh) iotop użycie: Monitorowanie użycia dysku przez procesy

## Overview
Polecenie `iotop` służy do monitorowania użycia dysku przez procesy w systemie Linux. Umożliwia użytkownikom obserwację, które procesy generują największy ruch dyskowy, co jest przydatne w diagnostyce wydajności systemu.

## Usage
Podstawowa składnia polecenia `iotop` jest następująca:

```bash
iotop [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla `iotop`:

- `-o` – Wyświetla tylko procesy, które aktualnie wykonują operacje I/O.
- `-b` – Uruchamia `iotop` w trybie wsadowym, co jest przydatne do zapisywania wyników do pliku.
- `-n NUM` – Określa liczbę iteracji, po których `iotop` zakończy działanie.
- `-d SEC` – Ustawia czas opóźnienia między aktualizacjami w sekundach.

## Common Examples
Oto kilka praktycznych przykładów użycia `iotop`:

1. Aby uruchomić `iotop` i obserwować procesy z aktualizacjami w czasie rzeczywistym:
   ```bash
   iotop
   ```

2. Aby wyświetlić tylko procesy, które wykonują operacje I/O:
   ```bash
   iotop -o
   ```

3. Aby uruchomić `iotop` w trybie wsadowym i zapisać wyniki do pliku:
   ```bash
   iotop -b -n 10 > iotop_output.txt
   ```

4. Aby ustawić czas opóźnienia między aktualizacjami na 2 sekundy:
   ```bash
   iotop -d 2
   ```

## Tips
- Używaj opcji `-o`, aby szybko zidentyfikować procesy, które obecnie obciążają dysk.
- W trybie wsadowym możesz łatwo analizować dane później, zapisując je do pliku.
- Regularnie monitoruj użycie dysku, aby wykrywać potencjalne problemy z wydajnością w systemie.