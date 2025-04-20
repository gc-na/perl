# [Linux] C Shell (csh) stty Verwendung: Terminal-Einstellungen ändern

## Übersicht
Der Befehl `stty` wird verwendet, um Terminal-Einstellungen zu ändern und zu konfigurieren. Mit `stty` können Sie verschiedene Parameter des Terminals anpassen, wie z.B. die Eingabe- und Ausgabeoptionen, Steuerzeichen und mehr.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```csh
stty [Optionen] [Argumente]
```

## Häufige Optionen
- `-a`: Zeigt alle aktuellen Einstellungen des Terminals an.
- `-g`: Gibt die aktuellen Einstellungen in einer Form aus, die später mit `stty` wiederhergestellt werden kann.
- `erase <Zeichen>`: Setzt das Zeichen, das zum Löschen eines Zeichens verwendet wird.
- `kill <Zeichen>`: Setzt das Zeichen, das zum Löschen der aktuellen Zeile verwendet wird.
- `intr <Zeichen>`: Setzt das Zeichen, das zum Unterbrechen eines laufenden Prozesses verwendet wird.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `stty`:

1. **Alle Terminal-Einstellungen anzeigen:**
   ```csh
   stty -a
   ```

2. **Das Erase-Zeichen auf Backspace setzen:**
   ```csh
   stty erase ^H
   ```

3. **Das Kill-Zeichen auf Ctrl+U setzen:**
   ```csh
   stty kill ^U
   ```

4. **Das Interrupt-Zeichen auf Ctrl+C setzen:**
   ```csh
   stty intr ^C
   ```

5. **Einstellungen speichern und später wiederherstellen:**
   ```csh
   stty -g > settings.txt
   stty $(<settings.txt)
   ```

## Tipps
- Überprüfen Sie regelmäßig die Terminal-Einstellungen mit `stty -a`, um sicherzustellen, dass alles korrekt konfiguriert ist.
- Seien Sie vorsichtig beim Ändern von Steuerzeichen, da falsche Einstellungen die Bedienung des Terminals beeinträchtigen können.
- Nutzen Sie die Möglichkeit, Einstellungen in einer Datei zu speichern, um sie bei Bedarf schnell wiederherzustellen.