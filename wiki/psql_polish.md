# [Linux] C Shell (csh) psql użycie: Interakcja z bazą danych PostgreSQL

## Overview
Polecenie `psql` jest interaktywnym narzędziem do zarządzania bazą danych PostgreSQL. Umożliwia użytkownikom wykonywanie zapytań SQL, zarządzanie schematami bazy danych oraz administrację serwerem PostgreSQL.

## Usage
Podstawowa składnia polecenia `psql` jest następująca:

```csh
psql [opcje] [argumenty]
```

## Common Options
- `-h` : Określa adres hosta serwera PostgreSQL.
- `-U` : Umożliwia podanie nazwy użytkownika do logowania.
- `-d` : Określa nazwę bazy danych, z którą chcesz się połączyć.
- `-p` : Umożliwia podanie portu, na którym nasłuchuje serwer PostgreSQL.
- `-f` : Wykonuje polecenia SQL z pliku.

## Common Examples
- Połączenie z lokalną bazą danych jako domyślny użytkownik:

```csh
psql
```

- Połączenie z określoną bazą danych jako określony użytkownik:

```csh
psql -U nazwa_użytkownika -d nazwa_bazy
```

- Połączenie z serwerem na innym hoście:

```csh
psql -h adres_hosta -U nazwa_użytkownika -d nazwa_bazy
```

- Wykonanie poleceń SQL z pliku:

```csh
psql -U nazwa_użytkownika -d nazwa_bazy -f sczytaj.sql
```

## Tips
- Zawsze używaj opcji `-U`, aby upewnić się, że logujesz się jako właściwy użytkownik.
- Możesz używać pliku `.pgpass`, aby przechowywać hasła, co ułatwia logowanie.
- Korzystaj z opcji `\?` w interaktywnym trybie `psql`, aby uzyskać pomoc dotyczącą dostępnych poleceń i opcji.