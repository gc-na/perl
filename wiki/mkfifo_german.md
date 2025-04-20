# [Linux] C Shell (csh) mkfifo: Erstellen von benannten Pipes

## Übersicht
Der Befehl `mkfifo` wird verwendet, um benannte Pipes (FIFO) in einem Unix-ähnlichen Betriebssystem zu erstellen. Eine benannte Pipe ermöglicht die Kommunikation zwischen Prozessen, indem sie Daten in einem First-In-First-Out (FIFO) Format überträgt.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```csh
mkfifo [Optionen] [Argumente]
```

## Häufige Optionen
- `-m, --mode`: Setzt die Berechtigungen für die erstellte Pipe.
- `-Z, --context`: Setzt den Sicherheitskontext für die Pipe (nützlich in SELinux-Umgebungen).

## Häufige Beispiele
Hier sind einige praktische Beispiele zur Verwendung von `mkfifo`:

### Beispiel 1: Erstellen einer einfachen benannten Pipe
```csh
mkfifo meine_pipe
```

### Beispiel 2: Erstellen einer benannten Pipe mit bestimmten Berechtigungen
```csh
mkfifo -m 660 meine_pipe
```

### Beispiel 3: Verwenden der benannten Pipe in einem Skript
```csh
mkfifo meine_pipe
cat meine_pipe &
echo "Hallo, Welt!" > meine_pipe
```

### Beispiel 4: Erstellen mehrerer benannter Pipes
```csh
mkfifo pipe1 pipe2 pipe3
```

## Tipps
- Stellen Sie sicher, dass Sie die Pipe schließen, nachdem Sie mit ihr fertig sind, um Ressourcen freizugeben.
- Überprüfen Sie die Berechtigungen der Pipe, um sicherzustellen, dass die richtigen Prozesse darauf zugreifen können.
- Verwenden Sie benannte Pipes in Skripten, um die Kommunikation zwischen verschiedenen Prozessen zu erleichtern.