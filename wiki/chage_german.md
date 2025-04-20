# [Linux] C Shell (csh) chage Verwendung: Benutzerpasswortalter verwalten

## Übersicht
Der Befehl `chage` wird verwendet, um die Passwortablauf- und Änderungsrichtlinien für Benutzerkonten in einem Linux-System zu verwalten. Mit `chage` können Administratoren festlegen, wie oft ein Benutzer sein Passwort ändern muss und wann das Passwort abläuft.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
chage [Optionen] [Argumente]
```

## Häufige Optionen
- `-l, --list`: Zeigt die aktuellen Passwortablaufinformationen für den angegebenen Benutzer an.
- `-m, --mindays`: Legt die minimale Anzahl von Tagen fest, die zwischen Passwortänderungen liegen müssen.
- `-M, --maxdays`: Legt die maximale Anzahl von Tagen fest, nach denen das Passwort abläuft.
- `-I, --inactive`: Legt die Anzahl der Tage fest, nach denen das Konto inaktiv wird, nachdem das Passwort abgelaufen ist.
- `-E, --expire`: Legt das Datum fest, an dem das Benutzerkonto abläuft.

## Häufige Beispiele
- Um die Passwortablaufinformationen für einen Benutzer namens `max` anzuzeigen:

```bash
chage -l max
```

- Um die minimale Anzahl von Tagen zwischen Passwortänderungen für den Benutzer `max` auf 5 festzulegen:

```bash
chage -m 5 max
```

- Um die maximale Anzahl von Tagen für das Passwort von `max` auf 90 Tage einzustellen:

```bash
chage -M 90 max
```

- Um das Konto von `max` nach 30 Tagen Inaktivität ablaufen zu lassen:

```bash
chage -I 30 max
```

- Um das Ablaufdatum des Kontos von `max` auf den 1. Januar 2024 festzulegen:

```bash
chage -E 2024-01-01 max
```

## Tipps
- Überprüfen Sie regelmäßig die Passwortablaufinformationen, um sicherzustellen, dass Benutzer ihre Passwörter rechtzeitig ändern.
- Verwenden Sie die `-l` Option, um eine Übersicht über die aktuellen Einstellungen zu erhalten, bevor Sie Änderungen vornehmen.
- Stellen Sie sicher, dass die Richtlinien für Passwortänderungen den Sicherheitsanforderungen Ihrer Organisation entsprechen.