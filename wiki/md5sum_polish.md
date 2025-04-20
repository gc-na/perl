# [Linux] C Shell (csh) md5sum użycie: Obliczanie sum kontrolnych MD5

## Overview
Polecenie `md5sum` służy do obliczania i weryfikacji sum kontrolnych MD5 dla plików. Jest to przydatne narzędzie do sprawdzania integralności danych, ponieważ pozwala na porównanie sum kontrolnych plików w celu wykrycia ewentualnych zmian lub uszkodzeń.

## Usage
Podstawowa składnia polecenia `md5sum` jest następująca:

```csh
md5sum [opcje] [argumenty]
```

## Common Options
- `-b`: Oblicza sumę kontrolną dla plików binarnych.
- `-c`: Sprawdza sumy kontrolne z pliku.
- `-t`: Oblicza sumę kontrolną dla danych tekstowych.
- `--help`: Wyświetla pomoc dotyczącą użycia polecenia.

## Common Examples
1. Obliczanie sumy kontrolnej dla pojedynczego pliku:
   ```csh
   md5sum plik.txt
   ```

2. Obliczanie sumy kontrolnej dla wielu plików:
   ```csh
   md5sum plik1.txt plik2.txt
   ```

3. Zapis sum kontrolnych do pliku:
   ```csh
   md5sum plik.txt > suma.md5
   ```

4. Sprawdzanie sum kontrolnych z pliku:
   ```csh
   md5sum -c suma.md5
   ```

## Tips
- Zawsze zapisuj sumy kontrolne do pliku, aby móc je później zweryfikować.
- Używaj opcji `-b` dla plików binarnych, aby uzyskać dokładne wyniki.
- Regularnie sprawdzaj sumy kontrolne ważnych plików, aby zapewnić ich integralność.