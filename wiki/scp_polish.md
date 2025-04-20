# [Linux] C Shell (csh) scp użycie: Kopiowanie plików między hostami

## Overview
Polecenie `scp` (Secure Copy Protocol) służy do bezpiecznego kopiowania plików między lokalnym a zdalnym systemem lub między dwoma zdalnymi systemami. Używa protokołu SSH do zapewnienia bezpieczeństwa przesyłanych danych.

## Usage
Podstawowa składnia polecenia `scp` jest następująca:

```csh
scp [opcje] [źródło] [cel]
```

## Common Options
- `-r`: Kopiuj katalogi rekurencyjnie.
- `-P`: Określa port, na którym działa serwer SSH (z dużą literą P).
- `-p`: Zachowuje czas modyfikacji i uprawnienia plików.
- `-q`: Wyłącza wyjście komunikatów.
- `-C`: Włącza kompresję podczas transferu.

## Common Examples
1. Kopiowanie pliku z lokalnego systemu na zdalny serwer:
   ```csh
   scp lokalny_plik.txt użytkownik@zdalny_serwer:/ścieżka/do/katalogu/
   ```

2. Kopiowanie pliku z zdalnego serwera na lokalny system:
   ```csh
   scp użytkownik@zdalny_serwer:/ścieżka/do/zdalnego_pliku.txt /lokalna/ścieżka/
   ```

3. Kopiowanie katalogu z lokalnego systemu na zdalny serwer:
   ```csh
   scp -r lokalny_katalog/ użytkownik@zdalny_serwer:/ścieżka/do/katalogu/
   ```

4. Kopiowanie pliku z zdalnego serwera na inny zdalny serwer:
   ```csh
   scp użytkownik1@zdalny_serwer1:/ścieżka/do/pliku.txt użytkownik2@zdalny_serwer2:/ścieżka/do/katalogu/
   ```

## Tips
- Używaj opcji `-C`, aby przyspieszyć transfer dużych plików.
- Zawsze upewnij się, że masz odpowiednie uprawnienia do odczytu i zapisu w lokalizacji docelowej.
- Rozważ użycie kluczy SSH do uwierzytelniania, aby uniknąć wprowadzania hasła za każdym razem.