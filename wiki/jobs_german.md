# [Linux] C Shell (csh) jobs Verwendung: Zeigt die laufenden Jobs an

## Übersicht
Der Befehl `jobs` in der C Shell (csh) wird verwendet, um eine Liste der aktuell laufenden oder angehaltenen Jobs im Hintergrund anzuzeigen. Dies ist besonders nützlich, um den Status von Prozessen zu überwachen, die Sie in der aktuellen Shell-Sitzung gestartet haben.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```csh
jobs [optionen] [argumente]
```

## Häufige Optionen
- `-l`: Zeigt die Prozess-ID (PID) der Jobs an.
- `-n`: Zeigt nur die Jobs an, die seit dem letzten Aufruf von `jobs` geändert wurden.
- `-p`: Gibt nur die Prozess-IDs der Jobs aus.

## Häufige Beispiele
Hier sind einige praktische Beispiele zur Verwendung des Befehls `jobs`:

1. **Einfaches Auflisten der Jobs:**
   ```csh
   jobs
   ```

2. **Auflisten der Jobs mit Prozess-IDs:**
   ```csh
   jobs -l
   ```

3. **Auflisten der Jobs, die seit dem letzten Aufruf geändert wurden:**
   ```csh
   jobs -n
   ```

4. **Auflisten nur der Prozess-IDs:**
   ```csh
   jobs -p
   ```

## Tipps
- Verwenden Sie `jobs` regelmäßig, um den Überblick über Ihre laufenden Prozesse zu behalten.
- Kombinieren Sie `jobs` mit anderen Befehlen wie `fg` oder `bg`, um Jobs in den Vordergrund oder Hintergrund zu verschieben.
- Achten Sie darauf, dass `jobs` nur die Prozesse anzeigt, die in der aktuellen Shell-Sitzung gestartet wurden.