# [Linux] C Shell (csh) tail użycie: Wyświetlanie końcowych linii pliku

## Overview
Polecenie `tail` służy do wyświetlania ostatnich linii pliku tekstowego. Jest to przydatne narzędzie do monitorowania logów lub plików, które są często aktualizowane.

## Usage
Podstawowa składnia polecenia `tail` jest następująca:

```csh
tail [options] [arguments]
```

## Common Options
- `-n <number>`: Określa liczbę linii do wyświetlenia. Domyślnie wyświetlane jest 10 ostatnich linii.
- `-f`: Śledzi plik w czasie rzeczywistym, wyświetlając nowe linie, gdy są dodawane.
- `-c <number>`: Wyświetla określoną liczbę bajtów z końca pliku.

## Common Examples
- Wyświetlenie ostatnich 10 linii pliku `log.txt`:
  ```csh
  tail log.txt
  ```

- Wyświetlenie ostatnich 20 linii pliku `log.txt`:
  ```csh
  tail -n 20 log.txt
  ```

- Śledzenie pliku `log.txt` w czasie rzeczywistym:
  ```csh
  tail -f log.txt
  ```

- Wyświetlenie ostatnich 50 bajtów pliku `data.txt`:
  ```csh
  tail -c 50 data.txt
  ```

## Tips
- Używaj opcji `-f`, aby monitorować pliki logów w czasie rzeczywistym, co jest szczególnie przydatne podczas debugowania aplikacji.
- Możesz łączyć `tail` z innymi poleceniami, takimi jak `grep`, aby filtrować wyniki. Na przykład:
  ```csh
  tail -f log.txt | grep "ERROR"
  ```
- Pamiętaj, że `tail` działa najlepiej z plikami tekstowymi; używanie go z plikami binarnymi może prowadzić do nieprzewidywalnych wyników.