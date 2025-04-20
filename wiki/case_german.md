# [Linux] C Shell (csh) case Verwendung: Mustervergleich von Variablen

## Übersicht
Der `case` Befehl in der C Shell (csh) wird verwendet, um Variablen mit verschiedenen Mustern zu vergleichen. Er ermöglicht es, unterschiedliche Aktionen basierend auf dem Wert einer Variablen auszuführen, ähnlich wie eine Switch-Anweisung in anderen Programmiersprachen.

## Verwendung
Die grundlegende Syntax des `case` Befehls sieht wie folgt aus:

```
case [variable] in
    [muster1]) [Befehle1];;
    [muster2]) [Befehle2];;
    ...
esac
```

## Häufige Optionen
- `in`: Leitet die Musterdefinition ein.
- `;;`: Beendet einen Musterblock.
- `esac`: Beendet die `case` Anweisung.

## Häufige Beispiele

### Beispiel 1: Einfache Musterübereinstimmung
```csh
set var = "rot"
case $var in
    "rot") echo "Die Farbe ist rot";;
    "blau") echo "Die Farbe ist blau";;
    *) echo "Unbekannte Farbe";;
esac
```

### Beispiel 2: Mehrere Muster
```csh
set tier = "Hund"
case $tier in
    "Hund" | "Katze") echo "Es ist ein Haustier";;
    "Vogel") echo "Es ist ein Vogel";;
    *) echo "Unbekanntes Tier";;
esac
```

### Beispiel 3: Verwendung von Platzhaltern
```csh
set datei = "bericht.txt"
case $datei in
    *.txt) echo "Es handelt sich um eine Textdatei";;
    *.jpg) echo "Es handelt sich um ein Bild";;
    *) echo "Unbekannte Dateityp";;
esac
```

## Tipps
- Verwenden Sie Platzhalter (`*` und `?`), um flexiblere Muster zu erstellen.
- Stellen Sie sicher, dass die Muster in der richtigen Reihenfolge angeordnet sind, da die erste Übereinstimmung verwendet wird.
- Nutzen Sie `*)` als Standardfall, um unerwartete Werte zu behandeln.