# [Linux] C Shell (csh) cksum: obliczanie sum kontrolnych plików

## Overview
Polecenie `cksum` w powłoce C Shell (csh) służy do obliczania sum kontrolnych plików. Sumy kontrolne są używane do weryfikacji integralności danych, co pozwala na sprawdzenie, czy plik nie został zmieniony lub uszkodzony.

## Usage
Podstawowa składnia polecenia `cksum` jest następująca:

```csh
cksum [options] [arguments]
```

## Common Options
- `-a, --algorithm=ALG`: Określa algorytm używany do obliczania sumy kontrolnej.
- `-h, --help`: Wyświetla pomoc dotyczącą użycia polecenia.
- `-V, --version`: Wyświetla wersję programu.

## Common Examples
1. Obliczanie sumy kontrolnej dla pojedynczego pliku:
   ```csh
   cksum plik.txt
   ```

2. Obliczanie sum kontrolnych dla wielu plików:
   ```csh
   cksum plik1.txt plik2.txt plik3.txt
   ```

3. Użycie opcji do wyświetlenia wersji:
   ```csh
   cksum -V
   ```

4. Użycie opcji pomocy:
   ```csh
   cksum -h
   ```

## Tips
- Zawsze sprawdzaj sumy kontrolne po przesyłaniu plików, aby upewnić się, że nie zostały one uszkodzone.
- Możesz przekierować wyniki do pliku, aby zachować sumy kontrolne do późniejszego porównania:
  ```csh
  cksum plik.txt > suma.txt
  ```
- Używaj opcji `-a` do wyboru algorytmu, jeśli potrzebujesz specyficznego typu sumy kontrolnej.