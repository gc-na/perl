# [Linux] C Shell (csh) netcat użycie: Narzędzie do komunikacji sieciowej

## Przegląd
Netcat, znany również jako "nc", to wszechstronne narzędzie do komunikacji sieciowej, które umożliwia przesyłanie danych przez protokoły TCP i UDP. Może być używane do różnych zadań, takich jak skanowanie portów, przesyłanie plików, czy jako prosty serwer.

## Użycie
Podstawowa składnia polecenia netcat wygląda następująco:

```csh
netcat [opcje] [argumenty]
```

## Często używane opcje
- `-l`: Uruchamia netcat w trybie nasłuchu (serwera).
- `-p [port]`: Określa port, na którym netcat ma nasłuchiwać lub łączyć się.
- `-u`: Używa protokołu UDP zamiast TCP.
- `-v`: Włącza tryb szczegółowy, wyświetlając dodatkowe informacje.
- `-w [czas]`: Ustala czas oczekiwania na odpowiedź.

## Przykłady
1. **Nasłuchiwanie na porcie 1234**:
   ```csh
   netcat -l -p 1234
   ```

2. **Łączenie się z serwerem na porcie 80**:
   ```csh
   netcat example.com 80
   ```

3. **Przesyłanie pliku**:
   Na serwerze:
   ```csh
   netcat -l -p 1234 > plik.txt
   ```
   Na kliencie:
   ```csh
   netcat [adres_serwera] 1234 < plik.txt
   ```

4. **Skanowanie portów**:
   ```csh
   netcat -z -v example.com 1-1000
   ```

## Wskazówki
- Używaj opcji `-v`, aby uzyskać więcej informacji podczas korzystania z netcat.
- Pamiętaj, aby zawsze sprawdzić, czy porty, które chcesz używać, są otwarte i dostępne.
- Netcat może być używany do testowania połączeń sieciowych, więc warto go mieć w swoim zestawie narzędzi.