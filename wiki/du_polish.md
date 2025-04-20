# [Linux] C Shell (csh) du użycie: Sprawdza rozmiar plików i katalogów

## Overview
Polecenie `du` (disk usage) służy do wyświetlania informacji o rozmiarze plików i katalogów w systemie plików. Umożliwia użytkownikom zrozumienie, ile miejsca zajmują różne pliki i foldery.

## Usage
Podstawowa składnia polecenia `du` wygląda następująco:

```csh
du [opcje] [argumenty]
```

## Common Options
- `-h`: Wyświetla rozmiary w formacie czytelnym dla człowieka (np. KB, MB).
- `-s`: Podsumowuje rozmiar dla każdego argumentu, zamiast wyświetlać rozmiary dla wszystkich podkatalogów.
- `-a`: Wyświetla rozmiary dla wszystkich plików, nie tylko katalogów.
- `-c`: Dodaje podsumowanie całkowitego rozmiaru na końcu.

## Common Examples
- Aby wyświetlić rozmiar katalogu w formacie czytelnym dla człowieka:
  ```csh
  du -h /ścieżka/do/katalogu
  ```

- Aby uzyskać podsumowanie rozmiaru katalogu:
  ```csh
  du -sh /ścieżka/do/katalogu
  ```

- Aby wyświetlić rozmiary wszystkich plików i katalogów w bieżącym katalogu:
  ```csh
  du -ah .
  ```

- Aby uzyskać całkowity rozmiar wszystkich plików i katalogów w bieżącym katalogu:
  ```csh
  du -ch .
  ```

## Tips
- Używaj opcji `-h`, aby łatwiej interpretować rozmiary plików.
- Opcja `-s` jest przydatna, gdy chcesz szybko sprawdzić rozmiar głównego katalogu bez szczegółowych informacji o podkatalogach.
- Regularnie sprawdzaj rozmiary katalogów, aby zarządzać przestrzenią dyskową w systemie.