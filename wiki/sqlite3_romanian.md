# [Linux] C Shell (csh) sqlite3 utilizare: Interacționează cu baze de date SQLite

## Overview
Comanda `sqlite3` este un instrument de linie de comandă care permite utilizatorilor să interacționeze cu bazele de date SQLite. Aceasta oferă funcționalități pentru a crea, modifica și interoga baze de date, facilitând gestionarea datelor într-un mod eficient.

## Usage
Sintaxa de bază a comenzii `sqlite3` este următoarea:
```bash
sqlite3 [opțiuni] [argumente]
```

## Common Options
- `-help`: Afișează ajutorul și opțiunile disponibile pentru utilizare.
- `-version`: Afișează versiunea curentă a SQLite.
- `-init <file>`: Execută comenzile din fișierul specificat la pornirea sqlite3.
- `-batch`: Rulare în modul batch, fără interacțiune cu utilizatorul.

## Common Examples
1. **Crearea unei baze de date noi**:
   ```bash
   sqlite3 baza_de_date.db
   ```

2. **Executarea unui fișier SQL**:
   ```bash
   sqlite3 baza_de_date.db < script.sql
   ```

3. **Interogarea unei baze de date**:
   ```bash
   sqlite3 baza_de_date.db "SELECT * FROM tabela;"
   ```

4. **Afișarea versiunii SQLite**:
   ```bash
   sqlite3 -version
   ```

5. **Crearea unei tabele**:
   ```bash
   sqlite3 baza_de_date.db "CREATE TABLE utilizatori (id INTEGER PRIMARY KEY, nume TEXT);"
   ```

## Tips
- Folosește opțiunea `-init` pentru a încărca automat scripturi SQL la pornirea sqlite3, economisind timp.
- Asigură-te că ai backup-uri ale bazelor de date importante înainte de a efectua modificări.
- Explorează documentația SQLite pentru a învăța despre funcționalitățile avansate, cum ar fi indexarea și tranzacțiile.