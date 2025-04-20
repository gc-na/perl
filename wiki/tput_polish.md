# [Linux] C Shell (csh) tput użycie: Ustawianie właściwości terminala

## Overview
Polecenie `tput` jest używane do interakcji z terminalem, umożliwiając użytkownikom ustawianie właściwości wyświetlania, takich jak kolory, położenie kursora i inne atrybuty terminala. Dzięki `tput` można dostosować wygląd i zachowanie terminala w skryptach powłoki.

## Usage
Podstawowa składnia polecenia `tput` jest następująca:

```csh
tput [opcje] [argumenty]
```

## Common Options
- `setaf` - Ustawia kolor tekstu (foreground).
- `setab` - Ustawia kolor tła (background).
- `clear` - Czyści ekran terminala.
- `cup` - Ustawia położenie kursora w określonym wierszu i kolumnie.
- `bold` - Ustawia tekst na pogrubiony.

## Common Examples
1. Ustawienie koloru tekstu na czerwony:
   ```csh
   tput setaf 1
   ```

2. Ustawienie koloru tła na niebieski:
   ```csh
   tput setab 4
   ```

3. Wyczyszczenie ekranu terminala:
   ```csh
   tput clear
   ```

4. Przesunięcie kursora do wiersza 10, kolumny 5:
   ```csh
   tput cup 10 5
   ```

5. Ustawienie tekstu na pogrubiony:
   ```csh
   tput bold
   ```

## Tips
- Używaj `tput reset`, aby przywrócić terminal do domyślnych ustawień.
- Możesz łączyć różne polecenia `tput` w skryptach, aby stworzyć bardziej złożone efekty wizualne.
- Sprawdź dostępne kolory i atrybuty terminala, używając `tput colors` oraz `tput -T xterm-256color` dla terminali obsługujących 256 kolorów.