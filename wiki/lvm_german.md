# [Linux] C Shell (csh) lvm Verwendung: Verwaltung von logischen Volumes

## Übersicht
Der Befehl `lvm` (Logical Volume Manager) wird verwendet, um logische Volumes in einem Linux-System zu verwalten. Mit `lvm` können Benutzer Speicherplatz effizienter verwalten, indem sie logische Volumes erstellen, ändern und löschen.

## Verwendung
Die grundlegende Syntax des `lvm`-Befehls lautet:

```bash
lvm [Optionen] [Argumente]
```

## Häufige Optionen
- `create`: Erstellt ein neues logisches Volume.
- `remove`: Löscht ein bestehendes logisches Volume.
- `extend`: Erweitert ein bestehendes logisches Volume.
- `reduce`: Verringert die Größe eines logischen Volumes.
- `lvdisplay`: Zeigt Informationen über logische Volumes an.

## Häufige Beispiele
Hier sind einige praktische Beispiele zur Verwendung von `lvm`:

### 1. Erstellen eines neuen logischen Volumes
```bash
lvm lvcreate -n mein_volume -L 10G vg_name
```
Dies erstellt ein neues logisches Volume mit dem Namen "mein_volume" und einer Größe von 10 GB in der Volume-Gruppe "vg_name".

### 2. Löschen eines logischen Volumes
```bash
lvm lvremove vg_name/mein_volume
```
Dieser Befehl löscht das logische Volume "mein_volume" aus der Volume-Gruppe "vg_name".

### 3. Erweitern eines logischen Volumes
```bash
lvm lvextend -L +5G vg_name/mein_volume
```
Hier wird das logische Volume "mein_volume" um 5 GB erweitert.

### 4. Verringern eines logischen Volumes
```bash
lvm lvreduce -L -3G vg_name/mein_volume
```
Dieser Befehl verringert die Größe des logischen Volumes "mein_volume" um 3 GB.

### 5. Anzeigen von Informationen über logische Volumes
```bash
lvm lvdisplay
```
Mit diesem Befehl werden alle logischen Volumes und ihre Eigenschaften angezeigt.

## Tipps
- Stellen Sie sicher, dass Sie vor dem Ändern oder Löschen von logischen Volumes ein Backup Ihrer Daten haben.
- Verwenden Sie den Befehl `lvdisplay`, um vor größeren Änderungen Informationen über Ihre logischen Volumes zu überprüfen.
- Achten Sie darauf, dass das logische Volume nicht gemountet ist, bevor Sie es löschen oder reduzieren.