# [Linux] C Shell (csh) diff użycie: Porównywanie plików

## Overview
Polecenie `diff` służy do porównywania zawartości dwóch plików tekstowych. Umożliwia identyfikację różnic między nimi, co jest przydatne w wielu sytuacjach, takich jak przeglądanie zmian w kodzie źródłowym czy dokumentach.

## Usage
Podstawowa składnia polecenia `diff` jest następująca:

```
diff [opcje] [argumenty]
```

## Common Options
- `-u`: Wyświetla różnice w formacie z jedną linią kontekstu.
- `-c`: Wyświetla różnice w formacie kontekstowym.
- `-i`: Ignoruje różnice w wielkości liter.
- `-w`: Ignoruje różnice w białych znakach.
- `-r`: Porównuje katalogi rekurencyjnie.

## Common Examples
1. Porównanie dwóch plików tekstowych:
   ```csh
   diff plik1.txt plik2.txt
   ```

2. Porównanie plików z ignorowaniem wielkości liter:
   ```csh
   diff -i plik1.txt plik2.txt
   ```

3. Wyświetlenie różnic w formacie z jedną linią kontekstu:
   ```csh
   diff -u plik1.txt plik2.txt
   ```

4. Porównanie dwóch katalogów:
   ```csh
   diff -r katalog1/ katalog2/
   ```

## Tips
- Zawsze używaj opcji `-u` lub `-c`, aby uzyskać bardziej czytelne wyniki.
- Jeśli pracujesz z kodem źródłowym, rozważ użycie narzędzi takich jak `git diff`, które oferują bardziej zaawansowane funkcje.
- Regularnie porównuj pliki, aby śledzić zmiany i unikać konfliktów w projektach zespołowych.