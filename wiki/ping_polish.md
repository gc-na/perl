# [Linux] C Shell (csh) ping użycie: Sprawdzenie dostępności hosta

## Overview
Polecenie `ping` służy do sprawdzania dostępności hosta w sieci. Wysyła pakiety ICMP Echo Request do określonego adresu IP lub nazwy hosta i oczekuje na odpowiedź. Jest to przydatne narzędzie do diagnozowania problemów z połączeniem sieciowym.

## Usage
Podstawowa składnia polecenia `ping` jest następująca:

```csh
ping [opcje] [argumenty]
```

## Common Options
- `-c <liczba>`: Określa liczbę wysyłanych pakietów.
- `-i <czas>`: Ustala czas w sekundach między wysyłanymi pakietami.
- `-s <rozmiar>`: Ustala rozmiar wysyłanych pakietów w bajtach.
- `-t <TTL>`: Ustala wartość Time To Live dla pakietów.

## Common Examples
1. Sprawdzenie dostępności hosta:
   ```csh
   ping example.com
   ```

2. Wysłanie 5 pakietów:
   ```csh
   ping -c 5 example.com
   ```

3. Ustalenie rozmiaru pakietu na 128 bajtów:
   ```csh
   ping -s 128 example.com
   ```

4. Ustalenie interwału między pakietami na 2 sekundy:
   ```csh
   ping -i 2 example.com
   ```

5. Ustalenie wartości TTL na 64:
   ```csh
   ping -t 64 example.com
   ```

## Tips
- Użyj opcji `-c` w celu ograniczenia liczby wysyłanych pakietów, co jest przydatne, gdy chcesz szybko sprawdzić połączenie.
- Monitoruj czas odpowiedzi, aby ocenić jakość połączenia.
- Jeśli nie otrzymujesz odpowiedzi, sprawdź, czy adres IP jest poprawny oraz czy masz dostęp do sieci.