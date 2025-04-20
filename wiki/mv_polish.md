# [Linux] C Shell (csh) mv użycie: Przenoszenie i zmiana nazw plików

## Overview
Polecenie `mv` w C Shell (csh) służy do przenoszenia plików i katalogów oraz zmiany ich nazw. Jest to jedno z podstawowych narzędzi do zarządzania plikami w systemie Unix i Linux.

## Usage
Podstawowa składnia polecenia `mv` jest następująca:

```
mv [opcje] [argumenty]
```

## Common Options
- `-i`: Pyta o potwierdzenie przed nadpisaniem istniejącego pliku.
- `-u`: Przenosi plik tylko wtedy, gdy źródło jest nowsze niż cel lub cel nie istnieje.
- `-v`: Wyświetla szczegóły operacji przenoszenia.

## Common Examples
1. **Przenoszenie pliku do innego katalogu:**
   ```csh
   mv dokument.txt /home/użytkownik/dokumenty/
   ```

2. **Zmiana nazwy pliku:**
   ```csh
   mv stary_nazwa.txt nowy_nazwa.txt
   ```

3. **Przenoszenie wielu plików do katalogu:**
   ```csh
   mv plik1.txt plik2.txt /home/użytkownik/dokumenty/
   ```

4. **Przenoszenie pliku z potwierdzeniem:**
   ```csh
   mv -i dokument.txt /home/użytkownik/dokumenty/
   ```

5. **Przenoszenie pliku tylko jeśli jest nowszy:**
   ```csh
   mv -u dokument.txt /home/użytkownik/dokumenty/
   ```

## Tips
- Zawsze używaj opcji `-i`, jeśli nie jesteś pewien, czy chcesz nadpisać istniejące pliki.
- Używaj opcji `-v`, aby śledzić, co dokładnie robi polecenie `mv`, co może być pomocne w przypadku przenoszenia wielu plików.
- Przed przeniesieniem plików do nowego katalogu, upewnij się, że masz odpowiednie uprawnienia do zapisu w tym katalogu.