# [Linux] C Shell (csh) lsblk Verwendung: Zeigt Blockgeräte an

## Übersicht
Der Befehl `lsblk` wird verwendet, um Informationen über Blockgeräte im System anzuzeigen. Dazu gehören Festplatten, Partitionen und andere Speichermedien. Der Befehl zeigt eine hierarchische Ansicht der Geräte und deren Eigenschaften.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```csh
lsblk [Optionen] [Argumente]
```

## Häufige Optionen
- `-a` oder `--all`: Zeigt alle Geräte an, auch leere.
- `-f` oder `--fs`: Zeigt Dateisysteminformationen an.
- `-l` oder `--list`: Listet die Geräte in einer flachen Liste auf.
- `-o` oder `--output`: Gibt an, welche Spalten angezeigt werden sollen.
- `-n` oder `--noheadings`: Unterdrückt die Kopfzeile in der Ausgabe.

## Häufige Beispiele
Hier sind einige praktische Beispiele zur Verwendung von `lsblk`:

### Beispiel 1: Grundlegende Anzeige von Blockgeräten
```csh
lsblk
```

### Beispiel 2: Anzeige aller Geräte, einschließlich leerer
```csh
lsblk -a
```

### Beispiel 3: Anzeige von Dateisysteminformationen
```csh
lsblk -f
```

### Beispiel 4: Ausgabe in einer flachen Liste
```csh
lsblk -l
```

### Beispiel 5: Anzeige spezifischer Spalten
```csh
lsblk -o NAME,SIZE,TYPE,MOUNTPOINT
```

## Tipps
- Verwenden Sie die Option `-n`, um die Ausgabe zu bereinigen, wenn Sie nur die Geräteinformationen ohne Überschriften benötigen.
- Kombinieren Sie `lsblk` mit anderen Befehlen wie `grep`, um gezielt nach bestimmten Geräten zu suchen.
- Nutzen Sie die Option `-f`, um schnell Informationen über die Dateisysteme auf den Geräten zu erhalten, was besonders nützlich bei der Fehlersuche ist.