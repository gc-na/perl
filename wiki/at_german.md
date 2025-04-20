# [Linux] C Shell (csh) at: Aufgaben zeitgesteuert ausführen

## Übersicht
Der `at` Befehl wird verwendet, um einmalige Aufgaben zu einem bestimmten Zeitpunkt in der Zukunft auszuführen. Dies ist nützlich, um Skripte oder Befehle zu planen, die zu einem späteren Zeitpunkt automatisch ausgeführt werden sollen.

## Verwendung
Die grundlegende Syntax des `at` Befehls lautet:

```
at [Optionen] [Zeit]
```

## Häufige Optionen
- `-f`: Gibt eine Datei an, die die Befehle enthält, die ausgeführt werden sollen.
- `-m`: Sendet eine E-Mail-Benachrichtigung, wenn der Job abgeschlossen ist.
- `-q`: Gibt die Warteschlange an, in der der Job ausgeführt werden soll.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung des `at` Befehls:

1. **Einen Befehl um 15:00 Uhr ausführen:**
   ```csh
   echo "echo 'Hallo Welt'" | at 15:00
   ```

2. **Ein Skript zu einem bestimmten Datum und Uhrzeit ausführen:**
   ```csh
   at 2023-10-31 14:00 < mein_skript.sh
   ```

3. **Einen Befehl in 10 Minuten ausführen:**
   ```csh
   echo "backup.sh" | at now + 10 minutes
   ```

4. **Einen Befehl aus einer Datei ausführen:**
   ```csh
   at -f befehle.txt 09:00
   ```

## Tipps
- Überprüfen Sie Ihre geplanten Jobs mit dem Befehl `atq`, um sicherzustellen, dass alles korrekt eingeplant ist.
- Nutzen Sie die `-m` Option, um sicherzustellen, dass Sie eine Benachrichtigung erhalten, wenn der Job abgeschlossen ist.
- Seien Sie vorsichtig bei der Angabe von Zeiten; verwenden Sie das 24-Stunden-Format, um Missverständnisse zu vermeiden.