# [Linux] C Shell (csh) cp Użycie: Kopiowanie plików i katalogów

## Overview
Polecenie `cp` w C Shell (csh) służy do kopiowania plików i katalogów. Umożliwia tworzenie kopii zapasowych lub przenoszenie danych w systemie plików.

## Usage
Podstawowa składnia polecenia `cp` jest następująca:

```csh
cp [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `cp`:

- `-i`: Pyta o potwierdzenie przed nadpisaniem istniejącego pliku.
- `-r`: Kopiuje katalogi rekurencyjnie.
- `-u`: Kopiuje tylko pliki, które są nowsze od istniejących plików docelowych lub gdy plik docelowy nie istnieje.
- `-v`: Wyświetla szczegóły dotyczące kopiowania plików.

## Common Examples
Poniżej znajdują się przykłady użycia polecenia `cp`:

1. Kopiowanie pojedynczego pliku:

   ```csh
   cp plik.txt kopia_plik.txt
   ```

2. Kopiowanie katalogu rekurencyjnie:

   ```csh
   cp -r katalog/ kopia_katalogu/
   ```

3. Kopiowanie pliku z potwierdzeniem przed nadpisaniem:

   ```csh
   cp -i plik.txt kopia_plik.txt
   ```

4. Kopiowanie tylko nowszych plików:

   ```csh
   cp -u plik.txt kopia_plik.txt
   ```

5. Wyświetlanie szczegółów podczas kopiowania:

   ```csh
   cp -v plik.txt kopia_plik.txt
   ```

## Tips
- Zawsze używaj opcji `-i`, gdy kopiujesz pliki do katalogów, w których mogą już istnieć pliki o tych samych nazwach, aby uniknąć przypadkowego nadpisania.
- Przy kopiowaniu dużych katalogów użyj opcji `-r`, aby upewnić się, że wszystkie podkatalogi i pliki zostaną skopiowane.
- Regularnie twórz kopie zapasowe ważnych plików, aby zabezpieczyć się przed ich utratą.