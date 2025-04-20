# [Linux] C Shell (csh) sqlite3 Verwendung: Datenbankverwaltung über die Kommandozeile

## Übersicht
Der `sqlite3` Befehl ist ein Kommandozeilenwerkzeug zur Verwaltung von SQLite-Datenbanken. Mit diesem Befehl können Benutzer Datenbanken erstellen, abfragen, aktualisieren und verwalten, ohne eine grafische Benutzeroberfläche zu benötigen.

## Verwendung
Die grundlegende Syntax des `sqlite3` Befehls ist wie folgt:

```bash
sqlite3 [Optionen] [Argumente]
```

## Häufige Optionen
- `-help`: Zeigt eine Hilfe mit den verfügbaren Befehlen und Optionen an.
- `-version`: Gibt die aktuelle Version von SQLite aus.
- `-init <datei>`: Führt die angegebenen SQL-Befehle aus der Datei beim Start aus.
- `-batch`: Führt die Befehle im Batch-Modus aus, ohne interaktive Eingabe.

## Häufige Beispiele
Hier sind einige praktische Beispiele zur Verwendung des `sqlite3` Befehls:

### 1. Erstellen einer neuen Datenbank
```bash
sqlite3 meine_datenbank.db
```

### 2. Erstellen einer Tabelle
```bash
sqlite3 meine_datenbank.db "CREATE TABLE benutzer (id INTEGER PRIMARY KEY, name TEXT);"
```

### 3. Einfügen von Daten
```bash
sqlite3 meine_datenbank.db "INSERT INTO benutzer (name) VALUES ('Max Mustermann');"
```

### 4. Abfragen von Daten
```bash
sqlite3 meine_datenbank.db "SELECT * FROM benutzer;"
```

### 5. Exportieren von Daten in eine CSV-Datei
```bash
sqlite3 meine_datenbank.db "SELECT * FROM benutzer;" > benutzer.csv
```

## Tipps
- Verwenden Sie die Option `-init`, um beim Starten von `sqlite3` automatisch SQL-Skripte auszuführen.
- Nutzen Sie den Batch-Modus (`-batch`), wenn Sie Skripte ohne Benutzereingabe ausführen möchten.
- Speichern Sie häufig verwendete Abfragen in SQL-Dateien, um die Wiederverwendbarkeit zu erhöhen und die Eingabe zu erleichtern.