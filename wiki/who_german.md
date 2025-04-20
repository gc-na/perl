# [Linux] C Shell (csh) who Verwendung: Zeigt angemeldete Benutzer an

## Übersicht
Der Befehl `who` zeigt eine Liste der Benutzer an, die derzeit am System angemeldet sind. Er liefert Informationen wie Benutzernamen, Terminal, Anmeldezeit und manchmal auch die IP-Adresse des Benutzers.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```
who [Optionen] [Argumente]
```

## Häufige Optionen
- `-b`: Zeigt die letzte Systemstartzeit an.
- `-q`: Gibt nur die Benutzernamen und die Anzahl der angemeldeten Benutzer aus.
- `-H`: Fügt eine Kopfzeile zu den Ausgaben hinzu, die die Spaltenüberschriften beschreibt.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung des `who`-Befehls:

1. **Einfacher Befehl**: Zeigt alle angemeldeten Benutzer an.
   ```csh
   who
   ```

2. **Mit Kopfzeile**: Zeigt die Benutzer mit einer Kopfzeile an.
   ```csh
   who -H
   ```

3. **Letzte Systemstartzeit**: Zeigt die Zeit des letzten Systemstarts an.
   ```csh
   who -b
   ```

4. **Benutzeranzahl**: Zeigt nur die Benutzernamen und die Anzahl der angemeldeten Benutzer an.
   ```csh
   who -q
   ```

## Tipps
- Verwenden Sie `who -H`, um die Ausgabe klarer zu gestalten, insbesondere wenn Sie die Informationen mit anderen teilen.
- Kombinieren Sie `who` mit anderen Befehlen wie `grep`, um nach bestimmten Benutzern zu suchen.
- Nutzen Sie `man who`, um eine vollständige Liste der Optionen und deren Beschreibungen zu erhalten.