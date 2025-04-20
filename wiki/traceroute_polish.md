# [Linux] C Shell (csh) traceroute użycie: śledzenie trasy pakietów sieciowych

## Overview
Polecenie `traceroute` służy do śledzenia trasy, jaką pokonują pakiety danych w sieci, od źródła do celu. Umożliwia to zrozumienie, przez jakie węzły przechodzą dane oraz identyfikację potencjalnych problemów z połączeniem.

## Usage
Podstawowa składnia polecenia `traceroute` jest następująca:

```csh
traceroute [opcje] [argumenty]
```

## Common Options
- `-m <liczba>`: Ustala maksymalną liczbę skoków (hops), które mają być śledzone.
- `-n`: Nie rozwiązuje nazw hostów, wyświetla jedynie adresy IP.
- `-w <czas>`: Ustala czas oczekiwania na odpowiedź w sekundach.
- `-q <liczba>`: Ustala liczbę zapytań wysyłanych do każdego węzła.

## Common Examples
1. Śledzenie trasy do określonego hosta:
   ```csh
   traceroute example.com
   ```

2. Śledzenie trasy z maksymalną liczbą skoków ustawioną na 15:
   ```csh
   traceroute -m 15 example.com
   ```

3. Śledzenie trasy bez rozwiązywania nazw hostów:
   ```csh
   traceroute -n example.com
   ```

4. Ustalenie czasu oczekiwania na odpowiedź na 2 sekundy:
   ```csh
   traceroute -w 2 example.com
   ```

5. Wysyłanie 3 zapytań do każdego węzła:
   ```csh
   traceroute -q 3 example.com
   ```

## Tips
- Używaj opcji `-n`, gdy chcesz szybko uzyskać wyniki bez opóźnienia spowodowanego rozwiązywaniem nazw hostów.
- Monitoruj wyniki, aby zidentyfikować, gdzie mogą występować problemy w sieci.
- Zwracaj uwagę na czas odpowiedzi dla każdego skoku, aby ocenić wydajność połączenia.