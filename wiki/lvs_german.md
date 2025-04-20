# [Linux] C Shell (csh) lvs Verwendung: Zeigt logische Volumes an

## Übersicht
Der Befehl `lvs` wird verwendet, um Informationen über logische Volumes im Logical Volume Manager (LVM) anzuzeigen. Er bietet eine Übersicht über die vorhandenen logischen Volumes und deren Eigenschaften.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```
lvs [Optionen] [Argumente]
```

## Häufige Optionen
- `-o`: Gibt an, welche Spalten angezeigt werden sollen.
- `-a`: Zeigt auch inaktive logische Volumes an.
- `--units`: Legt die Einheit für die Ausgabe fest (z. B. MB, GB).
- `-n`: Zeigt nur die Namen der logischen Volumes an.

## Häufige Beispiele
Um alle logischen Volumes anzuzeigen, verwenden Sie:

```bash
lvs
```

Um spezifische Informationen über die logischen Volumes anzuzeigen, einschließlich ihrer Größe und Status:

```bash
lvs -o +devices
```

Um alle logischen Volumes, einschließlich der inaktiven, anzuzeigen:

```bash
lvs -a
```

Um die Ausgabe in Gigabyte anzuzeigen:

```bash
lvs --units g
```

Um nur die Namen der logischen Volumes anzuzeigen:

```bash
lvs -n
```

## Tipps
- Verwenden Sie die Option `-o`, um nur die für Sie relevanten Informationen anzuzeigen und die Ausgabe übersichtlicher zu gestalten.
- Kombinieren Sie `lvs` mit anderen LVM-Befehlen, um umfassendere Informationen über Ihre Volumes zu erhalten.
- Überprüfen Sie regelmäßig Ihre logischen Volumes, um sicherzustellen, dass genügend Speicherplatz verfügbar ist und um eine optimale Leistung zu gewährleisten.