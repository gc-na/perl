# [Linux] C Shell (csh) pr: Textdateien formatieren und drucken

## Übersicht
Der Befehl `pr` wird verwendet, um Textdateien für die Ausgabe auf dem Bildschirm oder für den Druck zu formatieren. Er kann Text in Spalten anordnen, Seitenzahlen hinzufügen und die Ausgabe für eine bessere Lesbarkeit anpassen.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```
pr [Optionen] [Argumente]
```

## Häufige Optionen
- `-h`: Fügt eine Kopfzeile hinzu.
- `-l`: Legt die Anzahl der Zeilen pro Seite fest.
- `-w`: Bestimmt die Breite der Ausgabe in Zeichen.
- `-s`: Gibt ein Trennzeichen für die Spalten an.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung des `pr`-Befehls:

1. **Einfaches Formatieren einer Textdatei:**
   ```csh
   pr datei.txt
   ```

2. **Formatieren mit einer Kopfzeile:**
   ```csh
   pr -h "Mein Dokument" datei.txt
   ```

3. **Festlegen der Zeilen pro Seite:**
   ```csh
   pr -l 50 datei.txt
   ```

4. **Ausgabe in zwei Spalten:**
   ```csh
   pr -2 datei.txt
   ```

5. **Festlegen der Breite der Ausgabe:**
   ```csh
   pr -w 80 datei.txt
   ```

## Tipps
- Verwenden Sie die Option `-h`, um Ihre Ausgaben klarer zu gestalten, insbesondere bei längeren Dokumenten.
- Experimentieren Sie mit der Zeilenanzahl und Breite, um die Lesbarkeit auf verschiedenen Ausgabegeräten zu optimieren.
- Nutzen Sie die Ausgabe von `pr` in Kombination mit anderen Befehlen, wie `less`, um große Dateien besser zu durchsuchen.