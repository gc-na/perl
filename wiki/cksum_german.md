# [Linux] C Shell (csh) cksum: Berechnung von Prüfziffern

## Übersicht
Der Befehl `cksum` wird verwendet, um die Prüfziffer (Checksumme) und die Byteanzahl einer Datei zu berechnen. Diese Prüfziffer kann nützlich sein, um die Integrität von Dateien zu überprüfen.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```csh
cksum [Optionen] [Argumente]
```

## Häufige Optionen
- `-a, --algorithm=ALGORITHM`: Gibt den Algorithmus an, der zur Berechnung der Prüfziffer verwendet werden soll.
- `-h, --help`: Zeigt eine Hilfe-Seite mit Informationen zur Verwendung des Befehls an.
- `-V, --version`: Gibt die Versionsnummer des Befehls aus.

## Häufige Beispiele
Hier sind einige praktische Beispiele zur Verwendung von `cksum`:

1. **Berechnung der Prüfziffer einer Datei:**
   ```csh
   cksum datei.txt
   ```

2. **Berechnung der Prüfziffer mehrerer Dateien:**
   ```csh
   cksum datei1.txt datei2.txt
   ```

3. **Verwendung einer bestimmten Prüfziffer-Algorithmus:**
   ```csh
   cksum -a crc32 datei.txt
   ```

4. **Hilfe zur Verwendung des Befehls anzeigen:**
   ```csh
   cksum --help
   ```

## Tipps
- Verwenden Sie `cksum`, um sicherzustellen, dass Dateien während der Übertragung nicht beschädigt wurden.
- Speichern Sie die Ausgabe von `cksum` in einer Datei, um spätere Vergleiche zu ermöglichen.
- Nutzen Sie die Option `--version`, um sicherzustellen, dass Sie die neueste Version des Befehls verwenden, die möglicherweise neue Funktionen bietet.