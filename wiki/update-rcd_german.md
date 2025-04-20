# [Linux] C Shell (csh) update-rc.d: Dienstprogramme verwalten

## Übersicht
Der Befehl `update-rc.d` wird verwendet, um Skripte für Systemdienste in das Init-System von Debian-basierten Linux-Distributionen zu integrieren. Er ermöglicht das Hinzufügen, Entfernen oder Ändern von Start- und Stopprioritäten für Dienste, die beim Systemstart oder -stopp ausgeführt werden.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
update-rc.d [optionen] [argumente]
```

## Häufige Optionen
- `defaults`: Fügt die Standardstart- und Stopp-Skripte für den Dienst hinzu.
- `remove`: Entfernt die Start- und Stopp-Skripte für den Dienst.
- `enable`: Aktiviert den Dienst für den automatischen Start.
- `disable`: Deaktiviert den Dienst für den automatischen Start.
- `force`: Erzwingt die Ausführung des Befehls, auch wenn es zu Konflikten kommen könnte.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `update-rc.d`:

1. **Standarddienste hinzufügen**:
   ```bash
   sudo update-rc.d myservice defaults
   ```

2. **Dienst entfernen**:
   ```bash
   sudo update-rc.d myservice remove
   ```

3. **Dienst aktivieren**:
   ```bash
   sudo update-rc.d myservice enable
   ```

4. **Dienst deaktivieren**:
   ```bash
   sudo update-rc.d myservice disable
   ```

5. **Dienste mit Zwang hinzufügen**:
   ```bash
   sudo update-rc.d myservice defaults force
   ```

## Tipps
- Stellen Sie sicher, dass die Skripte im Verzeichnis `/etc/init.d/` vorhanden sind, bevor Sie `update-rc.d` verwenden.
- Überprüfen Sie die Prioritäten der Dienste, um Konflikte beim Start zu vermeiden.
- Nutzen Sie `man update-rc.d`, um weitere Informationen und Optionen zu erhalten.