# [Linux] C Shell (csh) cmp gebruik: Vergelijk bestanden byte voor byte

## Overview
De `cmp`-opdracht in C Shell (csh) wordt gebruikt om twee bestanden byte voor byte te vergelijken. Het geeft de eerste locatie weer waar de bestanden verschillen, wat nuttig is voor het identificeren van verschillen tussen tekst- of binaire bestanden.

## Usage
De basis syntaxis van de `cmp`-opdracht is als volgt:

```csh
cmp [opties] [bestanden]
```

## Common Options
Hier zijn enkele veelvoorkomende opties voor de `cmp`-opdracht:

- `-l`: Toon de verschillen in octale waarden.
- `-s`: Stil; geen uitvoer, maar geeft een exitstatus terug.
- `-i OFFSET`: Begin de vergelijking bij een specifieke byte-offset.
- `-n N`: Vergelijk slechts de eerste N bytes van de bestanden.

## Common Examples
Hier zijn enkele praktische voorbeelden van het gebruik van de `cmp`-opdracht:

1. Vergelijk twee bestanden en toon de eerste verschillen:
   ```csh
   cmp bestand1.txt bestand2.txt
   ```

2. Vergelijk twee binaire bestanden stil en controleer de exitstatus:
   ```csh
   cmp -s bestand1.bin bestand2.bin
   ```

3. Vergelijk alleen de eerste 10 bytes van twee bestanden:
   ```csh
   cmp -n 10 bestand1.txt bestand2.txt
   ```

4. Toon de verschillen in octale waarden:
   ```csh
   cmp -l bestand1.txt bestand2.txt
   ```

## Tips
- Gebruik de `-s` optie als je alleen geïnteresseerd bent in de exitstatus om te bepalen of de bestanden gelijk zijn zonder uitvoer te genereren.
- Combineer de `-n` optie met `-l` om specifieke secties van bestanden gedetailleerd te vergelijken.
- Vergeet niet dat `cmp` alleen de eerste verschillen toont; als je een volledig overzicht wilt van alle verschillen, overweeg dan om `diff` te gebruiken.