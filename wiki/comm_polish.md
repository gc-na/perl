# [Linux] C Shell (csh) comm: Porównywanie linii w plikach

## Overview
Polecenie `comm` w C Shell (csh) służy do porównywania dwóch posortowanych plików tekstowych i wyświetlania linii, które są wspólne, unikalne dla każdego z plików oraz różnice między nimi.

## Usage
Podstawowa składnia polecenia `comm` jest następująca:

```csh
comm [opcje] [argumenty]
```

## Common Options
- `-1`: Ukrywa linie, które są unikalne dla pierwszego pliku.
- `-2`: Ukrywa linie, które są unikalne dla drugiego pliku.
- `-3`: Ukrywa linie, które są wspólne dla obu plików.
- `-i`: Ignoruje wielkość liter podczas porównywania linii.

## Common Examples
Przykłady użycia polecenia `comm`:

1. Porównanie dwóch plików i wyświetlenie wszystkich linii:
   ```csh
   comm file1.txt file2.txt
   ```

2. Wyświetlenie tylko linii unikalnych dla pierwszego pliku:
   ```csh
   comm -13 file1.txt file2.txt
   ```

3. Wyświetlenie tylko linii unikalnych dla drugiego pliku:
   ```csh
   comm -12 file1.txt file2.txt
   ```

4. Porównanie dwóch plików z ignorowaniem wielkości liter:
   ```csh
   comm -i file1.txt file2.txt
   ```

## Tips
- Upewnij się, że pliki są posortowane przed użyciem `comm`, aby uzyskać poprawne wyniki.
- Możesz użyć polecenia `sort` w połączeniu z `comm`, aby automatycznie posortować pliki:
  ```csh
  comm <(sort file1.txt) <(sort file2.txt)
  ```
- Eksperymentuj z różnymi opcjami, aby dostosować wyniki do swoich potrzeb.