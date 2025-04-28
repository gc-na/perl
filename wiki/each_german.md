<!--
Meta Description: # Perl "each" - Ein umfassender Leitfaden ## Synopsis Der `each` Befehl in Perl ermöglicht es Entwicklern, durch die Schlüssel-Wert-Paare eines Hashes...
Meta Keywords: each, die, der, schlüssel, hashes
-->

# Perl "each" - Ein umfassender Leitfaden

## Synopsis
Der `each` Befehl in Perl ermöglicht es Entwicklern, durch die Schlüssel-Wert-Paare eines Hashes zu iterieren. Es ist ein nützliches Werkzeug, um auf die Elemente eines Hashes zuzugreifen, ohne die Schlüssel oder Werte separat zu verwalten.

## Dokumentation
### Zweck
Der `each` Befehl wird verwendet, um den nächsten Schlüssel-Wert-Paar eines Hashes abzurufen. Bei jedem Aufruf von `each` wird das nächste Paar zurückgegeben, bis alle Paare durchlaufen sind.

### Verwendung
Der `each` Befehl wird typischerweise in einer `while`-Schleife verwendet, um alle Elemente eines Hashes zu durchlaufen. Die Syntax lautet:

```perl
while (my ($key, $value) = each %hash) {
    # Verarbeitung von $key und $value
}
```

Hierbei wird `%hash` durch die Hash-Variable ersetzt, die durchlaufen werden soll. 

### Details
- `each` gibt ein Array zurück, dessen erstes Element der Schlüssel und das zweite Element der Wert ist.
- Es ändert den internen Zähler des Hashes, sodass bei aufeinanderfolgenden Aufrufen von `each` die nächsten Paare zurückgegeben werden.
- Wenn alle Paare durchlaufen sind, gibt `each` einen leeren Listenausdruck zurück, was das Ende der Iteration anzeigt.

## Beispiele
### Einfaches Beispiel
```perl
my %fruits = (
    'Apfel'   => 'Rot',
    'Banane'  => 'Gelb',
    'Traube'  => 'Lila',
);

while (my ($key, $value) = each %fruits) {
    print "$key ist $value\n";
}
```

### Beispiel mit `each` und `if`
```perl
my %personen = (
    'Alice' => 30,
    'Bob'   => 25,
    'Eve'   => 35,
);

while (my ($name, $alter) = each %personen) {
    if ($alter > 30) {
        print "$name ist älter als 30 Jahre.\n";
    }
}
```

## Erklärung
- **Gemeinsame Fallstricke**: Verwenden Sie `each` nicht mit Arrays, da es nur für Hashes geeignet ist. Der Befehl wird auch nicht funktionieren, wenn die Hash-Variable nicht korrekt initialisiert ist.
- **Effizienz**: `each` kann in Situationen nützlich sein, in denen Sie sowohl Schlüssel als auch Werte benötigen, da es die Notwendigkeit beseitigt, zuerst die Schlüssel mit `keys` abzurufen.
- **Beenden der Iteration**: Achten Sie darauf, die Iteration zu beenden, wenn `each` einen leeren Listenausdruck zurückgibt, um unbeabsichtigte Endlosschleifen zu vermeiden.

## Ein-Satz-Zusammenfassung
Der `each` Befehl in Perl ermöglicht eine einfache und effiziente Iteration über die Schlüssel-Wert-Paare eines Hashes.