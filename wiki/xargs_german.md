# [Linux] C Shell (csh) xargs Verwendung: Befehle ausführen mit Eingaben von Standard- oder Dateiquellen

## Übersicht
Der Befehl `xargs` wird verwendet, um Eingaben von Standard- oder Dateiquellen zu lesen und diese als Argumente an andere Befehle zu übergeben. Dies ist besonders nützlich, wenn die Anzahl der Argumente, die an einen Befehl übergeben werden, die maximale Anzahl überschreiten könnte, die die Shell verarbeiten kann.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```
xargs [Optionen] [Argumente]
```

## Häufige Optionen
- `-n N`: Gibt an, dass maximal N Argumente an den Befehl übergeben werden sollen.
- `-d DELIMITER`: Legt das Trennzeichen für die Eingabe fest (standardmäßig ist es ein Leerzeichen).
- `-p`: Fragt vor der Ausführung jedes Befehls um Bestätigung.
- `-0`: Erwartet Null-terminierte Eingaben, was nützlich ist, um mit Dateinamen umzugehen, die Leerzeichen enthalten.

## Häufige Beispiele

1. **Dateien mit `find` und `xargs` löschen:**
   ```bash
   find . -name "*.tmp" | xargs rm
   ```
   Dieses Beispiel sucht nach allen `.tmp`-Dateien im aktuellen Verzeichnis und löscht sie.

2. **Dateien mit `xargs` komprimieren:**
   ```bash
   ls *.txt | xargs gzip
   ```
   Hier werden alle `.txt`-Dateien im aktuellen Verzeichnis komprimiert.

3. **Begrenzung der Argumentanzahl:**
   ```bash
   echo "a b c d e" | xargs -n 2
   ```
   Dieses Beispiel gibt die Argumente in Gruppen von zwei aus: `a b` und `c d`.

4. **Verwendung eines benutzerdefinierten Trennzeichens:**
   ```bash
   echo "file1,file2,file3" | xargs -d ',' cp -t /backup/
   ```
   Hier werden die Dateien `file1`, `file2` und `file3` in das Verzeichnis `/backup/` kopiert, wobei das Komma als Trennzeichen verwendet wird.

## Tipps
- Verwenden Sie die Option `-p`, um sicherzustellen, dass Sie vor der Ausführung eines potenziell gefährlichen Befehls um Bestätigung gefragt werden.
- Wenn Sie mit Dateinamen arbeiten, die Leerzeichen oder spezielle Zeichen enthalten, verwenden Sie die Option `-0` zusammen mit `find -print0`, um Probleme zu vermeiden.
- Testen Sie Ihre Befehle zuerst mit `echo`, um zu sehen, welche Argumente übergeben werden, bevor Sie sie tatsächlich ausführen.