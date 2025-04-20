# [Linux] C Shell (csh) fdisk Verwendung: Partitionierung von Festplatten

## Übersicht
Der `fdisk` Befehl wird verwendet, um Partitionen auf Festplatten zu erstellen, zu löschen und zu verwalten. Er ist ein wichtiges Werkzeug für die Verwaltung von Datenträgern in Unix-ähnlichen Betriebssystemen.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```csh
fdisk [Optionen] [Argumente]
```

## Häufige Optionen
- `-l`: Listet alle Partitionen auf allen Festplatten auf.
- `-u`: Zeigt die Partitionen in Sektoren an.
- `-n`: Erstellt eine neue Partition.
- `-d`: Löscht eine bestehende Partition.
- `-p`: Zeigt die Partitionstabelle der angegebenen Festplatte an.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `fdisk`:

1. **Auflisten aller Partitionen:**
   ```csh
   fdisk -l
   ```

2. **Partitionstabelle einer bestimmten Festplatte anzeigen:**
   ```csh
   fdisk -p /dev/sda
   ```

3. **Neue Partition erstellen:**
   ```csh
   fdisk /dev/sda
   ```
   (Im interaktiven Modus, verwenden Sie die Eingabeaufforderungen, um eine neue Partition zu erstellen.)

4. **Eine Partition löschen:**
   ```csh
   fdisk /dev/sda
   ```
   (Wählen Sie die Option zum Löschen im interaktiven Modus.)

## Tipps
- Stellen Sie sicher, dass Sie ein Backup Ihrer Daten haben, bevor Sie Partitionen ändern.
- Verwenden Sie `man fdisk`, um die vollständige Dokumentation und alle verfügbaren Optionen zu lesen.
- Seien Sie vorsichtig beim Arbeiten mit `fdisk`, da falsche Befehle zu Datenverlust führen können.