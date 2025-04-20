# [Deutsch] C Shell (csh) Benutzerbefehl: Benutzerinformationen anzeigen

## Übersicht
Der Befehl `users` zeigt die Benutzernamen der aktuell angemeldeten Benutzer im System an. Dies ist nützlich, um schnell zu überprüfen, welche Benutzer gerade aktiv sind.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```
users [optionen] [argumente]
```

## Häufige Optionen
- `-n`: Gibt die Anzahl der angemeldeten Benutzer aus.
- `-r`: Zeigt nur die Benutzernamen der Benutzer an, die auf dem System aktiv sind.

## Häufige Beispiele
Um die Benutzernamen der aktuell angemeldeten Benutzer anzuzeigen, verwenden Sie einfach:

```csh
users
```

Um die Anzahl der angemeldeten Benutzer anzuzeigen, verwenden Sie die Option `-n`:

```csh
users -n
```

Wenn Sie nur die aktiven Benutzer sehen möchten, verwenden Sie die Option `-r`:

```csh
users -r
```

## Tipps
- Verwenden Sie `who` oder `w`, um detailliertere Informationen über die angemeldeten Benutzer zu erhalten, einschließlich ihrer Anmeldezeiten und aktiven Sitzungen.
- Kombinieren Sie den `users` Befehl mit anderen Befehlen in einer Pipeline, um die Ausgabe weiter zu verarbeiten oder zu filtern.