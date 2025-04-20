# [Linux] C Shell (csh) strace Verwendung: Systemaufrufe verfolgen

## Übersicht
Der Befehl `strace` wird verwendet, um die Systemaufrufe und Signale eines Prozesses zu verfolgen. Dies ist besonders nützlich für die Fehlersuche und das Debugging von Programmen, da es Einblicke in die Interaktionen eines Programms mit dem Betriebssystem bietet.

## Verwendung
Die grundlegende Syntax des `strace`-Befehls lautet:

```csh
strace [Optionen] [Argumente]
```

## Häufige Optionen
- `-p <PID>`: Verfolgt einen bereits laufenden Prozess mit der angegebenen Prozess-ID (PID).
- `-e <Ausdruck>`: Filtert die Systemaufrufe, die verfolgt werden sollen, basierend auf dem angegebenen Ausdruck.
- `-o <Dateiname>`: Leitet die Ausgabe in die angegebene Datei um, anstatt sie auf dem Bildschirm anzuzeigen.
- `-c`: Gibt eine Zusammenfassung der Systemaufrufe und deren Häufigkeit aus, anstatt die vollständigen Details anzuzeigen.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `strace`:

1. Verfolgen eines neuen Prozesses:
   ```csh
   strace ls
   ```

2. Verfolgen eines laufenden Prozesses mit der PID 1234:
   ```csh
   strace -p 1234
   ```

3. Ausgabe der Systemaufrufe in eine Datei umleiten:
   ```csh
   strace -o ausgabe.txt cat datei.txt
   ```

4. Nur die `open` und `close` Systemaufrufe verfolgen:
   ```csh
   strace -e trace=open,close ls
   ```

5. Zusammenfassung der Systemaufrufe anzeigen:
   ```csh
   strace -c ls
   ```

## Tipps
- Verwenden Sie `strace` mit Bedacht, da es die Leistung des Programms beeinträchtigen kann.
- Kombinieren Sie `strace` mit anderen Debugging-Tools, um umfassendere Einblicke zu erhalten.
- Überprüfen Sie die Ausgaben sorgfältig, um Muster oder Fehler in den Systemaufrufen zu identifizieren.