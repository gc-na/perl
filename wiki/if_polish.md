# [Linux] C Shell (csh) if: Sprawdza warunki i wykonuje polecenia

## Overview
Polecenie `if` w C Shell (csh) służy do wykonywania warunkowego kodu. Umożliwia sprawdzenie, czy określony warunek jest spełniony, a następnie wykonanie odpowiednich poleceń w zależności od wyniku tego sprawdzenia.

## Usage
Podstawowa składnia polecenia `if` jest następująca:

```csh
if (warunek) then
    polecenia
endif
```

## Common Options
- `then`: Wskazuje początek bloku poleceń, które mają być wykonane, jeśli warunek jest spełniony.
- `endif`: Kończy blok `if`, wskazując, że nie ma więcej poleceń do wykonania w tym warunku.

## Common Examples
Przykłady użycia polecenia `if`:

1. Sprawdzenie, czy plik istnieje:
    ```csh
    if (-e plik.txt) then
        echo "Plik istnieje."
    endif
    ```

2. Sprawdzenie, czy zmienna jest pusta:
    ```csh
    set zmienna = ""
    if ("$zmienna" == "") then
        echo "Zmienna jest pusta."
    endif
    ```

3. Sprawdzenie, czy liczba jest większa od zera:
    ```csh
    set liczba = 5
    if ($liczba > 0) then
        echo "Liczba jest większa od zera."
    endif
    ```

4. Użycie `else` do alternatywnego działania:
    ```csh
    set liczba = -3
    if ($liczba > 0) then
        echo "Liczba jest dodatnia."
    else
        echo "Liczba jest niedodatnia."
    endif
    ```

## Tips
- Zawsze pamiętaj o zakończeniu bloku `if` poleceniem `endif`, aby uniknąć błędów składniowych.
- Używaj odpowiednich operatorów porównania, takich jak `==`, `!=`, `>`, `<`, aby poprawnie sprawdzać warunki.
- Możesz zagnieżdżać instrukcje `if`, aby tworzyć bardziej złożone logiki warunkowe.