# [Linux] C Shell (csh) sha512sum Verwendung: Berechnung von SHA-512-Prüfziffern

## Übersicht
Der Befehl `sha512sum` wird verwendet, um den SHA-512-Hash eines oder mehrerer Dateien zu berechnen. Dies ist nützlich, um die Integrität von Dateien zu überprüfen oder um sicherzustellen, dass Dateien nicht verändert wurden.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```csh
sha512sum [Optionen] [Argumente]
```

## Häufige Optionen
- `-b`: Berechnet den Hash für Binärdateien.
- `-c`: Überprüft die Hash-Werte in einer Datei.
- `-h`: Zeigt eine Hilfe mit Informationen zur Verwendung des Befehls an.
- `--tag`: Fügt einen Tag zu den Ausgaben hinzu.

## Häufige Beispiele
1. **Berechnung des SHA-512-Hashes einer Datei:**
   ```csh
   sha512sum datei.txt
   ```

2. **Berechnung des SHA-512-Hashes mehrerer Dateien:**
   ```csh
   sha512sum datei1.txt datei2.txt
   ```

3. **Überprüfung von Hash-Werten aus einer Datei:**
   Angenommen, Sie haben eine Datei `hashes.txt`, die Hash-Werte enthält:
   ```csh
   sha512sum -c hashes.txt
   ```

4. **Berechnung des Hashes für eine Binärdatei:**
   ```csh
   sha512sum -b datei.bin
   ```

## Tipps
- Verwenden Sie die Option `-c`, um sicherzustellen, dass die Dateien nicht verändert wurden, indem Sie die Hash-Werte mit einer vorher gespeicherten Liste vergleichen.
- Speichern Sie die Ausgabe von `sha512sum` in einer Datei, um später eine Überprüfung durchführen zu können:
  ```csh
  sha512sum datei.txt > hashes.txt
  ```
- Achten Sie darauf, dass die Datei, die Sie überprüfen möchten, im gleichen Verzeichnis wie die Hash-Datei ist, um Fehler zu vermeiden.