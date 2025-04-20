# [Linux] C Shell (csh) finger Verwendung: Benutzerinformationen anzeigen

## Übersicht
Der Befehl `finger` wird verwendet, um Informationen über Benutzer auf einem System anzuzeigen. Er liefert Details wie den vollständigen Namen, die Anmeldedaten, die letzte Anmeldedauer und andere relevante Informationen.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```
finger [Optionen] [Argumente]
```

## Häufige Optionen
- `-l`: Zeigt eine detaillierte Ausgabe an, die zusätzliche Informationen über den Benutzer enthält.
- `-m`: Sucht nach Benutzernamen, die mit dem angegebenen Muster übereinstimmen.
- `-s`: Gibt eine kurze Zusammenfassung der Benutzerinformationen aus.

## Häufige Beispiele
Um die Informationen für einen bestimmten Benutzer anzuzeigen, verwenden Sie:

```bash
finger benutzername
```

Um eine detaillierte Ausgabe für einen Benutzer zu erhalten, verwenden Sie:

```bash
finger -l benutzername
```

Um alle Benutzer auf dem System aufzulisten:

```bash
finger
```

Um nach Benutzern zu suchen, die einem bestimmten Muster entsprechen:

```bash
finger -m muster
```

## Tipps
- Verwenden Sie `finger` ohne Argumente, um schnell einen Überblick über alle angemeldeten Benutzer zu erhalten.
- Kombinieren Sie `finger` mit anderen Befehlen wie `grep`, um spezifische Informationen zu filtern.
- Beachten Sie, dass nicht alle Systeme den `finger`-Dienst aktiviert haben; überprüfen Sie dies gegebenenfalls mit Ihrem Systemadministrator.