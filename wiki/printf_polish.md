# [Linux] C Shell (csh) printf użycie: Formatowanie i wyświetlanie tekstu

## Overview
Polecenie `printf` w C Shell (csh) służy do formatowania i wyświetlania tekstu w konsoli. Umożliwia precyzyjne kontrolowanie sposobu, w jaki dane są prezentowane, co jest szczególnie przydatne w skryptach i automatyzacji.

## Usage
Podstawowa składnia polecenia `printf` jest następująca:

```csh
printf [opcje] [argumenty]
```

## Common Options
- `%s` - format dla łańcucha znaków.
- `%d` - format dla liczb całkowitych.
- `%f` - format dla liczb zmiennoprzecinkowych.
- `\n` - nowa linia.
- `\t` - tabulacja.

## Common Examples
Przykłady użycia polecenia `printf`:

1. Wyświetlenie prostego łańcucha znaków:
   ```csh
   printf "Witaj, świecie!\n"
   ```

2. Formatowanie liczby całkowitej:
   ```csh
   set liczba = 42
   printf "Liczba to: %d\n" $liczba
   ```

3. Wyświetlenie zmiennoprzecinkowej wartości:
   ```csh
   set pi = 3.14159
   printf "Pi wynosi: %.2f\n" $pi
   ```

4. Użycie tabulacji w wyjściu:
   ```csh
   printf "Imię\tWiek\n"
   printf "Jan\t25\n"
   printf "Anna\t30\n"
   ```

## Tips
- Używaj formatów odpowiednich do typu danych, aby uniknąć błędów.
- Zawsze dodawaj `\n` na końcu, aby poprawnie zakończyć linię.
- Możesz łączyć różne formaty w jednym wywołaniu `printf`, co pozwala na elastyczne formatowanie wyjścia.