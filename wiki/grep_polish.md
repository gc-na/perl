# [Linux] C Shell (csh) grep użycie: Wyszukiwanie wzorców w plikach

## Overview
Polecenie `grep` służy do wyszukiwania wzorców w plikach tekstowych. Umożliwia użytkownikom znajdowanie linii, które pasują do określonego wyrażenia regularnego, co czyni je niezwykle przydatnym narzędziem w analizie danych i programowaniu.

## Usage
Podstawowa składnia polecenia `grep` wygląda następująco:

```csh
grep [opcje] [argumenty]
```

## Common Options
Oto kilka popularnych opcji, które można użyć z poleceniem `grep`:

- `-i` – ignoruje wielkość liter podczas wyszukiwania.
- `-v` – zwraca linie, które **nie** pasują do wzorca.
- `-r` – przeszukuje katalogi rekurencyjnie.
- `-n` – wyświetla numery linii, w których znaleziono dopasowanie.
- `-l` – wyświetla tylko nazwy plików, które zawierają dopasowanie.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `grep`:

1. Wyszukiwanie prostego wzorca w pliku:
   ```csh
   grep "szukany_wzorzec" plik.txt
   ```

2. Ignorowanie wielkości liter:
   ```csh
   grep -i "szukany_wzorzec" plik.txt
   ```

3. Wyszukiwanie wzorca w wielu plikach:
   ```csh
   grep "szukany_wzorzec" *.txt
   ```

4. Wyszukiwanie wzorca rekurencyjnie w katalogu:
   ```csh
   grep -r "szukany_wzorzec" /ścieżka/do/katalogu
   ```

5. Wyświetlanie numerów linii z dopasowaniami:
   ```csh
   grep -n "szukany_wzorzec" plik.txt
   ```

## Tips
- Używaj opcji `-i`, gdy nie jesteś pewien wielkości liter w wyszukiwanym wzorcu.
- Opcja `-v` jest przydatna, gdy chcesz znaleźć linie, które nie zawierają określonego wzorca.
- Zawsze sprawdzaj dokumentację (`man grep`), aby poznać więcej opcji i możliwości tego polecenia.