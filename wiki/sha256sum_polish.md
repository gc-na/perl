# [Linux] C Shell (csh) sha256sum użycie: Obliczanie sumy kontrolnej SHA-256

## Przegląd
Polecenie `sha256sum` służy do obliczania sum kontrolnych SHA-256 dla plików. Jest to przydatne narzędzie do weryfikacji integralności danych, umożliwiające sprawdzenie, czy plik nie został zmieniony.

## Użycie
Podstawowa składnia polecenia `sha256sum` jest następująca:

```csh
sha256sum [opcje] [argumenty]
```

## Częste opcje
- `-b` – oblicza sumę kontrolną dla plików binarnych.
- `-c` – sprawdza sumy kontrolne z pliku.
- `-o` – zapisuje wynik do określonego pliku.
- `--help` – wyświetla pomoc dotycząca użycia polecenia.

## Przykłady
1. Obliczanie sumy kontrolnej dla pliku:
   ```csh
   sha256sum plik.txt
   ```

2. Zapis sumy kontrolnej do pliku:
   ```csh
   sha256sum plik.txt > suma.txt
   ```

3. Sprawdzanie sum kontrolnych z pliku:
   ```csh
   sha256sum -c suma.txt
   ```

4. Obliczanie sumy kontrolnej dla pliku binarnego:
   ```csh
   sha256sum -b plik.bin
   ```

## Wskazówki
- Zawsze zapisuj sumy kontrolne w osobnym pliku, aby móc je później wykorzystać do weryfikacji.
- Używaj opcji `-c`, aby szybko sprawdzić integralność wielu plików na podstawie wcześniej obliczonych sum.
- Regularnie weryfikuj sumy kontrolne ważnych plików, aby upewnić się, że nie zostały one zmienione.