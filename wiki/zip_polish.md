# [Linux] C Shell (csh) zip użycie: Kompresja plików

## Overview
Polecenie `zip` służy do kompresji plików i folderów w celu zaoszczędzenia miejsca na dysku lub ułatwienia ich przesyłania. Tworzy archiwa w formacie ZIP, które są powszechnie używane w systemach operacyjnych.

## Usage
Podstawowa składnia polecenia `zip` jest następująca:

```
zip [opcje] [argumenty]
```

## Common Options
- `-r`: Rekursywnie kompresuje foldery i ich zawartość.
- `-e`: Tworzy zaszyfrowane archiwum ZIP.
- `-u`: Aktualizuje istniejące pliki w archiwum.
- `-d`: Usuwa pliki z archiwum ZIP.

## Common Examples
1. Kompresja pojedynczego pliku:
   ```bash
   zip archiwum.zip plik.txt
   ```

2. Kompresja wielu plików:
   ```bash
   zip archiwum.zip plik1.txt plik2.txt plik3.txt
   ```

3. Rekursywna kompresja folderu:
   ```bash
   zip -r archiwum.zip folder/
   ```

4. Tworzenie zaszyfrowanego archiwum:
   ```bash
   zip -e archiwum.zip plik.txt
   ```

5. Aktualizacja plików w archiwum:
   ```bash
   zip -u archiwum.zip plik_nowy.txt
   ```

6. Usuwanie pliku z archiwum:
   ```bash
   zip -d archiwum.zip plik_do_usuniecia.txt
   ```

## Tips
- Używaj opcji `-r`, gdy chcesz skompresować całe foldery, aby nie pominąć żadnych plików.
- Zawsze sprawdzaj zawartość archiwum za pomocą polecenia `unzip -l archiwum.zip`, aby upewnić się, że wszystkie pliki zostały poprawnie skompresowane.
- Pamiętaj o używaniu opcji `-e`, gdy potrzebujesz dodatkowego zabezpieczenia dla wrażliwych danych.