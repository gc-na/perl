# [Linux] C Shell (csh) mtr Verwendung: Netzwerkverbindung testen

## Übersicht
Der Befehl `mtr` (My Traceroute) kombiniert die Funktionen von `ping` und `traceroute`, um die Netzwerkverbindung zu einem Ziel zu überprüfen. Er zeigt die Route und die Zeit, die Pakete benötigen, um zu ihrem Ziel zu gelangen, sowie die Paketverluste auf jedem Hop.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```
mtr [Optionen] [Ziel]
```

## Häufige Optionen
- `-r`: Führt einen einmaligen Test durch und gibt die Ergebnisse in einem Bericht aus.
- `-c <Anzahl>`: Gibt die Anzahl der gesendeten Pakete an.
- `-i <Intervall>`: Setzt das Intervall zwischen den gesendeten Paketen in Sekunden.
- `-p`: Zeigt die Ports der Zielhosts an.

## Häufige Beispiele
Hier sind einige praktische Beispiele zur Verwendung von `mtr`:

1. **Einfacher Test zu einem Ziel:**
   ```bash
   mtr example.com
   ```

2. **Einmaliger Bericht über die Verbindung:**
   ```bash
   mtr -r example.com
   ```

3. **Test mit einer bestimmten Anzahl von Paketen:**
   ```bash
   mtr -c 10 example.com
   ```

4. **Test mit einem Intervall von 1 Sekunde:**
   ```bash
   mtr -i 1 example.com
   ```

5. **Test, der auch die Ports anzeigt:**
   ```bash
   mtr -p example.com
   ```

## Tipps
- Verwenden Sie die Option `-r`, wenn Sie eine schnelle Übersicht über die Verbindung wünschen, ohne die kontinuierliche Ausgabe.
- Kombinieren Sie die Optionen, um spezifische Tests durchzuführen, z.B. `mtr -c 5 -i 2 example.com`, um alle 2 Sekunden 5 Pakete zu senden.
- Achten Sie darauf, dass einige Netzwerke ICMP-Pakete blockieren können, was die Ergebnisse von `mtr` beeinflussen kann.