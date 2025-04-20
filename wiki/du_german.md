# [Linux] C Shell (csh) du: Speicherplatznutzung anzeigen

## Übersicht
Der `du`-Befehl (Disk Usage) wird verwendet, um die Speicherplatznutzung von Dateien und Verzeichnissen im Dateisystem anzuzeigen. Er hilft Benutzern, den Speicherplatzverbrauch zu überwachen und zu verwalten.

## Verwendung
Die grundlegende Syntax des `du`-Befehls lautet:

```
du [Optionen] [Argumente]
```

## Häufige Optionen
- `-h`: Gibt die Ausgabe in einem menschenlesbaren Format (z.B. KB, MB) aus.
- `-s`: Zeigt nur die Gesamtsumme der angegebenen Verzeichnisse an.
- `-a`: Listet alle Dateien und Verzeichnisse auf, nicht nur die Verzeichnisse.
- `-c`: Gibt eine Gesamtsumme für alle angegebenen Argumente aus.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung des `du`-Befehls:

1. **Speicherplatznutzung eines Verzeichnisses anzeigen:**
   ```bash
   du /pfad/zum/verzeichnis
   ```

2. **Menschenlesbare Ausgabe der Speicherplatznutzung:**
   ```bash
   du -h /pfad/zum/verzeichnis
   ```

3. **Gesamtsumme der Speicherplatznutzung eines Verzeichnisses anzeigen:**
   ```bash
   du -sh /pfad/zum/verzeichnis
   ```

4. **Speicherplatznutzung aller Dateien und Verzeichnisse im aktuellen Verzeichnis:**
   ```bash
   du -a
   ```

5. **Gesamtsumme für mehrere Verzeichnisse anzeigen:**
   ```bash
   du -ch /pfad/zum/verzeichnis1 /pfad/zum/verzeichnis2
   ```

## Tipps
- Verwenden Sie die Option `-h`, um die Ausgabe leichter lesbar zu machen.
- Kombinieren Sie `-s` mit `-h`, um eine schnelle Übersicht über die Größe von Verzeichnissen zu erhalten.
- Nutzen Sie `du` regelmäßig, um den Speicherplatzverbrauch im Auge zu behalten und unnötige Dateien zu identifizieren.