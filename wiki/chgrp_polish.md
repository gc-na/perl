# [Linux] C Shell (csh) chgrp: Zmiana grupy plików

## Overview
Polecenie `chgrp` służy do zmiany grupy, do której należy plik lub katalog. Umożliwia to administratorom i użytkownikom zarządzanie dostępem do plików w systemie UNIX/Linux.

## Usage
Podstawowa składnia polecenia `chgrp` jest następująca:

```csh
chgrp [opcje] [argumenty]
```

## Common Options
- `-R`: Rekursywnie zmienia grupę dla wszystkich plików i katalogów w podanym katalogu.
- `-v`: Wyświetla szczegóły dotyczące zmiany grupy dla każdego pliku.
- `-c`: Wyświetla tylko pliki, dla których zmiana grupy się powiodła.

## Common Examples
Przykłady użycia polecenia `chgrp`:

1. Zmiana grupy pliku na `developers`:
   ```csh
   chgrp developers plik.txt
   ```

2. Rekursywna zmiana grupy dla katalogu `projekt`:
   ```csh
   chgrp -R developers projekt
   ```

3. Wyświetlenie szczegółów zmiany grupy:
   ```csh
   chgrp -v developers plik.txt
   ```

4. Zmiana grupy dla wielu plików jednocześnie:
   ```csh
   chgrp developers plik1.txt plik2.txt plik3.txt
   ```

## Tips
- Upewnij się, że masz odpowiednie uprawnienia do zmiany grupy plików.
- Zawsze sprawdzaj, czy zmiana grupy została przeprowadzona pomyślnie, używając polecenia `ls -l`, aby zobaczyć aktualne grupy plików.
- Używaj opcji `-R` ostrożnie, aby nie zmienić grupy dla niezamierzonych plików w podkatalogach.