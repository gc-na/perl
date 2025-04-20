# [Linux] C Shell (csh) uniq Verwendung: Doppelte Zeilen entfernen

## Übersicht
Der Befehl `uniq` wird verwendet, um aufeinanderfolgende doppelte Zeilen aus einer Datei oder von der Standardeingabe zu entfernen. Dies ist besonders nützlich, wenn Sie eine Liste von Einträgen haben und nur die einzigartigen Werte behalten möchten.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```csh
uniq [Optionen] [Argumente]
```

## Häufige Optionen
- `-c`: Zählt die Anzahl der Vorkommen jeder Zeile und gibt diese vor der Zeile aus.
- `-d`: Gibt nur die doppelten Zeilen aus.
- `-u`: Gibt nur die einzigartigen Zeilen aus.
- `-i`: Ignoriert Groß- und Kleinschreibung bei der Vergleichung der Zeilen.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `uniq`:

1. **Entfernen von doppelten Zeilen aus einer Datei:**
   ```csh
   uniq datei.txt
   ```

2. **Zählen der Vorkommen jeder Zeile:**
   ```csh
   uniq -c datei.txt
   ```

3. **Anzeigen nur der doppelten Zeilen:**
   ```csh
   uniq -d datei.txt
   ```

4. **Anzeigen nur der einzigartigen Zeilen:**
   ```csh
   uniq -u datei.txt
   ```

5. **Ignorieren der Groß- und Kleinschreibung:**
   ```csh
   uniq -i datei.txt
   ```

## Tipps
- Stellen Sie sicher, dass die Eingabedaten sortiert sind, da `uniq` nur aufeinanderfolgende doppelte Zeilen entfernt. Verwenden Sie den Befehl `sort`, um die Datei vorher zu sortieren.
- Kombinieren Sie `uniq` mit anderen Befehlen, um leistungsstarke Pipelines zu erstellen. Zum Beispiel: 
  ```csh
  sort datei.txt | uniq
  ```
- Nutzen Sie die Option `-c`, um schnell zu sehen, wie oft jede Zeile vorkommt, was hilfreich sein kann, um die Verteilung von Daten zu analysieren.