# [Linux] C Shell (csh) find użycie: znajdowanie nazw plików

## Overview
Polecenie `find` w C Shell (csh) służy do wyszukiwania plików i katalogów w hierarchii systemu plików. Umożliwia użytkownikom lokalizowanie plików na podstawie różnych kryteriów, takich jak nazwa, typ, rozmiar czy data modyfikacji.

## Usage
Podstawowa składnia polecenia `find` jest następująca:

```csh
find [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji polecenia `find`:

- `-name <nazwa>`: Wyszukuje pliki o podanej nazwie.
- `-type <typ>`: Filtruje wyniki według typu pliku (np. `f` dla plików, `d` dla katalogów).
- `-size <rozmiar>`: Wyszukuje pliki o określonym rozmiarze.
- `-mtime <dni>`: Znajduje pliki zmodyfikowane w ciągu ostatnich dni.
- `-exec <polecenie> {} \;`: Wykonuje określone polecenie na każdym znalezionym pliku.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `find`:

1. Wyszukiwanie plików o nazwie `example.txt` w bieżącym katalogu i podkatalogach:

   ```csh
   find . -name "example.txt"
   ```

2. Wyszukiwanie wszystkich katalogów w systemie:

   ```csh
   find / -type d
   ```

3. Wyszukiwanie plików większych niż 1 MB w bieżącym katalogu:

   ```csh
   find . -size +1M
   ```

4. Wyszukiwanie plików zmodyfikowanych w ciągu ostatnich 7 dni:

   ```csh
   find . -mtime -7
   ```

5. Usuwanie wszystkich plików tymczasowych z rozszerzeniem `.tmp`:

   ```csh
   find . -name "*.tmp" -exec rm {} \;
   ```

## Tips
- Używaj opcji `-print` na końcu, aby wyświetlić wyniki w czytelny sposób, jeśli nie używasz `-exec`.
- Zawsze testuj polecenia `find` z opcją `-print`, zanim użyjesz `-exec`, aby uniknąć przypadkowego usunięcia lub zmodyfikowania plików.
- Możesz łączyć różne opcje, aby precyzyjniej określić kryteria wyszukiwania, co zwiększa efektywność polecenia.