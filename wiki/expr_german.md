# [Linux] C Shell (csh) expr Verwendung: Berechnungen und String-Manipulation

## Übersicht
Der Befehl `expr` wird in der C Shell (csh) verwendet, um einfache Berechnungen durchzuführen und Zeichenfolgen zu manipulieren. Er kann für arithmetische Operationen, logische Vergleiche und das Extrahieren von Substrings eingesetzt werden.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```csh
expr [Optionen] [Argumente]
```

## Häufige Optionen
- `+` : Addition von zwei Zahlen.
- `-` : Subtraktion von zwei Zahlen.
- `*` : Multiplikation von zwei Zahlen (muss mit Escape-Zeichen `\*` verwendet werden).
- `/` : Division von zwei Zahlen.
- `%` : Modulo-Operation, um den Rest einer Division zu erhalten.
- `=` : Vergleich von zwei Werten auf Gleichheit.
- `!=` : Vergleich von zwei Werten auf Ungleichheit.

## Häufige Beispiele

### 1. Einfache Addition
```csh
expr 5 + 3
```
Gibt `8` zurück.

### 2. Subtraktion
```csh
expr 10 - 4
```
Gibt `6` zurück.

### 3. Multiplikation
```csh
expr 7 \* 6
```
Gibt `42` zurück.

### 4. Division
```csh
expr 20 / 4
```
Gibt `5` zurück.

### 5. Modulo
```csh
expr 10 % 3
```
Gibt `1` zurück.

### 6. String-Länge
```csh
expr length "Hallo Welt"
```
Gibt `11` zurück.

### 7. Substring Extraktion
```csh
expr substr "Hallo Welt" 1 5
```
Gibt `Hallo` zurück.

## Tipps
- Achten Sie darauf, Multiplikation mit einem Escape-Zeichen (`\*`) zu verwenden, um Missverständnisse mit Shell-Metazeichen zu vermeiden.
- Verwenden Sie Klammern für komplexe Berechnungen, um die Reihenfolge der Operationen klarzustellen.
- `expr` gibt nur Ganzzahlen zurück; für Gleitkommazahlen sollten Sie andere Tools wie `bc` verwenden.