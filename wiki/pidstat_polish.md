# [Linux] C Shell (csh) pidstat użycie: Monitorowanie statystyk procesów

## Overview
Polecenie `pidstat` służy do monitorowania statystyk procesów w systemie Linux. Umożliwia użytkownikom śledzenie wykorzystania CPU, pamięci i innych zasobów przez poszczególne procesy w czasie rzeczywistym.

## Usage
Podstawowa składnia polecenia `pidstat` jest następująca:

```bash
pidstat [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `pidstat`:

- `-h`: Wyświetla nagłówki w formacie przyjaznym dla użytkownika.
- `-r`: Wyświetla statystyki pamięci.
- `-u`: Wyświetla statystyki użycia CPU.
- `-p <PID>`: Monitoruje określony proces na podstawie jego identyfikatora PID.
- `-t`: Wyświetla statystyki dla wszystkich wątków danego procesu.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `pidstat`:

1. Aby monitorować użycie CPU przez wszystkie procesy co 2 sekundy:
   ```bash
   pidstat 2
   ```

2. Aby wyświetlić statystyki pamięci dla wszystkich procesów:
   ```bash
   pidstat -r
   ```

3. Aby monitorować określony proces o PID 1234:
   ```bash
   pidstat -p 1234
   ```

4. Aby uzyskać statystyki dla wszystkich wątków procesu o PID 5678:
   ```bash
   pidstat -t -p 5678
   ```

5. Aby wyświetlić statystyki użycia CPU w formacie przyjaznym dla użytkownika:
   ```bash
   pidstat -u -h
   ```

## Tips
- Używaj opcji `-r` i `-u` razem, aby uzyskać pełny obraz wykorzystania zasobów przez procesy.
- Regularne monitorowanie procesów może pomóc w identyfikacji problemów z wydajnością w systemie.
- Rozważ użycie `pidstat` w skryptach, aby automatycznie zbierać dane o wydajności procesów w określonych interwałach.