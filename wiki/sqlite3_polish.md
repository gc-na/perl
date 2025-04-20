# [Linux] C Shell (csh) sqlite3 użycie: Interakcja z bazą danych SQLite

## Overview
Polecenie `sqlite3` służy do interakcji z bazą danych SQLite. Umożliwia użytkownikom wykonywanie zapytań SQL, tworzenie i modyfikowanie baz danych oraz zarządzanie danymi w prosty sposób.

## Usage
Podstawowa składnia polecenia `sqlite3` jest następująca:

```csh
sqlite3 [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `sqlite3`:

- `-header`: Wyświetla nagłówki kolumn w wynikach zapytań.
- `-csv`: Eksportuje wyniki zapytań w formacie CSV.
- `-init <plik>`: Wykonuje polecenia z podanego pliku przy uruchamianiu.
- `-batch`: Włącza tryb wsadowy, co oznacza, że nie będzie interaktywnego powiadamiania o błędach.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `sqlite3`:

1. **Utworzenie nowej bazy danych:**
   ```csh
   sqlite3 nowa_baza.db
   ```

2. **Wykonanie zapytania SQL:**
   ```csh
   sqlite3 nowa_baza.db "SELECT * FROM tabela;"
   ```

3. **Eksport wyników do pliku CSV:**
   ```csh
   sqlite3 -csv nowa_baza.db "SELECT * FROM tabela;" > wyniki.csv
   ```

4. **Wykonanie poleceń z pliku:**
   ```csh
   sqlite3 -init skrypt.sql nowa_baza.db
   ```

5. **Wyświetlenie nagłówków kolumn:**
   ```csh
   sqlite3 -header nowa_baza.db "SELECT * FROM tabela;"
   ```

## Tips
- Zawsze twórz kopie zapasowe bazy danych przed wprowadzeniem istotnych zmian.
- Używaj opcji `-header`, aby ułatwić czytanie wyników zapytań.
- Eksperymentuj z różnymi formatami eksportu, aby znaleźć ten, który najlepiej pasuje do Twoich potrzeb.