# [Linux] C Shell (csh) nohup użycie: Uruchamianie procesów w tle bez przerywania

## Overview
Polecenie `nohup` (no hang up) w systemie C Shell (csh) służy do uruchamiania procesów, które mają działać w tle, nawet po wylogowaniu się z sesji. Dzięki temu, procesy nie są przerywane, gdy terminal zostaje zamknięty.

## Usage
Podstawowa składnia polecenia `nohup` wygląda następująco:

```csh
nohup [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `nohup`:

- `&` - Uruchamia proces w tle.
- `-o` - Umożliwia określenie pliku, do którego będą zapisywane standardowe dane wyjściowe.
- `-e` - Umożliwia określenie pliku, do którego będą zapisywane standardowe dane błędów.

## Common Examples
Oto kilka praktycznych przykładów użycia `nohup`:

1. Uruchamianie skryptu w tle:
   ```csh
   nohup ./myscript.sh &
   ```

2. Uruchamianie polecenia `ping` i zapisywanie wyjścia do pliku:
   ```csh
   nohup ping google.com > output.txt &
   ```

3. Uruchamianie programu z błędami zapisywanymi w osobnym pliku:
   ```csh
   nohup ./myprogram > output.txt 2> error.txt &
   ```

## Tips
- Zawsze używaj `&` na końcu polecenia, aby uruchomić proces w tle.
- Sprawdzaj plik `nohup.out`, aby zobaczyć standardowe dane wyjściowe, jeśli nie określisz innego pliku.
- Używaj `jobs` i `bg` do zarządzania procesami w tle, jeśli potrzebujesz ich później wznowić.