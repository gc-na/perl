# [Linux] C Shell (csh) gunzip użycie: Rozpakowywanie plików gzip

## Overview
Polecenie `gunzip` służy do dekompresji plików skompresowanych za pomocą algorytmu gzip. Umożliwia użytkownikom przywrócenie oryginalnych plików z formatu .gz.

## Usage
Podstawowa składnia polecenia `gunzip` jest następująca:

```csh
gunzip [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `gunzip`:

- `-c`: Wyświetla dekompresowane dane na standardowym wyjściu, zamiast zapisywać je do pliku.
- `-f`: Wymusza dekompresję, nawet jeśli plik docelowy już istnieje.
- `-k`: Zachowuje oryginalny plik .gz po dekompresji.
- `-r`: Rekursywnie dekompresuje pliki w podkatalogach.

## Common Examples
Oto kilka praktycznych przykładów użycia `gunzip`:

1. Dekompresja pojedynczego pliku:
   ```csh
   gunzip plik.txt.gz
   ```

2. Dekompresja z zachowaniem oryginalnego pliku:
   ```csh
   gunzip -k plik.txt.gz
   ```

3. Wyświetlenie dekompresowanych danych na standardowym wyjściu:
   ```csh
   gunzip -c plik.txt.gz
   ```

4. Rekursywna dekompresja plików w katalogu:
   ```csh
   gunzip -r katalog/
   ```

## Tips
- Używaj opcji `-k`, jeśli chcesz zachować oryginalne pliki skompresowane.
- Zawsze sprawdzaj, czy masz odpowiednie uprawnienia do zapisu w katalogu, w którym chcesz dekompresować pliki.
- Możesz użyć `gunzip` w połączeniu z innymi poleceniami, aby efektywnie zarządzać plikami w skryptach.