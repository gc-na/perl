# [Linux] C Shell (csh) at: Planowanie zadań

## Overview
Polecenie `at` w C Shell (csh) służy do planowania jednorazowych zadań, które mają być wykonane w określonym czasie w przyszłości. Umożliwia użytkownikom uruchamianie skryptów lub poleceń w wyznaczonym momencie.

## Usage
Podstawowa składnia polecenia `at` jest następująca:

```csh
at [opcje] [argumenty]
```

## Common Options
- `-f` : Określa plik, z którego mają być odczytywane polecenia do wykonania.
- `-m` : Wysyła wiadomość e-mail po zakończeniu zadania.
- `-l` : Wyświetla listę zaplanowanych zadań.
- `-d` : Usuwa zaplanowane zadanie.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `at`:

1. **Planowanie prostego polecenia**:
   Aby zaplanować polecenie `echo` na godzinę 14:00, można użyć:

   ```csh
   echo "Hello, World!" | at 14:00
   ```

2. **Planowanie skryptu**:
   Aby uruchomić skrypt `backup.sh` o godzinie 18:30:

   ```csh
   at 18:30 -f /path/to/backup.sh
   ```

3. **Wyświetlanie zaplanowanych zadań**:
   Aby zobaczyć wszystkie zaplanowane zadania:

   ```csh
   at -l
   ```

4. **Usuwanie zaplanowanego zadania**:
   Aby usunąć zaplanowane zadanie o identyfikatorze `1`:

   ```csh
   at -d 1
   ```

## Tips
- Upewnij się, że masz odpowiednie uprawnienia do uruchamiania poleceń w zaplanowanym czasie.
- Sprawdzaj regularnie zaplanowane zadania, aby uniknąć nieporozumień.
- Używaj opcji `-m`, aby otrzymać powiadomienie e-mail po zakończeniu zadania, co może być przydatne w przypadku dłuższych operacji.