# [Linux] C Shell (csh) curl użycie: Pobieranie i przesyłanie danych przez URL

## Przegląd
Polecenie `curl` służy do przesyłania danych do lub z serwera, korzystając z różnych protokołów, takich jak HTTP, HTTPS, FTP i wiele innych. Jest to narzędzie wiersza poleceń, które umożliwia łatwe pobieranie plików oraz interakcję z API.

## Użycie
Podstawowa składnia polecenia `curl` wygląda następująco:

```csh
curl [opcje] [argumenty]
```

## Często używane opcje
- `-O` - Pobiera plik i zapisuje go z oryginalną nazwą.
- `-o <nazwa_pliku>` - Pobiera plik i zapisuje go pod podaną nazwą.
- `-I` - Wysyła zapytanie HEAD i wyświetla nagłówki odpowiedzi.
- `-d <dane>` - Wysyła dane w żądaniu POST.
- `-H <nagłówek>` - Dodaje nagłówek do żądania.

## Przykłady
1. Pobieranie pliku z internetu i zapisanie go z oryginalną nazwą:
   ```csh
   curl -O http://example.com/plik.txt
   ```

2. Pobieranie pliku i zapisywanie go pod inną nazwą:
   ```csh
   curl -o nowa_nazwa.txt http://example.com/plik.txt
   ```

3. Wysyłanie zapytania HEAD, aby zobaczyć nagłówki odpowiedzi:
   ```csh
   curl -I http://example.com
   ```

4. Wysyłanie danych w żądaniu POST:
   ```csh
   curl -d "parametr1=wartość1&parametr2=wartość2" http://example.com/api
   ```

5. Dodawanie niestandardowego nagłówka do żądania:
   ```csh
   curl -H "Authorization: Bearer token" http://example.com/api
   ```

## Wskazówki
- Używaj opcji `-v`, aby uzyskać szczegółowe informacje o procesie żądania i odpowiedzi, co może pomóc w debugowaniu.
- Zawsze sprawdzaj dokumentację API, aby upewnić się, że używasz odpowiednich nagłówków i danych.
- Pamiętaj o używaniu opcji `-L`, jeśli chcesz, aby `curl` śledził przekierowania.