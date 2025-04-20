# [Linux] C Shell (csh) watch użycie: monitorowanie poleceń w czasie rzeczywistym

## Overview
Polecenie `watch` w C Shell (csh) służy do wykonywania innego polecenia cyklicznie w określonych odstępach czasu, co pozwala na monitorowanie jego wyników w czasie rzeczywistym. Jest to przydatne narzędzie do obserwacji zmian w danych lub statusie systemu.

## Usage
Podstawowa składnia polecenia `watch` jest następująca:

```csh
watch [opcje] [argumenty]
```

## Common Options
- `-n <sekundy>`: Ustala interwał czasowy w sekundach, co ile polecenie ma być wykonywane. Domyślnie jest to 2 sekundy.
- `-d`: Podświetla różnice między kolejnymi wynikami, co ułatwia zauważenie zmian.
- `-t`: Wyłącza wyświetlanie nagłówka, co może być przydatne w przypadku długich wyników.

## Common Examples
Przykłady użycia polecenia `watch`:

1. Monitorowanie zawartości katalogu co 5 sekund:
   ```csh
   watch -n 5 ls -l
   ```

2. Obserwacja użycia pamięci RAM:
   ```csh
   watch free -h
   ```

3. Monitorowanie procesu `httpd`:
   ```csh
   watch -d ps aux | grep httpd
   ```

4. Sprawdzanie statusu serwera ping co 3 sekundy:
   ```csh
   watch -n 3 ping -c 1 example.com
   ```

## Tips
- Używaj opcji `-d`, aby szybko zauważyć zmiany w wynikach.
- Dostosuj interwał czasowy do swoich potrzeb, aby nie obciążać systemu zbyt częstymi zapytaniami.
- Możesz łączyć `watch` z innymi poleceniami, aby uzyskać bardziej złożone wyniki, np. używając potoków.