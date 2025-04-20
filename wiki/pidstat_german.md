# [Linux] C Shell (csh) pidstat: Überwachung von Prozessstatistiken

## Übersicht
Der Befehl `pidstat` wird verwendet, um die Leistungsstatistiken von Prozessen in einem Linux-System zu überwachen. Er zeigt Informationen wie CPU-Nutzung, Speicherverbrauch und andere wichtige Leistungsmetriken für laufende Prozesse an.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
pidstat [Optionen] [Argumente]
```

## Häufige Optionen
- `-h`: Zeigt die Statistiken in einem menschenlesbaren Format an.
- `-r`: Zeigt Informationen zur Speichernutzung an.
- `-u`: Zeigt Informationen zur CPU-Nutzung an.
- `-p <PID>`: Überwacht einen bestimmten Prozess anhand seiner Prozess-ID.
- `-t`: Zeigt die Statistiken für alle Threads eines Prozesses an.

## Häufige Beispiele

1. **CPU-Nutzung aller Prozesse anzeigen:**
   ```bash
   pidstat -u
   ```

2. **Speichernutzung eines bestimmten Prozesses anzeigen:**
   ```bash
   pidstat -r -p 1234
   ```

3. **Statistiken für alle Threads eines Prozesses anzeigen:**
   ```bash
   pidstat -t -p 5678
   ```

4. **Statistiken alle 2 Sekunden aktualisieren:**
   ```bash
   pidstat 2
   ```

## Tipps
- Verwenden Sie die Option `-h`, um die Ausgabe leserlicher zu gestalten, insbesondere wenn Sie mit vielen Prozessen arbeiten.
- Kombinieren Sie Optionen, um umfassendere Informationen zu erhalten, z.B. `pidstat -u -r`.
- Nutzen Sie `pidstat` in Skripten zur automatischen Überwachung von Prozessen über längere Zeiträume.