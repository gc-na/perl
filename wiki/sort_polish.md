# [Linux] C Shell (csh) sort użycie: sortowanie danych

## Overview
Polecenie `sort` w C Shell (csh) służy do sortowania linii tekstu w plikach lub danych wejściowych. Umożliwia uporządkowanie danych alfabetycznie lub numerycznie, co ułatwia ich analizę i przetwarzanie.

## Usage
Podstawowa składnia polecenia `sort` jest następująca:

```csh
sort [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `sort`:

- `-r` - sortowanie w odwrotnej kolejności (malejąco).
- `-n` - sortowanie numeryczne (zamiast alfabetycznego).
- `-k` - sortowanie według określonego klucza (np. kolumny).
- `-u` - usunięcie duplikatów z wyników sortowania.
- `-o` - zapisanie wyników sortowania do określonego pliku.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `sort`:

1. Sortowanie pliku tekstowego alfabetycznie:
   ```csh
   sort plik.txt
   ```

2. Sortowanie pliku numerycznie:
   ```csh
   sort -n liczby.txt
   ```

3. Sortowanie w odwrotnej kolejności:
   ```csh
   sort -r plik.txt
   ```

4. Sortowanie według drugiej kolumny:
   ```csh
   sort -k2 plik.txt
   ```

5. Zapisanie posortowanych danych do nowego pliku:
   ```csh
   sort plik.txt -o posortowany.txt
   ```

6. Usunięcie duplikatów z posortowanego pliku:
   ```csh
   sort -u plik.txt
   ```

## Tips
- Używaj opcji `-o`, aby bezpośrednio zapisać wyniki do pliku, co pozwala zaoszczędzić czas.
- W przypadku dużych plików, rozważ użycie opcji `-S`, aby określić ilość pamięci, którą `sort` może wykorzystać.
- Zawsze sprawdzaj wyniki sortowania, aby upewnić się, że dane są uporządkowane zgodnie z oczekiwaniami.