# [Linux] C Shell (csh) tcpdump użycie: Narzędzie do przechwytywania i analizy pakietów sieciowych

## Przegląd
Polecenie `tcpdump` służy do przechwytywania i analizy pakietów sieciowych w systemach operacyjnych Unix i Linux. Umożliwia użytkownikom monitorowanie ruchu sieciowego, co jest przydatne w diagnostyce problemów sieciowych oraz w analizie bezpieczeństwa.

## Użycie
Podstawowa składnia polecenia `tcpdump` jest następująca:

```bash
tcpdump [opcje] [argumenty]
```

## Częste opcje
- `-i <interfejs>`: Określa interfejs sieciowy do monitorowania.
- `-n`: Wyłącza rozwiązywanie nazw hostów, co przyspiesza działanie.
- `-c <liczba>`: Zatrzymuje przechwytywanie po określonej liczbie pakietów.
- `-w <plik>`: Zapisuje przechwycone pakiety do pliku.
- `-r <plik>`: Odczytuje pakiety z pliku.

## Częste przykłady
- Przechwytywanie pakietów na interfejsie `eth0`:
  ```bash
  tcpdump -i eth0
  ```

- Przechwytywanie tylko 10 pakietów:
  ```bash
  tcpdump -c 10
  ```

- Zapisanie przechwyconych pakietów do pliku `capture.pcap`:
  ```bash
  tcpdump -w capture.pcap
  ```

- Odczytanie pakietów z pliku `capture.pcap`:
  ```bash
  tcpdump -r capture.pcap
  ```

- Przechwytywanie pakietów HTTP (port 80):
  ```bash
  tcpdump -i eth0 port 80
  ```

## Wskazówki
- Używaj opcji `-n`, aby uniknąć opóźnień związanych z rozwiązywaniem nazw.
- Przechwytywanie dużej ilości pakietów może generować duże pliki, więc rozważ użycie opcji `-c` lub `-w`.
- Regularnie analizuj przechwycone dane, aby zidentyfikować potencjalne problemy z siecią lub zagrożenia bezpieczeństwa.