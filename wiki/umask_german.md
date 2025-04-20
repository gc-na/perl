# [Linux] C Shell (csh) umask Verwendung: Legt die Standardberechtigungen für neu erstellte Dateien fest

## Übersicht
Der Befehl `umask` in der C Shell (csh) wird verwendet, um die Standardberechtigungen für neu erstellte Dateien und Verzeichnisse festzulegen. Er bestimmt, welche Berechtigungen von den Standardwerten abgezogen werden, wenn eine Datei oder ein Verzeichnis erstellt wird.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```csh
umask [Optionen] [Argumente]
```

## Häufige Optionen
- `-S`: Zeigt die aktuelle umask in symbolischer Form an.
- `-p`: Zeigt die aktuelle umask in numerischer Form an.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung des umask-Befehls:

1. **Aktuelle umask anzeigen:**
   ```csh
   umask
   ```

2. **Umask auf 022 setzen (Schreibberechtigung für den Eigentümer, nur Lese- und Ausführungsberechtigungen für andere):**
   ```csh
   umask 022
   ```

3. **Umask auf 007 setzen (keine Berechtigungen für andere, nur der Eigentümer und die Gruppe haben Zugriff):**
   ```csh
   umask 007
   ```

4. **Aktuelle umask in symbolischer Form anzeigen:**
   ```csh
   umask -S
   ```

5. **Umask auf den Standardwert zurücksetzen (in der Regel 0022):**
   ```csh
   umask 0022
   ```

## Tipps
- Überprüfen Sie regelmäßig Ihre umask-Einstellungen, um sicherzustellen, dass sie den gewünschten Sicherheitsanforderungen entsprechen.
- Setzen Sie die umask in Ihren Startskripten (z.B. `.cshrc`), um konsistente Berechtigungen für alle neuen Dateien und Verzeichnisse zu gewährleisten.
- Seien Sie vorsichtig beim Setzen einer umask, die zu lockere Berechtigungen gewährt, da dies Sicherheitsrisiken verursachen kann.