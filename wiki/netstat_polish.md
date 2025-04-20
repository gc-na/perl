# [Linux] C Shell (csh) netstat Użycie: wyświetlanie informacji o połączeniach sieciowych

## Przegląd
Polecenie `netstat` służy do wyświetlania informacji o połączeniach sieciowych, tabel routingu oraz statystyk interfejsów sieciowych. Umożliwia monitorowanie aktywnych połączeń oraz diagnozowanie problemów z siecią.

## Użycie
Podstawowa składnia polecenia `netstat` jest następująca:

```
netstat [opcje] [argumenty]
```

## Częste opcje
- `-a` – wyświetla wszystkie połączenia i porty nasłuchujące.
- `-t` – pokazuje tylko połączenia TCP.
- `-u` – pokazuje tylko połączenia UDP.
- `-n` – wyświetla adresy IP i numery portów w formie numerycznej, zamiast nazw.
- `-r` – wyświetla tabelę routingu.

## Przykłady
1. Wyświetlenie wszystkich aktywnych połączeń:
   ```csh
   netstat -a
   ```

2. Wyświetlenie tylko połączeń TCP:
   ```csh
   netstat -t
   ```

3. Wyświetlenie połączeń UDP z adresami w formie numerycznej:
   ```csh
   netstat -un
   ```

4. Wyświetlenie tabeli routingu:
   ```csh
   netstat -r
   ```

## Wskazówki
- Używaj opcji `-n`, aby przyspieszyć wyświetlanie wyników, unikając rozwiązywania nazw hostów.
- Regularnie monitoruj połączenia sieciowe, aby wykrywać nieautoryzowane połączenia.
- Łącz opcje, aby uzyskać bardziej szczegółowe informacje, na przykład `netstat -tun` dla połączeń TCP i UDP w formie numerycznej.