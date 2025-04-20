# [Linux] C Shell (csh) Skriptverwendung: Aufzeichnen von Terminal-Sitzungen

## Übersicht
Der Befehl `script` wird verwendet, um eine Terminal-Sitzung aufzuzeichnen. Er erstellt eine Datei, in der alle Eingaben und Ausgaben während der Sitzung gespeichert werden. Dies ist besonders nützlich für die Dokumentation von Prozessen oder das Teilen von Sitzungen mit anderen.

## Verwendung
Die grundlegende Syntax des Befehls `script` lautet:

```csh
script [Optionen] [Dateiname]
```

## Häufige Optionen
- `-a`: Fügt die Ausgabe an eine bestehende Datei an, anstatt sie zu überschreiben.
- `-q`: Unterdrückt die Ausgabe von Start- und Endenachrichten.
- `-t`: Erstellt eine Timing-Datei, die die Zeitstempel der Eingaben und Ausgaben aufzeichnet.

## Häufige Beispiele

1. **Aufzeichnen einer Sitzung in einer Datei:**
   ```csh
   script aufzeichnung.txt
   ```
   Dieser Befehl startet die Aufzeichnung und speichert sie in der Datei `aufzeichnung.txt`.

2. **Anfügen an eine bestehende Aufzeichnungsdatei:**
   ```csh
   script -a aufzeichnung.txt
   ```
   Hier wird die Sitzung an die bestehende Datei `aufzeichnung.txt` angehängt.

3. **Aufzeichnen ohne Start- und Endenachrichten:**
   ```csh
   script -q aufzeichnung.txt
   ```
   Mit dieser Option wird die Aufzeichnung ohne zusätzliche Nachrichten gestartet.

4. **Aufzeichnung mit Timing-Informationen:**
   ```csh
   script -t timing.txt aufzeichnung.txt
   ```
   Dieser Befehl speichert die Sitzung in `aufzeichnung.txt` und erstellt eine Timing-Datei `timing.txt`.

## Tipps
- Verwenden Sie die `-q`-Option, wenn Sie eine saubere Aufzeichnung ohne Ablenkungen wünschen.
- Überprüfen Sie die Berechtigungen der Datei, um sicherzustellen, dass Sie die Aufzeichnung später lesen können.
- Nutzen Sie die `-a`-Option, um mehrere Sitzungen in einer Datei zu kombinieren, was die Nachverfolgbarkeit erleichtert.