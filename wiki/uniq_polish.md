# [Linux] C Shell (csh) uniq Użycie: Usuwa duplikaty z pliku

## Overview
Polecenie `uniq` w C Shell (csh) służy do usuwania duplikatów z posortowanej listy linii w pliku lub z danych wejściowych. Dzięki temu można łatwo uzyskać unikalne wpisy z zestawu danych.

## Usage
Podstawowa składnia polecenia `uniq` jest następująca:

```
uniq [opcje] [argumenty]
```

## Common Options
- `-c`: Zlicza wystąpienia każdej unikalnej linii i wyświetla je przed linią.
- `-d`: Wyświetla tylko linie, które są duplikatami.
- `-u`: Wyświetla tylko linie, które są unikalne (niepowtarzające się).
- `-i`: Ignoruje wielkość liter podczas porównywania linii.

## Common Examples
1. Usunięcie duplikatów z pliku:
   ```csh
   uniq plik.txt
   ```

2. Zliczanie wystąpień każdej unikalnej linii:
   ```csh
   uniq -c plik.txt
   ```

3. Wyświetlenie tylko duplikatów:
   ```csh
   uniq -d plik.txt
   ```

4. Ignorowanie wielkości liter:
   ```csh
   uniq -i plik.txt
   ```

## Tips
- Upewnij się, że dane są posortowane przed użyciem `uniq`, aby uzyskać poprawne wyniki.
- Możesz użyć `sort` w połączeniu z `uniq`, aby najpierw posortować dane:
  ```csh
  sort plik.txt | uniq
  ```
- Jeśli pracujesz z dużymi plikami, rozważ użycie opcji `-u` lub `-d`, aby szybko znaleźć unikalne lub duplikujące się linie.