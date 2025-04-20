# [Linux] C Shell (csh) diff gebruik: Vergelijk bestanden

## Overzicht
De `diff`-opdracht in C Shell (csh) wordt gebruikt om de verschillen tussen twee bestanden of mappen te vergelijken. Het toont de regels die verschillen tussen de bestanden, wat nuttig is voor het identificeren van wijzigingen of het bijhouden van versies.

## Gebruik
De basis syntaxis van de `diff`-opdracht is als volgt:

```csh
diff [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-u`: Toont de verschillen in een uniforme indeling.
- `-c`: Toont de verschillen in een context-indeling.
- `-i`: Negeert hoofdlettergebruik bij de vergelijking.
- `-w`: Negeert witruimtes bij de vergelijking.
- `-r`: Vergelijkt subdirectories recursief.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `diff`-opdracht:

1. Vergelijk twee tekstbestanden en toon de verschillen:
   ```csh
   diff bestand1.txt bestand2.txt
   ```

2. Gebruik de uniforme indeling om de verschillen weer te geven:
   ```csh
   diff -u bestand1.txt bestand2.txt
   ```

3. Negeer hoofdlettergebruik bij de vergelijking:
   ```csh
   diff -i bestand1.txt bestand2.txt
   ```

4. Vergelijk twee mappen en hun inhoud recursief:
   ```csh
   diff -r map1/ map2/
   ```

5. Toon de verschillen in een context-indeling:
   ```csh
   diff -c bestand1.txt bestand2.txt
   ```

## Tips
- Gebruik de `-u` optie voor een overzichtelijke weergave van de verschillen, vooral bij het bekijken van grote bestanden.
- Combineer opties om de vergelijking aan te passen aan jouw behoeften, zoals het negeren van witruimtes of hoofdletters.
- Bewaar de uitvoer van `diff` in een bestand voor latere referentie door het gebruik van omleiding:
  ```csh
  diff bestand1.txt bestand2.txt > verschillen.txt
  ```