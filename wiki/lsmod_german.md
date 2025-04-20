# [Linux] C Shell (csh) lsmod Verwendung: Zeigt geladene Kernelmodule an

## Übersicht
Der Befehl `lsmod` wird verwendet, um eine Liste der derzeit geladenen Kernelmodule in einem Linux-System anzuzeigen. Dies ist nützlich, um zu überprüfen, welche Module aktiv sind und um Informationen über deren Abhängigkeiten zu erhalten.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```csh
lsmod [Optionen] [Argumente]
```

## Häufige Optionen
- `-h`, `--help`: Zeigt eine Hilfeseite mit Informationen zur Verwendung des Befehls an.
- `-q`, `--quiet`: Reduziert die Ausgabe, um nur wichtige Informationen anzuzeigen.

## Häufige Beispiele
Um alle geladenen Kernelmodule anzuzeigen, verwenden Sie einfach:

```csh
lsmod
```

Um eine Hilfe zur Verwendung von lsmod anzuzeigen, verwenden Sie:

```csh
lsmod --help
```

Um die Ausgabe zu reduzieren und nur wichtige Informationen anzuzeigen, verwenden Sie:

```csh
lsmod -q
```

## Tipps
- Verwenden Sie `lsmod` in Kombination mit `grep`, um nach einem bestimmten Modul zu suchen, z.B. `lsmod | grep <modulname>`.
- Überprüfen Sie regelmäßig die geladenen Module, um sicherzustellen, dass keine unerwünschten oder veralteten Module aktiv sind.
- Nutzen Sie `modinfo <modulname>`, um detaillierte Informationen über ein spezifisches Modul zu erhalten, das Sie in der `lsmod`-Ausgabe gefunden haben.