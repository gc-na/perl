# [Linux] C Shell (csh) top Nutzung: Zeigt laufende Prozesse an

## Übersicht
Der Befehl `top` ist ein leistungsfähiges Tool zur Überwachung von Prozessen auf einem Unix-ähnlichen Betriebssystem. Es zeigt eine dynamische Ansicht der laufenden Prozesse und deren Ressourcennutzung in Echtzeit an.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```
top [Optionen] [Argumente]
```

## Häufige Optionen
- `-d <Sekunden>`: Legt die Aktualisierungsrate in Sekunden fest.
- `-p <PID>`: Zeigt nur die Prozesse mit der angegebenen Prozess-ID an.
- `-u <Benutzer>`: Filtert die Anzeige auf Prozesse eines bestimmten Benutzers.

## Häufige Beispiele
Um die Standardansicht von `top` zu starten, geben Sie einfach ein:

```bash
top
```

Um die Aktualisierungsrate auf 2 Sekunden zu setzen, verwenden Sie:

```bash
top -d 2
```

Um nur die Prozesse eines bestimmten Benutzers, z.B. `alice`, anzuzeigen, verwenden Sie:

```bash
top -u alice
```

Um einen bestimmten Prozess mit der PID 1234 zu überwachen, geben Sie ein:

```bash
top -p 1234
```

## Tipps
- Nutzen Sie die interaktive Steuerung von `top`, um Prozesse zu sortieren oder zu beenden. Drücken Sie `h` für Hilfe innerhalb der Anwendung.
- Um die Ansicht zu beenden, drücken Sie `q`.
- Experimentieren Sie mit verschiedenen Optionen, um die für Ihre Bedürfnisse beste Ansicht zu finden.