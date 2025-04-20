# [Linux] C Shell (csh) md5sum Verwendung: Berechnung von MD5-Prüfziffern

## Übersicht
Der Befehl `md5sum` wird verwendet, um die MD5-Prüfziffer (Checksum) einer Datei zu berechnen. Diese Prüfziffer wird häufig verwendet, um die Integrität von Dateien zu überprüfen, indem sichergestellt wird, dass die Datei nicht verändert wurde.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```csh
md5sum [Optionen] [Argumente]
```

## Häufige Optionen
- `-b`: Berechnet die Prüfziffer für Binärdateien.
- `-c`: Überprüft die Prüfziffern von Dateien, die in einer Prüfziffern-Datei angegeben sind.
- `--help`: Zeigt eine Hilfe-Seite mit verfügbaren Optionen an.
- `--version`: Gibt die Versionsnummer des md5sum-Befehls aus.

## Häufige Beispiele
Hier sind einige praktische Beispiele zur Verwendung von `md5sum`:

1. **Berechnung der MD5-Prüfziffer einer Datei:**

   ```csh
   md5sum datei.txt
   ```

2. **Berechnung der MD5-Prüfziffer für mehrere Dateien:**

   ```csh
   md5sum datei1.txt datei2.txt
   ```

3. **Speichern der Prüfziffer in einer Datei:**

   ```csh
   md5sum datei.txt > checksum.txt
   ```

4. **Überprüfung der Prüfziffer aus einer Datei:**

   ```csh
   md5sum -c checksum.txt
   ```

## Tipps
- Verwenden Sie die Option `-b`, wenn Sie mit Binärdateien arbeiten, um genaue Ergebnisse zu erhalten.
- Speichern Sie Prüfziffern in einer Datei, um später die Integrität der Dateien einfach zu überprüfen.
- Nutzen Sie die `--help`-Option, um sich über alle verfügbaren Optionen zu informieren, falls Sie unsicher sind.