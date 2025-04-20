# [Linux] C Shell (csh) basename Verwendung: Entfernt den Pfad und die Dateierweiterung von Dateinamen

## Übersicht
Der Befehl `basename` wird verwendet, um den Dateinamen aus einem vollständigen Pfad zu extrahieren. Er entfernt sowohl den Verzeichnispfad als auch eine angegebene Dateierweiterung, sodass nur der reine Dateiname übrig bleibt.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```
basename [Optionen] [Argumente]
```

## Häufige Optionen
- `-a`: Behandelt mehrere Argumente und gibt die Basen für alle an.
- `-s`: Entfernt die angegebene Dateierweiterung vom Dateinamen.

## Häufige Beispiele

1. **Einfacher Gebrauch ohne Erweiterung entfernen:**
   ```csh
   basename /usr/local/bin/script.sh
   ```
   Ausgabe:
   ```
   script.sh
   ```

2. **Entfernen der Dateierweiterung:**
   ```csh
   basename /usr/local/bin/script.sh .sh
   ```
   Ausgabe:
   ```
   script
   ```

3. **Verwendung mit mehreren Argumenten:**
   ```csh
   basename -a /usr/local/bin/script.sh /usr/bin/another_script.py
   ```
   Ausgabe:
   ```
   script.sh
   another_script.py
   ```

4. **Entfernen einer Erweiterung von mehreren Dateien:**
   ```csh
   basename -a /path/to/file1.txt /path/to/file2.txt .txt
   ```
   Ausgabe:
   ```
   file1
   file2
   ```

## Tipps
- Verwenden Sie `basename` in Skripten, um Dateinamen dynamisch zu verarbeiten, ohne sich um die Verzeichnispfade kümmern zu müssen.
- Kombinieren Sie `basename` mit anderen Befehlen wie `find`, um gezielt Dateinamen zu extrahieren und weiterzuverarbeiten.
- Achten Sie darauf, die richtige Dateierweiterung anzugeben, wenn Sie diese entfernen möchten, um unerwartete Ergebnisse zu vermeiden.