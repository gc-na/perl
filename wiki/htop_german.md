# [Linux] C Shell (csh) htop Verwendung: Prozessüberwachung und -verwaltung

## Übersicht
Der Befehl `htop` ist ein interaktives Prozessüberwachungswerkzeug, das eine benutzerfreundliche Alternative zu dem traditionellen `top`-Befehl bietet. Mit `htop` können Benutzer die Systemressourcennutzung in Echtzeit überwachen und Prozesse verwalten, indem sie sie einfach auswählen und steuern.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```csh
htop [Optionen] [Argumente]
```

## Häufige Optionen
- `-h`, `--help`: Zeigt die Hilfe und die verfügbaren Optionen an.
- `-s`, `--sort`: Sortiert die angezeigten Prozesse nach dem angegebenen Kriterium (z.B. CPU, RAM).
- `-p`, `--pid`: Zeigt nur die Prozesse mit den angegebenen Prozess-IDs an.
- `-u`, `--user`: Filtert die Prozesse nach dem angegebenen Benutzer.

## Häufige Beispiele
Hier sind einige praktische Beispiele zur Verwendung von `htop`:

1. **Einfaches Starten von htop**:
   ```csh
   htop
   ```

2. **Sortieren nach CPU-Nutzung**:
   ```csh
   htop -s PERCENT_CPU
   ```

3. **Anzeigen von Prozessen eines bestimmten Benutzers**:
   ```csh
   htop -u username
   ```

4. **Anzeigen von spezifischen Prozessen anhand ihrer PID**:
   ```csh
   htop -p 1234,5678
   ```

## Tipps
- Nutzen Sie die Pfeiltasten, um durch die Liste der Prozesse zu navigieren.
- Drücken Sie `F9`, um einen Prozess zu beenden, und wählen Sie das entsprechende Signal aus.
- Verwenden Sie `F3`, um nach einem bestimmten Prozess zu suchen, und `F4`, um zu filtern.
- Passen Sie die Anzeige an, indem Sie `F2` drücken, um die Einstellungen zu öffnen und verschiedene Optionen zu konfigurieren.