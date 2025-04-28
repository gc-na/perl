<!--
Meta Description: # "state" in Perl: Ein Überblick über den Zustand von Variablen ## Synopsis Das `state` Schlüsselwort in Perl ermöglicht die Deklaration von variablen...
Meta Keywords: state, die, der, variablen, perl
-->

# "state" in Perl: Ein Überblick über den Zustand von Variablen

## Synopsis
Das `state` Schlüsselwort in Perl ermöglicht die Deklaration von variablen Zuständen, die ihren Wert über mehrere Aufrufe einer Funktion hinweg behalten. Diese Funktionalität ist nützlich für die Speicherung von Daten, die nicht bei jedem Funktionsaufruf zurückgesetzt werden sollen.

## Dokumentation
### Zweck
Das `state` Schlüsselwort wurde in Perl 5.10 eingeführt und bietet eine Möglichkeit, lokale Variablen zu deklarieren, die ihren Wert zwischen Funktionsaufrufen beibehalten. Im Gegensatz zu regulären lokalen Variablen, die bei jedem Aufruf der Funktion neu initialisiert werden, wird eine `state`-Variable nur einmal beim ersten Aufruf der Funktion initialisiert.

### Verwendung
Um eine `state`-Variable zu deklarieren, verwendet man die Syntax:
```perl
state $variable_name;
```
Diese Variable wird wie eine lokale Variable behandelt, bleibt jedoch im Gedächtnis, bis das Programm beendet wird.

### Details
- `state`-Variablen sind nur innerhalb der Funktion sichtbar, in der sie deklariert wurden.
- Sie sind nicht global und können nicht außerhalb der Funktion verwendet werden.
- Die Initialisierung erfolgt beim ersten Aufruf der Funktion und bleibt bestehen, bis das Programm endet.

## Beispiele
### Einfaches Beispiel
```perl
sub zaehler {
    state $count = 0;  # $count wird nur einmal initialisiert
    $count++;
    return $count;
}

print zaehler(); # Gibt 1 aus
print zaehler(); # Gibt 2 aus
print zaehler(); # Gibt 3 aus
```

### Beispiel mit Bedingung
```perl
sub bedingter_increment {
    state $zahl = 0;
    
    if ($zahl < 5) {
        $zahl++;
    }
    
    return $zahl;
}

print bedingter_increment(); # Gibt 1 aus
print bedingter_increment(); # Gibt 2 aus
```

## Erklärung
Ein häufiges Missverständnis besteht darin, dass `state`-Variablen wie globale Variablen behandelt werden. Dies ist jedoch nicht der Fall, da sie nur innerhalb ihrer Funktion sichtbar sind. Ein weiteres potenzielles Problem ist, dass man die initialisierte Variable nicht direkt zurücksetzen kann, es sei denn, man beendet das Programm. Das kann zu unerwarteten Ergebnissen führen, wenn man erwartet, dass der Zustand der Variable zurückgesetzt wird.

## Einzeiliger Überblick
Das `state` Schlüsselwort in Perl ermöglicht es, lokale Variablen zu deklarieren, die ihren Wert über mehrere Funktionsaufrufe hinweg beibehalten.