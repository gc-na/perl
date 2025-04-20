# [Linux] C Shell (csh) sha256sum Verwendung: Berechnung von SHA-256-Prüfziffern

## Übersicht
Der Befehl `sha256sum` wird verwendet, um den SHA-256-Hashwert einer Datei zu berechnen. Dieser Hashwert kann zur Überprüfung der Integrität von Dateien verwendet werden, indem man sicherstellt, dass die Datei nicht verändert wurde.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```csh
sha256sum [Optionen] [Argumente]
```

## Häufige Optionen
- `-b`: Berechnet den Hashwert für Binärdateien.
- `-c`: Überprüft die Hashwerte von Dateien, die in einer Prüfziffern-Datei aufgeführt sind.
- `--quiet`: Gibt keine Warnungen aus, wenn die Überprüfung fehlschlägt.
- `--tag`: Fügt den Dateinamen in die Ausgabe ein.

## Häufige Beispiele
Hier sind einige praktische Beispiele zur Verwendung von `sha256sum`:

1. **Berechnung des SHA-256-Hashwerts einer Datei:**
   ```csh
   sha256sum datei.txt
   ```

2. **Berechnung des Hashwerts einer Binärdatei:**
   ```csh
   sha256sum -b datei.bin
   ```

3. **Überprüfung von Hashwerten aus einer Prüfziffern-Datei:**
   ```csh
   sha256sum -c pruefziffern.txt
   ```

4. **Berechnung des Hashwerts und Ausgabe mit Dateinamen:**
   ```csh
   sha256sum --tag datei.txt
   ```

## Tipps
- Speichern Sie die Ausgabe von `sha256sum` in einer Datei, um die Integrität später zu überprüfen.
- Verwenden Sie die Option `-c`, um sicherzustellen, dass die Dateien nicht verändert wurden, indem Sie die Hashwerte regelmäßig überprüfen.
- Achten Sie darauf, dass Sie die richtigen Optionen für den Dateityp verwenden, um genaue Ergebnisse zu erhalten.