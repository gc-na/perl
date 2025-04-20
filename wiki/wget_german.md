# [Linux] C Shell (csh) wget Verwendung: Dateien von Webservern herunterladen

## Übersicht
Der `wget`-Befehl ist ein leistungsstarkes Tool zum Herunterladen von Dateien aus dem Internet. Es unterstützt verschiedene Protokolle wie HTTP, HTTPS und FTP und ermöglicht das Herunterladen von Inhalten in einer Vielzahl von Formaten.

## Verwendung
Die grundlegende Syntax des `wget`-Befehls lautet:

```bash
wget [Optionen] [Argumente]
```

## Häufige Optionen
- `-O [Dateiname]`: Speichert die heruntergeladene Datei unter dem angegebenen Dateinamen.
- `-c`: Setzt einen unterbrochenen Download fort.
- `-r`: Aktiviert den rekursiven Download von Webseiten.
- `-p`: Lädt alle notwendigen Dateien herunter, um eine Webseite korrekt anzuzeigen (z.B. Bilder, CSS).
- `--limit-rate=[Rate]`: Beschränkt die Downloadgeschwindigkeit auf die angegebene Rate.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `wget`:

1. **Einzelne Datei herunterladen:**
   ```bash
   wget https://example.com/datei.zip
   ```

2. **Datei unter einem bestimmten Namen speichern:**
   ```bash
   wget -O meine_datei.zip https://example.com/datei.zip
   ```

3. **Download fortsetzen:**
   ```bash
   wget -c https://example.com/große_datei.zip
   ```

4. **Rekursiven Download einer Webseite:**
   ```bash
   wget -r https://example.com
   ```

5. **Webseite mit allen notwendigen Dateien herunterladen:**
   ```bash
   wget -p https://example.com
   ```

## Tipps
- Verwenden Sie die Option `-q`, um den Download im stillen Modus durchzuführen, ohne Fortschrittsanzeigen.
- Achten Sie darauf, die Downloadgeschwindigkeit mit `--limit-rate` zu begrenzen, um Bandbreite zu sparen.
- Prüfen Sie die heruntergeladenen Dateien regelmäßig auf Vollständigkeit und Integrität, insbesondere bei großen Downloads.