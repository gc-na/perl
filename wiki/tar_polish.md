# [Linux] C Shell (csh) tar Użycie: Narzędzie do archiwizacji plików

## Overview
Polecenie `tar` (tape archive) służy do tworzenia archiwów plików oraz ich rozpakowywania. Jest powszechnie używane do kompresji i przenoszenia wielu plików w jednym pliku archiwum.

## Usage
Podstawowa składnia polecenia `tar` jest następująca:

```csh
tar [opcje] [argumenty]
```

## Common Options
- `-c`: Tworzy nowe archiwum.
- `-x`: Rozpakowuje archiwum.
- `-f`: Określa nazwę pliku archiwum.
- `-v`: Wyświetla szczegóły operacji (verbose).
- `-z`: Kompresuje archiwum za pomocą gzip.
- `-j`: Kompresuje archiwum za pomocą bzip2.

## Common Examples
1. Tworzenie archiwum:
   ```csh
   tar -cvf archiwum.tar /ścieżka/do/katalogu
   ```

2. Rozpakowywanie archiwum:
   ```csh
   tar -xvf archiwum.tar
   ```

3. Tworzenie skompresowanego archiwum gzip:
   ```csh
   tar -czvf archiwum.tar.gz /ścieżka/do/katalogu
   ```

4. Rozpakowywanie skompresowanego archiwum gzip:
   ```csh
   tar -xzvf archiwum.tar.gz
   ```

5. Tworzenie archiwum bzip2:
   ```csh
   tar -cjvf archiwum.tar.bz2 /ścieżka/do/katalogu
   ```

6. Rozpakowywanie archiwum bzip2:
   ```csh
   tar -xjvf archiwum.tar.bz2
   ```

## Tips
- Zawsze sprawdzaj zawartość archiwum przed rozpakowaniem, używając opcji `-t`:
  ```csh
  tar -tvf archiwum.tar
  ```
- Używaj opcji `-v`, aby zobaczyć, które pliki są przetwarzane, co może być przydatne w przypadku dużych archiwów.
- Regularnie twórz kopie zapasowe ważnych danych, używając `tar`, aby uniknąć ich utraty.