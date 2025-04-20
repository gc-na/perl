# [Linux] C Shell (csh) find Verwendung: Dateinamen finden

## Übersicht
Der `find`-Befehl wird verwendet, um Dateien und Verzeichnisse in einem Dateisystem zu suchen. Er ermöglicht es Benutzern, gezielt nach Dateien zu suchen, die bestimmten Kriterien entsprechen, wie z.B. Namen, Typ oder Änderungsdatum.

## Verwendung
Die grundlegende Syntax des `find`-Befehls lautet:

```
find [Optionen] [Argumente]
```

## Häufige Optionen
- `-name <Muster>`: Sucht nach Dateien, deren Namen dem angegebenen Muster entsprechen.
- `-type <Typ>`: Filtert die Suche nach dem Dateityp (z.B. `f` für reguläre Dateien, `d` für Verzeichnisse).
- `-mtime <Tage>`: Sucht nach Dateien, die vor einer bestimmten Anzahl von Tagen geändert wurden.
- `-size <Größe>`: Sucht nach Dateien, die eine bestimmte Größe haben.
- `-exec <Befehl> {} \;`: Führt einen angegebenen Befehl für jede gefundene Datei aus.

## Häufige Beispiele
Um die Verwendung des `find`-Befehls zu veranschaulichen, sind hier einige praktische Beispiele:

1. Suchen nach einer Datei mit einem bestimmten Namen:
   ```csh
   find /pfad/zum/verzeichnis -name "datei.txt"
   ```

2. Suchen nach allen Verzeichnissen:
   ```csh
   find /pfad/zum/verzeichnis -type d
   ```

3. Suchen nach Dateien, die in den letzten 7 Tagen geändert wurden:
   ```csh
   find /pfad/zum/verzeichnis -mtime -7
   ```

4. Suchen nach Dateien mit einer bestimmten Größe (z.B. 1MB):
   ```csh
   find /pfad/zum/verzeichnis -size 1M
   ```

5. Ausführen eines Befehls auf jeder gefundenen Datei (z.B. `ls -l`):
   ```csh
   find /pfad/zum/verzeichnis -name "*.txt" -exec ls -l {} \;
   ```

## Tipps
- Verwenden Sie `-iname` anstelle von `-name`, um die Suche nicht zwischen Groß- und Kleinschreibung zu unterscheiden.
- Kombinieren Sie mehrere Optionen, um die Suche zu verfeinern (z.B. `-type f -mtime -30` für reguläre Dateien, die in den letzten 30 Tagen geändert wurden).
- Testen Sie Ihre `find`-Befehle zuerst ohne `-exec`, um sicherzustellen, dass Sie die richtigen Dateien finden, bevor Sie Aktionen darauf ausführen.