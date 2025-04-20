# [Linux] C Shell (csh) screen użycie: zarządzanie sesjami terminalowymi

## Overview
Polecenie `screen` w C Shell (csh) pozwala na tworzenie i zarządzanie wieloma sesjami terminalowymi w jednym oknie. Umożliwia to użytkownikom uruchamianie procesów w tle oraz powracanie do nich później, co jest szczególnie przydatne w przypadku długotrwałych zadań.

## Usage
Podstawowa składnia polecenia `screen` wygląda następująco:

```
screen [opcje] [argumenty]
```

## Common Options
- `-S <nazwa>`: Umożliwia nadanie sesji unikalnej nazwy.
- `-d -r`: Odłącza sesję i łączy się z nią ponownie.
- `-list`: Wyświetla listę aktywnych sesji.
- `-X <komenda>`: Wysyła komendę do działającej sesji.

## Common Examples
1. **Uruchomienie nowej sesji screen:**
   ```csh
   screen
   ```

2. **Nadanie nazwy sesji:**
   ```csh
   screen -S moja_sesja
   ```

3. **Odłączenie sesji:**
   Naciśnij `Ctrl-a` następnie `d`.

4. **Powrót do odłączonej sesji:**
   ```csh
   screen -r
   ```

5. **Wyświetlenie listy aktywnych sesji:**
   ```csh
   screen -list
   ```

6. **Wysyłanie komendy do sesji:**
   ```csh
   screen -S moja_sesja -X quit
   ```

## Tips
- Używaj unikalnych nazw sesji, aby łatwiej je identyfikować.
- Regularnie odłączaj sesje, aby uniknąć przeciążenia terminala.
- Sprawdzaj aktywne sesje przed uruchomieniem nowej, aby nie tworzyć zbędnych instancji.