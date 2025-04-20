# [Linux] C Shell (csh) nohup Verwendung: Befehle im Hintergrund ausführen

## Übersicht
Der Befehl `nohup` (no hang up) wird verwendet, um Prozesse im Hintergrund auszuführen, sodass sie nicht beendet werden, wenn die Sitzung geschlossen wird. Dies ist besonders nützlich, wenn Sie lange laufende Aufgaben haben, die nicht unterbrochen werden sollen.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```csh
nohup [Optionen] [Argumente]
```

## Häufige Optionen
- `&`: Führt den Befehl im Hintergrund aus.
- `-h`: Zeigt die Hilfe für den Befehl an.
- `-p`: Bezieht sich auf den Prozess, der mit `nohup` gestartet wurde.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `nohup`:

1. **Ein einfaches Skript im Hintergrund ausführen:**
   ```csh
   nohup ./mein_skript.sh &
   ```

2. **Ein Python-Skript im Hintergrund ausführen und die Ausgabe in eine Datei umleiten:**
   ```csh
   nohup python mein_programm.py > ausgabe.log &
   ```

3. **Einen Befehl im Hintergrund ausführen und die Fehlerausgabe in eine Datei umleiten:**
   ```csh
   nohup ls -l /verzeichnis > ausgabe.log 2>&1 &
   ```

4. **Einen Befehl ohne Ausgabe im Hintergrund ausführen:**
   ```csh
   nohup mein_befehl > /dev/null 2>&1 &
   ```

## Tipps
- Verwenden Sie `&`, um sicherzustellen, dass der Prozess im Hintergrund läuft.
- Überprüfen Sie die `nohup.out`-Datei, um die Standardausgabe und Fehlerausgaben zu sehen, wenn Sie keine Umleitung angegeben haben.
- Stellen Sie sicher, dass Sie die richtigen Berechtigungen haben, um das Skript oder den Befehl auszuführen, bevor Sie `nohup` verwenden.