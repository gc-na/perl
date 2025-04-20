# [Linux] C Shell (csh) socat użycie: Narzędzie do przesyłania danych między dwoma punktami

## Przegląd
`socat` to potężne narzędzie w systemie Linux, które umożliwia przesyłanie danych między różnymi punktami, takimi jak gniazda, pliki, czy urządzenia. Działa jako most, który łączy różne źródła danych, co czyni go niezwykle przydatnym w różnych scenariuszach sieciowych i systemowych.

## Użycie
Podstawowa składnia polecenia `socat` wygląda następująco:

```csh
socat [opcje] [argumenty]
```

## Często używane opcje
- `-d` : Włącza tryb debugowania, wyświetlając dodatkowe informacje o działaniu polecenia.
- `-v` : Włącza tryb verbose, który pokazuje więcej szczegółów o przesyłanych danych.
- `-u` : Umożliwia otwarcie gniazda w trybie tylko do odczytu.
- `-b` : Ustawia rozmiar bufora dla przesyłanych danych.

## Przykłady
Oto kilka praktycznych przykładów użycia `socat`:

1. **Przesyłanie danych z jednego gniazda do drugiego:**

```csh
socat TCP-LISTEN:1234,fork TCP:localhost:5678
```

2. **Przesyłanie danych z pliku do gniazda:**

```csh
socat -u FILE:/path/to/file.txt TCP:localhost:1234
```

3. **Łączenie dwóch gniazd TCP:**

```csh
socat TCP:host1:port1 TCP:host2:port2
```

4. **Przesyłanie danych z urządzenia szeregowego do gniazda:**

```csh
socat -u /dev/ttyS0 TCP:localhost:1234
```

## Wskazówki
- Używaj opcji `-d` i `-v` podczas testowania, aby uzyskać więcej informacji o działaniu `socat`.
- Zawsze sprawdzaj, czy porty, które chcesz użyć, są dostępne i nie są zajęte przez inne procesy.
- Zwracaj uwagę na uprawnienia do plików i urządzeń, aby uniknąć problemów z dostępem.