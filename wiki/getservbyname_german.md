<!--
Meta Description: # getservbyname in Perl: Eine umfassende Anleitung ## Synopsis Die Funktion `getservbyname` in Perl ermöglicht es, Dienstinformationen anhand des Dien...
Meta Keywords: die, ist, getservbyname, name, port
-->

# getservbyname in Perl: Eine umfassende Anleitung

## Synopsis
Die Funktion `getservbyname` in Perl ermöglicht es, Dienstinformationen anhand des Dienstnamens und des Protokolls abzurufen, was für Netzwerkprogrammierung und -konfiguration nützlich ist.

## Dokumentation
Die Funktion `getservbyname` ist Teil des Perl-Modules `Socket` und wird verwendet, um Informationen über Netzwerkdienste zu erhalten. Diese Funktion nimmt zwei Argumente entgegen: den Namen des Dienstes (z. B. "http") und das Protokoll (z. B. "tcp"). Sie gibt eine Liste von Informationen zurück, darunter die Portnummer und die zugehörige Service-Nummer.

### Verwendung
```perl
use Socket;

my $service_name = 'http';
my $protocol = 'tcp';
my ($name, $port, $proto) = getservbyname($service_name, $protocol);
```

### Parameter
- `$service_name`: Ein String, der den Namen des gewünschten Dienstes angibt.
- `$protocol`: Ein String, der das Protokoll angibt, das gewöhnlich "tcp" oder "udp" ist.

### Rückgabewerte
Die Funktion gibt im Erfolgsfall eine Array-Liste zurück, die den Namen des Dienstes, die zugehörige Portnummer (als Ganzzahl) und das Protokoll enthält. Im Fehlerfall wird `undef` zurückgegeben.

## Beispiele
### Beispiel 1: Abrufen von HTTP-Dienstinformationen
```perl
use Socket;

my ($name, $port, $proto) = getservbyname('http', 'tcp');
print "Name: $name, Port: $port, Protokoll: $proto\n";
```
**Ausgabe:**
```
Name: http, Port: 80, Protokoll: tcp
```

### Beispiel 2: Abrufen von FTP-Dienstinformationen
```perl
use Socket;

my ($name, $port, $proto) = getservbyname('ftp', 'tcp');
print "Name: $name, Port: $port, Protokoll: $proto\n";
```
**Ausgabe:**
```
Name: ftp, Port: 21, Protokoll: tcp
```

## Erklärung
Ein häufiges Problem beim Einsatz von `getservbyname` ist die Verwechslung von Dienstnamen und Protokollen. Es ist wichtig, den korrekten Dienstnamen zu verwenden, da falsche Eingaben `undef` zurückgeben. Zudem ist `getservbyname` von den auf dem System konfigurierten Netzwerkdiensten abhängig. Wenn ein Dienst nicht in den Konfigurationsdateien vorhanden ist, wird er nicht gefunden.

Ein weiterer Punkt zu beachten ist, dass diese Funktion auf Plattformen, die keine vollständige Implementierung der BSD-Socket-API unterstützen, möglicherweise nicht verfügbar ist.

## Ein Satz Zusammenfassung
Die `getservbyname`-Funktion in Perl ist ein nützliches Werkzeug zum Abrufen von Netzwerkdienstinformationen anhand des Dienstnamens und des Protokolls.