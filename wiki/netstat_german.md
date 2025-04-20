# [Linux] C Shell (csh) netstat Verwendung: Netzwerkverbindungen anzeigen

## Übersicht
Der Befehl `netstat` wird verwendet, um Netzwerkverbindungen, Routing-Tabellen, Schnittstellenstatistiken und andere Netzwerkinformationen anzuzeigen. Er ist ein nützliches Werkzeug zur Diagnose von Netzwerkproblemen und zur Überwachung von Netzwerkaktivitäten.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```csh
netstat [Optionen] [Argumente]
```

## Häufige Optionen
- `-a`: Zeigt alle Verbindungen und Listening-Ports an.
- `-n`: Zeigt Adressen und Portnummern in numerischer Form an, anstatt sie in Namen aufzulösen.
- `-r`: Zeigt die Routing-Tabelle an.
- `-i`: Zeigt Informationen über Netzwerkinterfaces an.
- `-s`: Zeigt Statistiken für verschiedene Protokolle an.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `netstat`:

1. **Alle aktiven Verbindungen anzeigen:**
   ```csh
   netstat -a
   ```

2. **Verbindungen in numerischer Form anzeigen:**
   ```csh
   netstat -an
   ```

3. **Routing-Tabelle anzeigen:**
   ```csh
   netstat -r
   ```

4. **Netzwerkinterfaces und deren Status anzeigen:**
   ```csh
   netstat -i
   ```

5. **Statistiken für TCP-Protokolle anzeigen:**
   ```csh
   netstat -s -p tcp
   ```

## Tipps
- Verwenden Sie die Option `-n`, um die Ausgabe zu beschleunigen, da die Namensauflösung umgangen wird.
- Kombinieren Sie Optionen, um spezifischere Informationen zu erhalten, z. B. `netstat -anr`, um sowohl die aktiven Verbindungen als auch die Routing-Tabelle anzuzeigen.
- Nutzen Sie `grep`, um die Ausgabe nach bestimmten Verbindungen oder Ports zu filtern, z. B. `netstat -an | grep 80`, um nur HTTP-Verbindungen anzuzeigen.