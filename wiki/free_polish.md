# [Linux] C Shell (csh) free użycie: wyświetlanie informacji o pamięci

## Overview
Polecenie `free` w systemie Linux służy do wyświetlania informacji o użyciu pamięci w systemie. Pokazuje ilość pamięci RAM oraz pamięci wymiany (swap), a także ich wykorzystanie przez różne procesy.

## Usage
Podstawowa składnia polecenia `free` jest następująca:

```csh
free [options] [arguments]
```

## Common Options
- `-h` : Wyświetla wartości w formacie czytelnym dla człowieka (np. MB, GB).
- `-m` : Wyświetla wartości w megabajtach.
- `-g` : Wyświetla wartości w gigabajtach.
- `-s [sekundy]` : Powtarza wyświetlanie co określoną liczbę sekund.
- `-t` : Wyświetla całkowitą ilość pamięci (RAM + swap).

## Common Examples
1. Wyświetlenie podstawowych informacji o pamięci:
    ```csh
    free
    ```

2. Wyświetlenie informacji w formacie czytelnym dla człowieka:
    ```csh
    free -h
    ```

3. Wyświetlenie pamięci w megabajtach:
    ```csh
    free -m
    ```

4. Powtarzanie wyświetlania co 5 sekund:
    ```csh
    free -s 5
    ```

5. Wyświetlenie całkowitej ilości pamięci:
    ```csh
    free -t
    ```

## Tips
- Używaj opcji `-h`, aby łatwiej zrozumieć wyniki, zwłaszcza w systemach z dużą ilością pamięci.
- Regularne monitorowanie pamięci może pomóc w identyfikacji problemów z wydajnością systemu.
- Możesz używać `free` w skryptach, aby automatycznie zbierać dane o pamięci w określonych odstępach czasu.