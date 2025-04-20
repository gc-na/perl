# [Linux] C Shell (csh) head użycie: wyświetlanie pierwszych linii pliku

## Przegląd
Polecenie `head` w C Shell (csh) służy do wyświetlania pierwszych kilku linii pliku tekstowego. Jest to przydatne narzędzie, gdy chcesz szybko zobaczyć zawartość pliku bez otwierania go w pełni.

## Użycie
Podstawowa składnia polecenia `head` jest następująca:

```
head [opcje] [argumenty]
```

## Częste opcje
- `-n [liczba]`: Określa liczbę linii do wyświetlenia. Domyślnie wyświetlane jest 10 linii.
- `-q`: Nie wyświetla nagłówków plików, gdy podano więcej niż jeden plik.
- `-v`: Zawsze wyświetla nagłówki plików, nawet gdy jest tylko jeden plik.

## Częste przykłady
1. Wyświetlenie pierwszych 10 linii pliku `plik.txt`:
   ```csh
   head plik.txt
   ```

2. Wyświetlenie pierwszych 5 linii pliku `dane.txt`:
   ```csh
   head -n 5 dane.txt
   ```

3. Wyświetlenie pierwszych 15 linii z pliku `log.txt`, z nagłówkiem:
   ```csh
   head -n 15 -v log.txt
   ```

4. Wyświetlenie pierwszych 10 linii z dwóch plików `plik1.txt` i `plik2.txt`, bez nagłówków:
   ```csh
   head -q plik1.txt plik2.txt
   ```

## Wskazówki
- Używaj opcji `-n`, aby dostosować liczbę wyświetlanych linii do swoich potrzeb.
- Jeśli pracujesz z dużymi plikami, `head` pozwala na szybkie uzyskanie wglądu w ich zawartość.
- Możesz łączyć `head` z innymi poleceniami, używając potoków, aby na przykład wyświetlić pierwsze linie wyników innego polecenia.