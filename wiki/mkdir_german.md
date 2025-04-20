# [Linux] C Shell (csh) mkdir Verwendung: Verzeichnisse erstellen

## Übersicht
Der Befehl `mkdir` wird verwendet, um neue Verzeichnisse im Dateisystem zu erstellen. Er ist ein grundlegendes Werkzeug in der Shell, um die Ordnerstruktur zu organisieren.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```csh
mkdir [Optionen] [Argumente]
```

## Häufige Optionen
- `-p`: Erstellt das Verzeichnis und alle übergeordneten Verzeichnisse, falls diese nicht existieren.
- `-m`: Setzt die Berechtigungen für das neu erstellte Verzeichnis, angegeben in oktaler Form.
- `-v`: Gibt eine ausführliche Ausgabe aus, die bestätigt, dass das Verzeichnis erstellt wurde.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `mkdir`:

1. **Ein einfaches Verzeichnis erstellen:**
   ```csh
   mkdir meinVerzeichnis
   ```

2. **Mehrere Verzeichnisse gleichzeitig erstellen:**
   ```csh
   mkdir verzeichnis1 verzeichnis2 verzeichnis3
   ```

3. **Ein Verzeichnis und alle übergeordneten Verzeichnisse erstellen:**
   ```csh
   mkdir -p /home/benutzer/neuerOrdner/unterordner
   ```

4. **Ein Verzeichnis mit bestimmten Berechtigungen erstellen:**
   ```csh
   mkdir -m 755 meinSicheresVerzeichnis
   ```

5. **Ausführliche Ausgabe beim Erstellen eines Verzeichnisses:**
   ```csh
   mkdir -v meinNeuesVerzeichnis
   ```

## Tipps
- Verwenden Sie die `-p` Option, um sicherzustellen, dass alle erforderlichen übergeordneten Verzeichnisse erstellt werden, ohne Fehlermeldungen zu erhalten.
- Überprüfen Sie die Berechtigungen des Verzeichnisses nach der Erstellung, um sicherzustellen, dass sie Ihren Anforderungen entsprechen.
- Nutzen Sie die `-v` Option, um Feedback zu erhalten, insbesondere wenn Sie mehrere Verzeichnisse auf einmal erstellen.