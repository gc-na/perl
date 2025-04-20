# [Linux] C Shell (csh) renice Verwendung: Ändern der Priorität von Prozessen

## Übersicht
Der Befehl `renice` wird verwendet, um die Priorität eines oder mehrerer laufender Prozesse in einem Unix-ähnlichen Betriebssystem zu ändern. Dies kann nützlich sein, um die Systemressourcen für bestimmte Anwendungen zu optimieren.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```csh
renice [Optionen] [Argumente]
```

## Häufige Optionen
- `-n`: Gibt den neuen Nice-Wert an. Ein höherer Wert bedeutet eine niedrigere Priorität.
- `-p`: Gibt die Prozess-ID (PID) an, deren Priorität geändert werden soll.
- `-g`: Ändert die Priorität aller Prozesse einer bestimmten Gruppe.
- `-u`: Ändert die Priorität aller Prozesse eines bestimmten Benutzers.

## Häufige Beispiele
Um die Priorität eines Prozesses mit der PID 1234 auf 10 zu setzen, verwenden Sie:

```csh
renice -n 10 -p 1234
```

Um die Priorität aller Prozesse eines bestimmten Benutzers (z. B. `benutzername`) auf 5 zu ändern, verwenden Sie:

```csh
renice -n 5 -u benutzername
```

Um die Priorität aller Prozesse einer bestimmten Gruppe (z. B. mit der GID 1001) auf 15 zu ändern, verwenden Sie:

```csh
renice -n 15 -g 1001
```

## Tipps
- Verwenden Sie `renice` mit Bedacht, da das Setzen einer zu niedrigen Priorität dazu führen kann, dass wichtige Prozesse nicht genügend Ressourcen erhalten.
- Überprüfen Sie die aktuelle Priorität eines Prozesses mit dem Befehl `ps` oder `top`, bevor Sie `renice` verwenden.
- Beachten Sie, dass nur der Benutzer oder der Root-Benutzer die Priorität eines Prozesses ändern kann, den er nicht gestartet hat.