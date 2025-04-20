# [Linux] C Shell (csh) expr użycie: Obliczanie wyrażeń arytmetycznych i logicznych

## Overview
Polecenie `expr` w C Shell (csh) służy do obliczania wartości wyrażeń arytmetycznych i logicznych. Umożliwia wykonywanie podstawowych operacji matematycznych oraz porównań, co czyni je przydatnym narzędziem w skryptach powłoki.

## Usage
Podstawowa składnia polecenia `expr` jest następująca:

```csh
expr [opcje] [argumenty]
```

## Common Options
- `+` : Dodawanie dwóch wartości.
- `-` : Odejmowanie drugiej wartości od pierwszej.
- `*` : Mnożenie dwóch wartości.
- `/` : Dzielenie pierwszej wartości przez drugą.
- `%` : Reszta z dzielenia pierwszej wartości przez drugą.
- `=` : Porównanie wartości (sprawdza równość).
- `!=` : Porównanie wartości (sprawdza nierówność).

## Common Examples
- Dodawanie dwóch liczb:
  ```csh
  expr 5 + 3
  ```
  Wynik: `8`

- Odejmowanie dwóch liczb:
  ```csh
  expr 10 - 4
  ```
  Wynik: `6`

- Mnożenie dwóch liczb:
  ```csh
  expr 7 \* 6
  ```
  Wynik: `42`

- Dzielenie dwóch liczb:
  ```csh
  expr 20 / 4
  ```
  Wynik: `5`

- Sprawdzanie równości:
  ```csh
  expr 5 = 5
  ```
  Wynik: `1` (prawda)

- Sprawdzanie nierówności:
  ```csh
  expr 5 != 3
  ```
  Wynik: `1` (prawda)

## Tips
- Pamiętaj, aby używać znaku `\` przed znakiem mnożenia `*`, aby uniknąć jego interpretacji przez powłokę.
- Używaj spacji wokół operatorów, aby `expr` poprawnie rozpoznał wyrażenia.
- `expr` zwraca `0` dla fałszywych warunków, co może być użyteczne w skryptach do kontroli przepływu.