# [Linux] C Shell (csh) mysql użycie: Interakcja z bazą danych MySQL

## Overview
Polecenie `mysql` jest klientem wiersza poleceń dla systemu zarządzania bazą danych MySQL. Umożliwia użytkownikom wykonywanie zapytań SQL, zarządzanie bazami danych oraz administrację użytkownikami w systemie MySQL.

## Usage
Podstawowa składnia polecenia `mysql` jest następująca:

```bash
mysql [options] [arguments]
```

## Common Options
- `-u [username]`: Określa nazwę użytkownika do logowania.
- `-p`: Wymusza podanie hasła użytkownika.
- `-h [hostname]`: Określa adres hosta serwera MySQL (domyślnie localhost).
- `-D [database]`: Określa bazę danych, z którą chcesz pracować.
- `--execute [query]`: Wykonuje podane zapytanie SQL.

## Common Examples
1. Logowanie do MySQL jako użytkownik root:
   ```bash
   mysql -u root -p
   ```

2. Logowanie do MySQL na zdalnym serwerze:
   ```bash
   mysql -u user -p -h 192.168.1.1
   ```

3. Wykonanie zapytania SQL bezpośrednio z wiersza poleceń:
   ```bash
   mysql -u user -p -e "SHOW DATABASES;"
   ```

4. Połączenie z określoną bazą danych:
   ```bash
   mysql -u user -p -D my_database
   ```

## Tips
- Zawsze używaj opcji `-p`, aby uniknąć niebezpieczeństwa ujawnienia hasła w historii poleceń.
- Używaj opcji `--execute`, aby szybko wykonać zapytania bez wchodzenia do interaktywnego trybu.
- Regularnie twórz kopie zapasowe swoich baz danych, aby zabezpieczyć dane przed utratą.