# [Linux] C Shell (csh) comm Befehl: Vergleicht zwei sortierte Dateien

## Übersicht
Der `comm` Befehl wird verwendet, um zwei sortierte Dateien zu vergleichen und die Unterschiede sowie die gemeinsamen Zeilen anzuzeigen. Er gibt die Inhalte der beiden Dateien in drei Spalten aus: nur in der ersten Datei, nur in der zweiten Datei und in beiden Dateien.

## Verwendung
Die grundlegende Syntax des `comm` Befehls lautet:

```csh
comm [Optionen] [Datei1] [Datei2]
```

## Häufige Optionen
- `-1`: Unterdrückt die Ausgabe der Zeilen, die nur in der ersten Datei vorhanden sind.
- `-2`: Unterdrückt die Ausgabe der Zeilen, die nur in der zweiten Datei vorhanden sind.
- `-3`: Unterdrückt die Ausgabe der Zeilen, die in beiden Dateien vorhanden sind.
- `-i`: Ignoriert Groß- und Kleinschreibung beim Vergleich.

## Häufige Beispiele

1. **Vergleich von zwei Dateien**:
   ```csh
   comm datei1.txt datei2.txt
   ```

2. **Nur die Zeilen anzeigen, die in der ersten Datei vorhanden sind**:
   ```csh
   comm -13 datei1.txt datei2.txt
   ```

3. **Nur die Zeilen anzeigen, die in der zweiten Datei vorhanden sind**:
   ```csh
   comm -12 datei1.txt datei2.txt
   ```

4. **Vergleich unter Ignorierung der Groß- und Kleinschreibung**:
   ```csh
   comm -i datei1.txt datei2.txt
   ```

## Tipps
- Stellen Sie sicher, dass die Dateien vor der Verwendung von `comm` sortiert sind, da der Befehl nur mit sortierten Eingaben korrekt funktioniert.
- Nutzen Sie die Optionen, um die Ausgabe an Ihre Bedürfnisse anzupassen und nur die relevanten Informationen anzuzeigen.
- Es kann hilfreich sein, die Ausgaben in eine Datei umzuleiten, um die Ergebnisse später zu analysieren, z.B. `comm datei1.txt datei2.txt > ergebnis.txt`.