# [Linux] C Shell (csh) trap Verwendung: Behandeln von Signalen

## Übersicht
Der `trap` Befehl in C Shell (csh) wird verwendet, um bestimmte Signale zu behandeln und Aktionen auszuführen, wenn diese Signale empfangen werden. Dies ist besonders nützlich, um Skripte sauber zu beenden oder um spezifische Aufgaben auszuführen, bevor ein Skript beendet wird.

## Verwendung
Die grundlegende Syntax des `trap` Befehls lautet:

```csh
trap [Aktion] [Signal]
```

## Häufige Optionen
- `INT`: Behandelt das Interrupt-Signal (z.B. durch Drücken von Ctrl+C).
- `TERM`: Behandelt das Terminationssignal, das oft verwendet wird, um Prozesse zu beenden.
- `EXIT`: Führt eine Aktion aus, wenn das Skript beendet wird, unabhängig vom Grund.

## Häufige Beispiele

### Beispiel 1: Interrupt-Signal behandeln
Um eine Nachricht auszugeben, wenn das Skript mit Ctrl+C unterbrochen wird:

```csh
trap 'echo "Skript wurde unterbrochen."' INT
```

### Beispiel 2: Aufräumarbeiten bei Skriptende
Um beim Beenden des Skripts eine Aufräumaktion durchzuführen:

```csh
trap 'rm -f temp.txt; echo "Temporäre Dateien gelöscht."' EXIT
```

### Beispiel 3: Terminationssignal behandeln
Um eine spezifische Aktion auszuführen, wenn das Skript mit einem Terminationssignal beendet wird:

```csh
trap 'echo "Skript wird beendet."' TERM
```

## Tipps
- Verwenden Sie `trap` in langen Skripten, um sicherzustellen, dass wichtige Aufräumarbeiten immer ausgeführt werden.
- Testen Sie Ihre `trap`-Befehle gründlich, um sicherzustellen, dass sie in allen Szenarien wie gewünscht funktionieren.
- Seien Sie vorsichtig mit der Verwendung von `trap` in interaktiven Shells, da es das normale Verhalten der Shell beeinflussen kann.