# [Linux] C Shell (csh) shutdown Verwendung: System herunterfahren

## Übersicht
Der Befehl `shutdown` wird verwendet, um ein System sicher herunterzufahren oder neu zu starten. Er ermöglicht es Administratoren, das System zu einem bestimmten Zeitpunkt oder nach einer bestimmten Verzögerung auszuschalten.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```csh
shutdown [options] [arguments]
```

## Häufige Optionen
- `-h`: Fährt das System herunter (halt).
- `-r`: Startet das System neu (reboot).
- `-k`: Sendet eine Warnung, ohne das System tatsächlich herunterzufahren.
- `time`: Gibt an, wann das Herunterfahren erfolgen soll (z.B. `now`, `+5` für in 5 Minuten).
- `message`: Eine optionale Nachricht, die an alle Benutzer gesendet wird.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung des `shutdown`-Befehls:

1. **System sofort herunterfahren:**
   ```csh
   shutdown -h now
   ```

2. **System in 10 Minuten herunterfahren:**
   ```csh
   shutdown -h +10
   ```

3. **System neu starten:**
   ```csh
   shutdown -r now
   ```

4. **Warnung an Benutzer senden, ohne das System herunterzufahren:**
   ```csh
   shutdown -k now "Das System wird in Kürze heruntergefahren."
   ```

5. **System in 1 Stunde herunterfahren und Nachricht senden:**
   ```csh
   shutdown -h +60 "Das System wird in 1 Stunde heruntergefahren."
   ```

## Tipps
- Verwenden Sie die `-k`-Option, um Benutzer zu warnen, bevor Sie das System tatsächlich herunterfahren.
- Stellen Sie sicher, dass Sie alle wichtigen Daten gespeichert haben, bevor Sie den Befehl ausführen.
- Testen Sie den Befehl in einer sicheren Umgebung, um sich mit den Optionen und deren Auswirkungen vertraut zu machen.