# [Linux] C Shell (csh) parted Verwendung: Partitionen verwalten

## Übersicht
Der Befehl `parted` wird verwendet, um Partitionen auf Festplatten zu erstellen, zu löschen, zu ändern und zu verwalten. Er bietet eine benutzerfreundliche Schnittstelle zur Verwaltung von Partitionen und unterstützt verschiedene Dateisysteme.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```shell
parted [Optionen] [Argumente]
```

## Häufige Optionen
- `-l` oder `--list`: Listet alle erkannten Partitionen auf.
- `mkpart`: Erstellt eine neue Partition.
- `rm`: Löscht eine Partition.
- `resizepart`: Ändert die Größe einer bestehenden Partition.
- `print`: Zeigt die Partitionstabelle der ausgewählten Festplatte an.

## Häufige Beispiele

1. **Partitionen auflisten:**
   ```shell
   parted -l
   ```

2. **Neue Partition erstellen:**
   ```shell
   parted /dev/sda mkpart primary ext4 1MiB 100MiB
   ```

3. **Partition löschen:**
   ```shell
   parted /dev/sda rm 1
   ```

4. **Größe einer Partition ändern:**
   ```shell
   parted /dev/sda resizepart 1 200MiB
   ```

5. **Partitionstabelle anzeigen:**
   ```shell
   parted /dev/sda print
   ```

## Tipps
- Stellen Sie sicher, dass Sie ein Backup Ihrer Daten haben, bevor Sie Partitionen ändern oder löschen.
- Verwenden Sie `parted` mit Bedacht, da falsche Befehle zu Datenverlust führen können.
- Überprüfen Sie die aktuelle Partitionstabelle regelmäßig, um sicherzustellen, dass alle Änderungen korrekt durchgeführt wurden.