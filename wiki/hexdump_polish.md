# [Linux] C Shell (csh) hexdump użycie: wyświetlanie danych w formacie szesnastkowym

## Overview
Polecenie `hexdump` służy do wyświetlania zawartości plików w formacie szesnastkowym. Umożliwia analizę danych binarnych, co jest przydatne w programowaniu i debugowaniu.

## Usage
Podstawowa składnia polecenia `hexdump` jest następująca:

```csh
hexdump [options] [arguments]
```

## Common Options
- `-C` - Wyświetla dane w formacie szesnastkowym z ASCII po prawej stronie.
- `-n N` - Odczytuje tylko pierwsze N bajtów z pliku.
- `-v` - Wyświetla wszystkie dane, w tym powtarzające się bajty.
- `-e FORMAT` - Umożliwia zdefiniowanie własnego formatu wyjścia.

## Common Examples
Przykłady użycia polecenia `hexdump`:

1. Wyświetlenie zawartości pliku w formacie szesnastkowym:
   ```csh
   hexdump myfile.bin
   ```

2. Wyświetlenie pierwszych 16 bajtów pliku:
   ```csh
   hexdump -n 16 myfile.bin
   ```

3. Wyświetlenie danych w formacie szesnastkowym z ASCII:
   ```csh
   hexdump -C myfile.bin
   ```

4. Użycie własnego formatu wyjścia:
   ```csh
   hexdump -e '1/1 "%02x " "\n"' myfile.bin
   ```

## Tips
- Używaj opcji `-C`, aby łatwiej analizować dane, zwłaszcza gdy interesuje Cię ich reprezentacja tekstowa.
- Zawsze sprawdzaj, czy plik, który analizujesz, nie jest zbyt duży, aby uniknąć przeciążenia terminala.
- Eksperymentuj z różnymi formatami wyjścia, aby dostosować prezentację danych do swoich potrzeb.