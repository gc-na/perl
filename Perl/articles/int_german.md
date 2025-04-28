<!--
Meta Description: # Der Perl-Befehl "int": Ganzzahlige Konvertierung und Rundung ## Synopsis Der `int` Befehl in Perl wird verwendet, um eine Zahl in eine ganze Zahl zu...
Meta Keywords: int, der, zahl, perl, eine
-->

# Der Perl-Befehl "int": Ganzzahlige Konvertierung und Rundung

## Synopsis
Der `int` Befehl in Perl wird verwendet, um eine Zahl in eine ganze Zahl zu konvertieren, indem die Nachkommastellen abgeschnitten werden. Dies ist nützlich, wenn Sie sicherstellen möchten, dass eine Zahl als Ganzzahl behandelt wird, ohne eine mathematische Rundung vorzunehmen.

## Dokumentation
Der `int` Befehl ist eine eingebaute Funktion in Perl, die eine numerische Eingabe erwartet und den größten ganzzahligen Wert zurückgibt, der kleiner oder gleich der Eingabe ist. Dabei werden alle Nachkommastellen verworfen.

### Verwendung
Die grundlegende Syntax sieht wie folgt aus:

```perl
my $ganzzahl = int($zahl);
```

Hierbei wird `$zahl` als Eingabewert verwendet, und `$ganzzahl` enthält das Ergebnis der Konvertierung.

### Details
- **Rückgabewert**: Der Rückgabewert von `int` ist immer ein ganzzahliger Wert.
- **Eingabewert**: Die Eingabe kann sowohl positive als auch negative Zahlen sowie Fließkommazahlen sein. Bei negativen Werten wird `int` zum nächsten kleineren ganzzahligen Wert runden.
- **Typenkonversion**: Perl konvertiert automatisch zwischen verschiedenen Datentypen, sodass `int` auch mit Strings funktionieren kann, die numerische Werte darstellen.

## Beispiele
### Beispiel 1: Grundlegende Verwendung
```perl
my $zahl = 3.7;
my $ganzzahl = int($zahl);
print $ganzzahl;  # Ausgabe: 3
```

### Beispiel 2: Negative Zahl
```perl
my $negative_zahl = -2.3;
my $ganzzahl_neg = int($negative_zahl);
print $ganzzahl_neg;  # Ausgabe: -2
```

### Beispiel 3: String-Eingabe
```perl
my $string_zahl = "5.9";
my $ganzzahl_string = int($string_zahl);
print $ganzzahl_string;  # Ausgabe: 5
```

## Erklärung
Ein häufiger Fehler besteht darin, zu glauben, dass `int` eine mathematische Rundung durchführt. Tatsächlich wird nur der ganzzahlige Teil der Zahl zurückgegeben, was bedeutet, dass `int(3.9)` zu `3` wird, nicht zu `4`. Ebenso kann bei negativen Zahlen `int` zu unerwarteten Ergebnissen führen, da es den Wert in Richtung Minus unendlich abrundet.

Ein weiteres wichtiges Detail ist, dass `int` nicht mit nicht-numerischen Werten umgehen kann. Wenn ein nicht-numerischer String übergeben wird, wird Perl diesen in der Regel als `0` interpretieren.

## Einzeilensummary
Der `int` Befehl in Perl wandelt eine Zahl in eine ganze Zahl um, indem er Nachkommastellen abschneidet, ohne zu runden.