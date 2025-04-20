# [Linux] C Shell (csh) iotop Verwendung: Überwachung der I/O-Nutzung von Prozessen

## Übersicht
Der Befehl `iotop` wird verwendet, um die Ein- und Ausgabe (I/O) Nutzung von Prozessen in Echtzeit zu überwachen. Er zeigt an, welche Prozesse die meisten I/O-Ressourcen beanspruchen, was hilfreich sein kann, um Engpässe oder Probleme im System zu identifizieren.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
iotop [Optionen] [Argumente]
```

## Häufige Optionen
- `-o` oder `--only`: Zeigt nur Prozesse an, die aktuell I/O nutzen.
- `-b` oder `--batch`: Führt `iotop` im Batch-Modus aus, nützlich für Skripte.
- `-d <Sekunden>`: Setzt das Intervall in Sekunden, wie oft die Anzeige aktualisiert wird.
- `-p <PID>`: Überwacht nur den Prozess mit der angegebenen Prozess-ID (PID).

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `iotop`:

1. **Echtzeitüberwachung der I/O-Nutzung:**
   ```bash
   iotop
   ```

2. **Nur Prozesse anzeigen, die I/O nutzen:**
   ```bash
   iotop -o
   ```

3. **Batch-Modus mit 5-Sekunden-Intervall:**
   ```bash
   iotop -b -d 5
   ```

4. **Überwachung eines bestimmten Prozesses mit PID 1234:**
   ```bash
   iotop -p 1234
   ```

## Tipps
- Verwenden Sie `iotop` mit Root-Rechten, um vollständige Informationen über alle Prozesse zu erhalten.
- Nutzen Sie den Batch-Modus, um die Ausgabe in eine Datei zu speichern und später zu analysieren.
- Achten Sie darauf, die Aktualisierungsrate anzupassen, um die Leistung des Systems nicht unnötig zu belasten.