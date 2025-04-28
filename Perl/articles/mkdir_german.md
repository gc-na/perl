<!--
Meta Description: # mkdir in Perl: Verzeichnis erstellen mit Perl ## Synopsis Der `mkdir` Befehl in Perl wird verwendet, um neue Verzeichnisse zu erstellen. Dieser Befe...
Meta Keywords: verzeichnis, mkdir, das, perl, erstellen
-->

# mkdir in Perl: Verzeichnis erstellen mit Perl

## Synopsis
Der `mkdir` Befehl in Perl wird verwendet, um neue Verzeichnisse zu erstellen. Dieser Befehl ist ein grundlegendes Werkzeug in der Dateisystemmanipulation und ermöglicht es Entwicklern, Verzeichnisse programmgesteuert zu erzeugen.

## Documentation
Der Befehl `mkdir` in Perl ist eine Funktion, die es ermöglicht, ein neues Verzeichnis im Dateisystem zu erstellen. Die Syntax ist wie folgt:

```perl
mkdir(DIRNAME, MODE);
```

### Parameter:
- **DIRNAME**: Der Name des Verzeichnisses, das erstellt werden soll. Dies kann ein relativer oder absoluter Pfad sein.
- **MODE**: (Optional) Ein Moduswert, der die Berechtigungen des neuen Verzeichnisses festlegt. Dieser Wert wird im Oktalformat angegeben. Wenn dieser Parameter nicht angegeben wird, wird das Verzeichnis mit den Standardberechtigungen erstellt.

### Rückgabewert:
Die `mkdir` Funktion gibt einen Wahrheitswert zurück. Bei Erfolg wird `1` zurückgegeben, andernfalls wird `undef` zurückgegeben und `$!` enthält den Fehlergrund.

## Examples
Hier sind einige grundlegende Beispiele zur Verwendung von `mkdir` in Perl:

### Einfaches Verzeichnis erstellen
```perl
use strict;
use warnings;

my $verzeichnis = 'neues_verzeichnis';
mkdir($verzeichnis) or die "Konnte das Verzeichnis nicht erstellen: $!";
print "Verzeichnis '$verzeichnis' erfolgreich erstellt.\n";
```

### Verzeichnis mit Berechtigungen erstellen
```perl
use strict;
use warnings;

my $verzeichnis = 'geschuetztes_verzeichnis';
my $modus = 0755; # rwxr-xr-x
mkdir($verzeichnis, $modus) or die "Konnte das Verzeichnis nicht erstellen: $!";
print "Verzeichnis '$verzeichnis' mit Modus '$modus' erfolgreich erstellt.\n";
```

## Explanation
Bei der Verwendung von `mkdir` gibt es einige häufige Fallstricke und Punkte, die beachtet werden sollten:

- **Berechtigungen**: Wenn das Skript nicht die erforderlichen Berechtigungen hat, um ein Verzeichnis zu erstellen, schlägt der Befehl fehl. Stellen Sie sicher, dass das Skript mit ausreichenden Rechten ausgeführt wird.
- **Existierendes Verzeichnis**: Wenn das angegebene Verzeichnis bereits existiert, gibt `mkdir` einen Fehler zurück. Um dies zu vermeiden, kann eine Überprüfung durchgeführt werden, bevor der Befehl ausgeführt wird.
- **Pfadtrennzeichen**: Achten Sie darauf, die richtigen Pfadtrennzeichen für das verwendete Betriebssystem zu verwenden (z.B. `/` für Unix/Linux und `\` für Windows).
- **Oktalmodus**: Wenn Sie den Modus angeben, verwenden Sie das Oktalformat. Dies wird oft übersehen und kann zu unerwarteten Berechtigungen führen.

## One Line Summary
Der `mkdir` Befehl in Perl ermöglicht das programmgesteuerte Erstellen von Verzeichnissen im Dateisystem.