<!--
Meta Description: # "our" in Perl: Verwendung und Bedeutung ## Synopsis Das Schlüsselwort "our" in Perl wird verwendet, um eine variable Sichtbarkeit zu definieren. Es ...
Meta Keywords: our, die, variablen, perl, mit
-->

# "our" in Perl: Verwendung und Bedeutung

## Synopsis
Das Schlüsselwort "our" in Perl wird verwendet, um eine variable Sichtbarkeit zu definieren. Es ermöglicht die Deklaration von Variablen mit einem lexikalischen Scope, die im gesamten Paket oder in der aktuellen Datei sichtbar sind, jedoch nicht im globalen Namespace.

## Dokumentation
Das Schlüsselwort "our" wurde in Perl 5.6 eingeführt und dient der Deklaration von Paketvariablen oder globalen Variablen innerhalb eines Moduls oder Skripts. Es ist eine wichtige Funktion, die es Entwicklern ermöglicht, sicherzustellen, dass Variablen nicht versehentlich global verwendet werden, was zu unerwartetem Verhalten führen kann.

### Verwendung
Um eine Variable mit "our" zu deklarieren, verwenden Sie das folgende Format:

```perl
our $variable_name;
```

Sie können auch mehrere Variablen in einer einzigen Zeile deklarieren:

```perl
our ($var1, $var2, $var3);
```

Variablen, die mit "our" deklariert wurden, können innerhalb des gesamten Pakets oder der aktuellen Datei verwendet werden, aber nicht außerhalb. Dies hilft, Kollisionen mit anderen Variablen im globalen Namespace zu vermeiden.

## Beispiele
Hier sind einige grundlegende Beispiele zur Verwendung von "our":

### Beispiel 1: Einfache Deklaration
```perl
package MyPackage;

our $global_var = "Ich bin global!";

sub print_var {
    print $global_var;
}
```

### Beispiel 2: Mehrere Variablen
```perl
package MyPackage;

our ($var1, $var2) = ("Hallo", "Welt");

sub print_vars {
    print "$var1 $var2\n";
}
```

### Beispiel 3: Verwendung in einer anderen Datei
```perl
# In my_package.pm
package MyPackage;

our $shared_var = "Teilen";

# In main.pl
use MyPackage;
print $MyPackage::shared_var;  # Ausgabe: Teilen
```

## Erklärung
Ein häufiger Fehler beim Arbeiten mit "our" ist die Verwechslung mit "my". Während "my" eine variable Sichtbarkeit innerhalb eines Blocks oder einer Funktion definiert, ist "our" für die Sichtbarkeit innerhalb des Pakets oder der Datei zuständig. Es ist wichtig zu beachten, dass Variablen, die mit "our" deklariert werden, nicht die gleichen Eigenschaften wie globale Variablen haben, da sie nicht in anderen Paketen ohne den Paketnamen referenziert werden können.

Ein weiterer Punkt zu beachten ist, dass "our" in Verbindung mit "strict" verwendet werden sollte, um sicherzustellen, dass die Variablen korrekt deklariert werden und keine unbeabsichtigten Fehler auftreten.

## Einzeiler Zusammenfassung
Das Schlüsselwort "our" in Perl definiert Paketvariablen mit einem lexikalischen Scope, die innerhalb des aktuellen Pakets oder der Datei sichtbar sind.