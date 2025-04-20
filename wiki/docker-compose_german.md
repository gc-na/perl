# [Linux] C Shell (csh) docker-compose Verwendung: Container-Orchestrierung

## Übersicht
Der Befehl `docker-compose` wird verwendet, um Multi-Container-Docker-Anwendungen zu definieren und zu verwalten. Mit einer einfachen YAML-Datei können Sie die Dienste, Netzwerke und Volumes Ihrer Anwendung konfigurieren und starten.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```
docker-compose [optionen] [argumente]
```

## Häufige Optionen
- `up`: Startet die definierten Container.
- `down`: Stoppt und entfernt die Container, Netzwerke und Volumes.
- `build`: Baut die Images für die Dienste.
- `logs`: Zeigt die Protokolle der Container an.
- `exec`: Führt einen Befehl in einem laufenden Container aus.

## Häufige Beispiele
Hier sind einige praktische Beispiele zur Verwendung von `docker-compose`:

1. **Container starten**
   ```bash
   docker-compose up
   ```

2. **Container im Hintergrund starten**
   ```bash
   docker-compose up -d
   ```

3. **Container stoppen und entfernen**
   ```bash
   docker-compose down
   ```

4. **Logs der Container anzeigen**
   ```bash
   docker-compose logs
   ```

5. **Befehl in einem laufenden Container ausführen**
   ```bash
   docker-compose exec <dienstname> <befehl>
   ```

## Tipps
- Verwenden Sie die Option `-d`, um Container im Hintergrund zu starten, was nützlich ist, wenn Sie Ihre Konsole nicht blockieren möchten.
- Halten Sie Ihre `docker-compose.yml`-Datei gut dokumentiert, um die Wartung zu erleichtern.
- Nutzen Sie Umgebungsvariablen in Ihrer `docker-compose.yml`, um Konfigurationen flexibel zu gestalten.