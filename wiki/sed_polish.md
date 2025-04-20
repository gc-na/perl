# [Linux] C Shell (csh) sed Użycie: Edytor strumieniowy tekstu

## Przegląd
Polecenie `sed` (stream editor) jest potężnym narzędziem do przetwarzania i edytowania tekstu w strumieniu. Umożliwia wykonywanie różnych operacji na plikach tekstowych, takich jak zamiana, usuwanie i wstawianie tekstu.

## Użycie
Podstawowa składnia polecenia `sed` wygląda następująco:

```bash
sed [opcje] [argumenty]
```

## Częste opcje
- `-e`: Umożliwia podanie wielu poleceń do wykonania.
- `-f`: Umożliwia wczytanie poleceń z pliku.
- `-i`: Edytuje plik w miejscu, bez tworzenia kopii.
- `-n`: Tylko wyświetla linie, które pasują do podanego wzorca.

## Częste przykłady
1. **Zamiana tekstu w pliku:**
   Zastąp wszystkie wystąpienia "stare" na "nowe" w pliku `plik.txt`.
   ```bash
   sed 's/stare/nowe/g' plik.txt
   ```

2. **Usunięcie linii zawierających wzorzec:**
   Usuń wszystkie linie, które zawierają "niepotrzebne" w pliku `plik.txt`.
   ```bash
   sed '/niepotrzebne/d' plik.txt
   ```

3. **Wstawienie tekstu przed określoną linią:**
   Wstaw "Witaj" przed drugą linią w pliku `plik.txt`.
   ```bash
   sed '2i Witaj' plik.txt
   ```

4. **Zapisanie zmian bezpośrednio w pliku:**
   Zastąp "stare" na "nowe" w pliku `plik.txt` i zapisz zmiany.
   ```bash
   sed -i 's/stare/nowe/g' plik.txt
   ```

## Wskazówki
- Zawsze wykonuj kopię zapasową plików przed użyciem opcji `-i`, aby uniknąć utraty danych.
- Używaj opcji `-n` w połączeniu z komendą `p`, aby wyświetlić tylko te linie, które chcesz zobaczyć.
- Testuj swoje polecenia na mniejszych plikach, aby upewnić się, że działają zgodnie z oczekiwaniami, zanim zastosujesz je do większych zbiorów danych.