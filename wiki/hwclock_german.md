# [Linux] C Shell (csh) hwclock Verwendung: Uhrzeit und Datum verwalten

## Übersicht
Der Befehl `hwclock` wird verwendet, um die Hardware-Uhr eines Computers zu lesen und zu setzen. Diese Uhr bleibt auch dann aktiv, wenn der Computer ausgeschaltet ist, und ist nützlich, um die Systemzeit beim Booten korrekt einzustellen.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```
hwclock [Optionen] [Argumente]
```

## Häufige Optionen
- `--show` oder `-r`: Zeigt die aktuelle Zeit der Hardware-Uhr an.
- `--set` oder `-w`: Setzt die Hardware-Uhr auf die aktuelle Systemzeit.
- `--hctosys`: Synchronisiert die Systemzeit mit der Hardware-Uhr.
- `--systohc`: Setzt die Hardware-Uhr auf die aktuelle Systemzeit.

## Häufige Beispiele
Um die aktuelle Zeit der Hardware-Uhr anzuzeigen, verwenden Sie:

```bash
hwclock --show
```

Um die Hardware-Uhr auf die aktuelle Systemzeit zu setzen, führen Sie aus:

```bash
hwclock --set --date="2023-10-01 12:00:00"
```

Um die Systemzeit mit der Hardware-Uhr zu synchronisieren, verwenden Sie:

```bash
hwclock --hctosys
```

Um die Hardware-Uhr auf die aktuelle Systemzeit zu setzen, verwenden Sie:

```bash
hwclock --systohc
```

## Tipps
- Stellen Sie sicher, dass die Systemzeit korrekt ist, bevor Sie die Hardware-Uhr setzen.
- Verwenden Sie `hwclock --show`, um regelmäßig die Zeit der Hardware-Uhr zu überprüfen.
- Führen Sie `hwclock` mit Root-Rechten aus, um Berechtigungsprobleme zu vermeiden.