# [Linux] C Shell (csh) nslookup użycie: Sprawdzanie adresów IP i nazw domen

## Przegląd
Polecenie `nslookup` służy do zapytania systemu DNS w celu uzyskania informacji o adresach IP i nazwach domen. Umożliwia użytkownikom sprawdzanie, jakie adresy IP są przypisane do danej nazwy domeny oraz odwrotnie.

## Użycie
Podstawowa składnia polecenia `nslookup` jest następująca:

```
nslookup [opcje] [argumenty]
```

## Częste opcje
- `-type=typ`: Określa typ zapytania, np. A (adres IPv4), AAAA (adres IPv6), MX (rekordy poczty).
- `-timeout=n`: Ustala czas oczekiwania na odpowiedź w sekundach.
- `-debug`: Włącza tryb debugowania, co pozwala na uzyskanie dodatkowych informacji o zapytaniach.

## Częste przykłady
1. Sprawdzenie adresu IP dla danej nazwy domeny:
   ```csh
   nslookup example.com
   ```

2. Uzyskanie rekordów MX dla domeny:
   ```csh
   nslookup -type=MX example.com
   ```

3. Sprawdzenie adresu IP dla subdomeny:
   ```csh
   nslookup sub.example.com
   ```

4. Ustawienie serwera DNS do użycia:
   ```csh
   nslookup example.com 8.8.8.8
   ```

## Wskazówki
- Używaj opcji `-debug`, aby uzyskać więcej informacji podczas rozwiązywania problemów z DNS.
- Pamiętaj, że wyniki mogą się różnić w zależności od używanego serwera DNS.
- Regularnie sprawdzaj rekordy DNS, aby upewnić się, że są aktualne i poprawne.