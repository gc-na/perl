# [Linux] C Shell (csh) rsync Verwendung: Dateien synchronisieren und übertragen

## Übersicht
Der `rsync`-Befehl ist ein leistungsstarkes Werkzeug zum Übertragen und Synchronisieren von Dateien und Verzeichnissen zwischen verschiedenen Speicherorten. Es ist besonders nützlich, um nur die Änderungen zu übertragen, wodurch Bandbreite und Zeit gespart werden.

## Verwendung
Die grundlegende Syntax des `rsync`-Befehls lautet:

```bash
rsync [Optionen] [Quell] [Ziel]
```

## Häufige Optionen
- `-a`: Archivmodus; überträgt Dateien rekursiv und bewahrt die Dateiattribute.
- `-v`: Ausführliche Ausgabe; zeigt den Fortschritt der Übertragung an.
- `-z`: Komprimiert die Daten während der Übertragung, um die Bandbreite zu sparen.
- `-r`: Überträgt Verzeichnisse rekursiv.
- `--delete`: Löscht Dateien im Zielverzeichnis, die nicht mehr im Quellverzeichnis vorhanden sind.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `rsync`:

1. **Ein einfaches Backup eines Verzeichnisses erstellen:**
   ```bash
   rsync -av /pfad/zum/quellverzeichnis/ /pfad/zum/zielverzeichnis/
   ```

2. **Daten über das Netzwerk synchronisieren:**
   ```bash
   rsync -avz /lokales/verzeichnis/ benutzer@remote-server:/remote/verzeichnis/
   ```

3. **Verzeichnisse synchronisieren und nicht mehr vorhandene Dateien im Ziel löschen:**
   ```bash
   rsync -av --delete /pfad/zum/quellverzeichnis/ /pfad/zum/zielverzeichnis/
   ```

4. **Nur neue oder geänderte Dateien übertragen:**
   ```bash
   rsync -av --ignore-existing /pfad/zum/quellverzeichnis/ /pfad/zum/zielverzeichnis/
   ```

## Tipps
- Verwenden Sie den `-n` oder `--dry-run`-Schalter, um eine Simulation der Übertragung durchzuführen, bevor Sie die tatsächliche Übertragung starten. So können Sie sehen, welche Dateien betroffen sind.
- Achten Sie darauf, den Schrägstrich `/` am Ende des Quellverzeichnisses zu verwenden, um nur den Inhalt und nicht das Verzeichnis selbst zu übertragen.
- Nutzen Sie `rsync` regelmäßig für Backups, um sicherzustellen, dass Ihre Daten immer aktuell sind.