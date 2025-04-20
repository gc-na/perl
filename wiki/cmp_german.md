# [Linux] C Shell (csh) cmp Verwendung: Vergleicht zwei Dateien

## Übersicht
Der `cmp` Befehl wird verwendet, um zwei Dateien byteweise zu vergleichen. Er zeigt an, ob die Dateien identisch sind oder, falls nicht, die Position des ersten Unterschieds.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```
cmp [Optionen] [Argumente]
```

## Häufige Optionen
- `-l`: Gibt die Unterschiede in einer numerischen Form aus.
- `-s`: Stille Ausgabe; gibt nur den Exit-Status zurück, ohne Ausgaben.
- `-i`: Ignoriert die ersten N Bytes der Dateien.

## Häufige Beispiele

1. **Einfacher Vergleich von zwei Dateien:**
   ```bash
   cmp datei1.txt datei2.txt
   ```

2. **Vergleich mit stiller Ausgabe:**
   ```bash
   cmp -s datei1.txt datei2.txt
   ```

3. **Unterschiede in numerischer Form anzeigen:**
   ```bash
   cmp -l datei1.txt datei2.txt
   ```

4. **Die ersten 10 Bytes ignorieren:**
   ```bash
   cmp -i 10 datei1.txt datei2.txt
   ```

## Tipps
- Verwenden Sie die Option `-s`, wenn Sie nur wissen möchten, ob die Dateien unterschiedlich sind, ohne Details zu sehen.
- Nutzen Sie `cmp` in Skripten, um automatisierte Vergleiche durchzuführen und entsprechende Aktionen basierend auf den Ergebnissen auszulösen.
- Denken Sie daran, dass `cmp` nur für binäre und Textdateien geeignet ist; für komplexere Vergleiche könnte ein anderer Befehl wie `diff` nützlicher sein.