<!--
Meta Description: # Import in Perl: Ein Überblick über das Importieren von Modulen und Funktionen ## Synopsis Das `import`-Kommando in Perl wird verwendet, um Funktione...
Meta Keywords: funktionen, die, perl, use, import
-->

# Import in Perl: Ein Überblick über das Importieren von Modulen und Funktionen

## Synopsis
Das `import`-Kommando in Perl wird verwendet, um Funktionen, Variablen oder Objekte aus einem Modul in den aktuellen Namespace zu importieren, sodass sie ohne Präfix verwendet werden können.

## Dokumentation
### Zweck
Das Importieren von Modulen ist eine zentrale Funktion in Perl, die es Programmierern ermöglicht, die Funktionalität ihrer Skripte durch die Nutzung vorhandener Module zu erweitern. Über das `import`-Kommando können spezifische Funktionen oder Variablen aus einem Modul in den aktuellen Geltungsbereich geladen werden.

### Verwendung
In Perl wird das `import`-Kommando häufig in Verbindung mit der `use`-Anweisung verwendet. Die Syntax lautet:

```perl
use Modulname qw(Funktion1 Funktion2);
```

Hierbei wird `Modulname` durch den Namen des gewünschten Moduls ersetzt, und `Funktion1`, `Funktion2` sind die spezifischen Funktionen, die importiert werden sollen. 

### Details
- **Standardverhalten**: Bei der Verwendung von `use Modulname;` werden alle exportierbaren Funktionen importiert, sofern das Modul dies unterstützt.
- **Export von Variablen**: Neben Funktionen können auch Variablen importiert werden.
- **Exportgruppen**: Viele Module definieren Gruppen von Funktionen, die über den Namen der Gruppe importiert werden können. Zum Beispiel:

```perl
use Modulname qw(:all);  # Importiert alle exportierbaren Funktionen
```

## Beispiele
### Einfaches Beispiel
```perl
use strict;
use warnings;
use List::Util qw(sum);

my @zahlen = (1, 2, 3, 4);
my $summe = sum(@zahlen);
print "Die Summe ist: $summe\n";  # Ausgabe: Die Summe ist: 10
```

### Importieren einer Variablen
```perl
package MeinModul;
use Exporter 'import';
our @EXPORT = qw($meine_variable);

$meine_variable = 42;

package main;
use MeinModul;

print $meine_variable;  # Ausgabe: 42
```

## Erklärung
### Häufige Stolpersteine
- **Namenskonflikte**: Wenn zwei Module die gleiche Funktion exportieren, kann es zu Konflikten kommen. Um dies zu vermeiden, ist es ratsam, spezifische Funktionen zu importieren oder Aliasnamen zu verwenden.
- **Nicht exportierte Funktionen**: Beachten Sie, dass nicht alle Funktionen eines Moduls automatisch exportiert werden. Überprüfen Sie die Dokumentation des Moduls, um sicherzustellen, dass die gewünschten Funktionen verfügbar sind.
- **Module ohne `import`-Funktion**: Einige Module bieten keine `import`-Funktion an. In solchen Fällen müssen Sie die Funktionen mit dem vollständigen Namensraum ansprechen.

## Ein-Satz-Zusammenfassung
Das `import`-Kommando in Perl ermöglicht das Importieren von Funktionen und Variablen aus Modulen in den aktuellen Namespace, um die Programmierung zu erleichtern und den Code zu modularisieren.