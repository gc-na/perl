# [Linux] C Shell (csh) crontab Verwendung: Zeitgesteuerte Aufgaben planen

## Übersicht
Der Befehl `crontab` wird verwendet, um zeitgesteuerte Aufgaben in Unix-ähnlichen Betriebssystemen zu planen. Mit `crontab` können Benutzer Skripte oder Befehle zu bestimmten Zeiten oder in regelmäßigen Abständen automatisch ausführen lassen.

## Verwendung
Die grundlegende Syntax des `crontab`-Befehls lautet:

```bash
crontab [Optionen] [Argumente]
```

## Häufige Optionen
- `-e`: Öffnet die Crontab-Datei im Editor zur Bearbeitung.
- `-l`: Listet die aktuelle Crontab des Benutzers auf.
- `-r`: Entfernt die Crontab des Benutzers.
- `-i`: Fordert eine Bestätigung an, bevor die Crontab gelöscht wird.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `crontab`:

1. **Crontab bearbeiten**:
   Um die Crontab-Datei zu bearbeiten, verwenden Sie:
   ```bash
   crontab -e
   ```

2. **Crontab auflisten**:
   Um die aktuelle Crontab anzuzeigen, verwenden Sie:
   ```bash
   crontab -l
   ```

3. **Crontab löschen**:
   Um die Crontab zu löschen, verwenden Sie:
   ```bash
   crontab -r
   ```

4. **Einen Job hinzufügen**:
   Um einen Job hinzuzufügen, der täglich um 2 Uhr morgens ein Skript ausführt, fügen Sie in der Crontab-Datei folgende Zeile hinzu:
   ```bash
   0 2 * * * /pfad/zum/skript.sh
   ```

5. **Ein Job, der jede Stunde ausgeführt wird**:
   Um einen Job zu planen, der jede Stunde ausgeführt wird, verwenden Sie:
   ```bash
   0 * * * * /pfad/zum/anderes_skript.sh
   ```

## Tipps
- Stellen Sie sicher, dass die Skripte, die Sie planen, ausführbar sind (verwenden Sie `chmod +x /pfad/zum/skript.sh`).
- Testen Sie Ihre Skripte manuell, bevor Sie sie in die Crontab einfügen, um sicherzustellen, dass sie wie gewünscht funktionieren.
- Verwenden Sie vollständige Pfade zu Skripten und Dateien, um Probleme mit dem Arbeitsverzeichnis zu vermeiden.