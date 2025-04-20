# [Linux] C Shell (csh) unzip użycie: Rozpakowywanie plików ZIP

## Overview
Polecenie `unzip` służy do rozpakowywania plików archiwów ZIP. Umożliwia użytkownikom wydobycie zawartości archiwów, co jest przydatne w przypadku pobierania plików z internetu lub pracy z pakietami oprogramowania.

## Usage
Podstawowa składnia polecenia `unzip` jest następująca:

```csh
unzip [opcje] [argumenty]
```

## Common Options
- `-l`: Wyświetla listę plików w archiwum ZIP bez ich rozpakowywania.
- `-d [katalog]`: Rozpakowuje pliki do określonego katalogu.
- `-o`: Nadpisuje istniejące pliki bez pytania o potwierdzenie.
- `-q`: Wykonuje operację w trybie cichym, bez wyświetlania komunikatów.

## Common Examples
1. Rozpakowanie pliku ZIP do bieżącego katalogu:
   ```csh
   unzip plik.zip
   ```

2. Rozpakowanie pliku ZIP do określonego katalogu:
   ```csh
   unzip plik.zip -d /ścieżka/do/katalogu
   ```

3. Wyświetlenie listy plików w archiwum ZIP:
   ```csh
   unzip -l plik.zip
   ```

4. Rozpakowanie pliku ZIP i nadpisanie istniejących plików:
   ```csh
   unzip -o plik.zip
   ```

## Tips
- Zawsze sprawdzaj zawartość archiwum za pomocą opcji `-l`, zanim je rozpakujesz, aby upewnić się, że nie nadpiszesz ważnych plików.
- Używaj opcji `-d`, aby zorganizować rozpakowane pliki w dedykowanym katalogu, co ułatwi zarządzanie nimi.
- W trybie cichym (`-q`) możesz używać `unzip` w skryptach, aby uniknąć zbędnych komunikatów.