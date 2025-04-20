# [Linux] C Shell (csh) stat Verwendung: Zeigt Dateistatistiken an

## Übersicht
Der `stat`-Befehl wird verwendet, um detaillierte Informationen über Dateien und Verzeichnisse anzuzeigen. Dazu gehören Dateigröße, Berechtigungen, Zeitstempel und andere Metadaten.

## Verwendung
Die grundlegende Syntax des `stat`-Befehls lautet:

```csh
stat [Optionen] [Argumente]
```

## Häufige Optionen
- `-c FORMAT`: Gibt die Ausgabe im angegebenen Format aus.
- `-f FORMAT`: Zeigt die Dateisysteminformationen im angegebenen Format an.
- `-L`: Folgt symbolischen Links und zeigt Informationen über die Zieldatei an.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung des `stat`-Befehls:

1. **Informationen über eine Datei anzeigen:**
   ```csh
   stat dateiname.txt
   ```

2. **Detaillierte Informationen im benutzerdefinierten Format anzeigen:**
   ```csh
   stat -c '%n: %s bytes, last modified: %y' dateiname.txt
   ```

3. **Informationen über ein Verzeichnis anzeigen:**
   ```csh
   stat /pfad/zum/verzeichnis
   ```

4. **Symbolische Links folgen:**
   ```csh
   stat -L linkname
   ```

## Tipps
- Verwenden Sie die `-c`-Option, um die Ausgabe an Ihre Bedürfnisse anzupassen und nur die benötigten Informationen anzuzeigen.
- Nutzen Sie `man stat`, um die vollständige Dokumentation und alle verfügbaren Optionen zu lesen.
- Achten Sie darauf, dass die Dateipfade korrekt sind, um Fehler zu vermeiden.