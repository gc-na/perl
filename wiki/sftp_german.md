# [Linux] C Shell (csh) sftp Verwendung: Dateien sicher übertragen

## Übersicht
Der `sftp`-Befehl (Secure File Transfer Protocol) wird verwendet, um Dateien sicher zwischen einem lokalen und einem entfernten Computer über SSH (Secure Shell) zu übertragen. Er bietet eine sichere Alternative zu FTP und ermöglicht das Hochladen, Herunterladen und Verwalten von Dateien auf einem Server.

## Verwendung
Die grundlegende Syntax des `sftp`-Befehls lautet:

```csh
sftp [optionen] [benutzer@host]
```

## Häufige Optionen
- `-P port`: Gibt den Port an, der für die Verbindung verwendet werden soll.
- `-i datei`: Gibt eine Datei mit einem privaten Schlüssel an, die zur Authentifizierung verwendet werden soll.
- `-b datei`: Führt Befehle aus einer Datei im Batch-Modus aus.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `sftp`:

1. **Verbindung zu einem Server herstellen:**
   ```csh
   sftp benutzer@hostname
   ```

2. **Datei vom lokalen Computer auf den Server hochladen:**
   ```csh
   put lokale_datei.txt
   ```

3. **Datei vom Server auf den lokalen Computer herunterladen:**
   ```csh
   get entfernte_datei.txt
   ```

4. **Verzeichnis auf dem Server auflisten:**
   ```csh
   ls
   ```

5. **Batch-Befehle aus einer Datei ausführen:**
   ```csh
   sftp -b befehle.txt benutzer@hostname
   ```

## Tipps
- Verwenden Sie `-P`, um einen spezifischen Port anzugeben, falls der Server nicht den Standardport 22 verwendet.
- Nutzen Sie den Batch-Modus, um mehrere Befehle in einer Datei zu speichern und sie automatisch auszuführen.
- Achten Sie darauf, dass Sie die richtigen Berechtigungen für die Dateien haben, die Sie übertragen möchten.