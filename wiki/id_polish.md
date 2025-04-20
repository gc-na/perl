# [Linux] C Shell (csh) id: wyświetlanie informacji o użytkowniku

## Overview
Polecenie `id` w C Shell (csh) służy do wyświetlania informacji o użytkowniku, w tym jego identyfikatora użytkownika (UID), identyfikatora grupy (GID) oraz przynależności do grup.

## Usage
Podstawowa składnia polecenia `id` jest następująca:

```
id [opcje] [argumenty]
```

## Common Options
- `-u`: Wyświetla tylko identyfikator użytkownika (UID).
- `-g`: Wyświetla tylko identyfikator grupy (GID).
- `-G`: Wyświetla wszystkie identyfikatory grup, do których należy użytkownik.
- `-n`: Wyświetla nazwy zamiast identyfikatorów.

## Common Examples
1. Wyświetlenie podstawowych informacji o bieżącym użytkowniku:
   ```csh
   id
   ```

2. Wyświetlenie tylko identyfikatora użytkownika:
   ```csh
   id -u
   ```

3. Wyświetlenie tylko identyfikatora grupy:
   ```csh
   id -g
   ```

4. Wyświetlenie wszystkich grup, do których należy użytkownik:
   ```csh
   id -G
   ```

5. Wyświetlenie nazwy użytkownika oraz identyfikatora:
   ```csh
   id -n -u
   ```

## Tips
- Używaj opcji `-n`, aby uzyskać bardziej czytelne wyniki, zwłaszcza gdy pracujesz z identyfikatorami grup.
- Sprawdzaj przynależność do grup, aby upewnić się, że masz odpowiednie uprawnienia do wykonywania określonych zadań.
- Możesz użyć `id [nazwa_użytkownika]`, aby uzyskać informacje o innym użytkowniku, co jest przydatne w administracji systemem.