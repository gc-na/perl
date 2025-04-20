# [Linux] C Shell (csh) rm użycie: Usuwanie plików i katalogów

## Overview
Polecenie `rm` w C Shell (csh) służy do usuwania plików i katalogów. Umożliwia użytkownikom usunięcie niepotrzebnych plików z systemu, co jest przydatne w zarządzaniu przestrzenią dyskową.

## Usage
Podstawowa składnia polecenia `rm` jest następująca:

```
rm [opcje] [argumenty]
```

## Common Options
- `-f` : Wymusza usunięcie plików bez potwierdzenia.
- `-i` : Pyta o potwierdzenie przed usunięciem każdego pliku.
- `-r` : Usuwa katalogi oraz ich zawartość rekurencyjnie.
- `-v` : Wyświetla szczegóły dotyczące usuwanych plików.

## Common Examples
- Usunięcie pojedynczego pliku:
  ```csh
  rm plik.txt
  ```

- Usunięcie wielu plików:
  ```csh
  rm plik1.txt plik2.txt plik3.txt
  ```

- Wymuszenie usunięcia pliku bez potwierdzenia:
  ```csh
  rm -f plik.txt
  ```

- Usunięcie katalogu oraz jego zawartości:
  ```csh
  rm -r katalog/
  ```

- Usunięcie pliku z potwierdzeniem:
  ```csh
  rm -i plik.txt
  ```

## Tips
- Zawsze sprawdzaj, które pliki chcesz usunąć, aby uniknąć przypadkowego usunięcia ważnych danych.
- Używaj opcji `-i`, gdy nie jesteś pewien, czy chcesz usunąć dany plik.
- Rozważ użycie polecenia `ls` przed `rm`, aby upewnić się, że usuwasz właściwe pliki.