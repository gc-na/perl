# [Linux] C Shell (csh) sed Verwendung: Textbearbeitung im Stream

## Übersicht
Der `sed`-Befehl ist ein Stream-Editor, der verwendet wird, um Text in einer Datei oder von der Standardeingabe zu bearbeiten. Er ermöglicht es, Textmuster zu suchen, zu ersetzen, zu löschen oder zu ändern, ohne die ursprüngliche Datei zu verändern, es sei denn, dies wird ausdrücklich angegeben.

## Verwendung
Die grundlegende Syntax des `sed`-Befehls lautet:

```bash
sed [Optionen] [Argumente]
```

## Häufige Optionen
- `-e`: Ermöglicht das Angeben mehrerer Bearbeitungsanweisungen.
- `-i`: Ändert die Datei direkt (in-place).
- `-n`: Unterdrückt die Standardausgabe; nur explizit angegebene Ausgaben werden angezeigt.
- `s`: Steht für "substitute" und wird verwendet, um Textmuster zu ersetzen.

## Häufige Beispiele

### 1. Einfaches Ersetzen
Um das Wort "alt" durch "neu" in einer Datei zu ersetzen:

```bash
sed 's/alt/neu/' datei.txt
```

### 2. Ersetzen in der Datei
Um das Wort "alt" durch "neu" direkt in der Datei zu ersetzen:

```bash
sed -i 's/alt/neu/' datei.txt
```

### 3. Mehrere Ersetzungen
Um mehrere Ersetzungen in einer Zeile durchzuführen:

```bash
sed -e 's/alt/neu/' -e 's/test/probe/' datei.txt
```

### 4. Zeilen löschen
Um alle Zeilen zu löschen, die das Wort "löschen" enthalten:

```bash
sed '/löschen/d' datei.txt
```

### 5. Nur bestimmte Zeilen anzeigen
Um nur die Zeilen 2 bis 4 einer Datei anzuzeigen:

```bash
sed -n '2,4p' datei.txt
```

## Tipps
- Teste deine `sed`-Befehle zuerst ohne die `-i`-Option, um sicherzustellen, dass die gewünschten Änderungen korrekt sind.
- Nutze reguläre Ausdrücke für komplexere Suchmuster.
- Speichere häufig verwendete `sed`-Befehle in Skripten, um die Wiederverwendbarkeit zu erhöhen.