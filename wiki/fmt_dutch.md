# [Linux] C Shell (csh) fmt Gebruik: Tekst formatteren

## Overzicht
De `fmt`-opdracht is een hulpmiddel voor het formatteren van tekst in een leesbare indeling. Het is vooral nuttig voor het aanpassen van de breedte van tekstregels in een bestand of op de standaardinvoer, zodat ze beter passen in een bepaalde ruimte.

## Gebruik
De basis syntaxis van de `fmt`-opdracht is als volgt:

```csh
fmt [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-w <breedte>`: Stelt de maximale breedte van de regels in. Standaard is dit meestal 72 tekens.
- `-s`: Voorkomt dat lege regels worden samengevoegd.
- `-u`: Voert een ongebroken tekstuitvoer uit, waarbij de regels niet worden afgebroken.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `fmt`-opdracht:

1. **Formatteren van een tekstbestand naar standaard breedte:**
   ```csh
   fmt tekstbestand.txt
   ```

2. **Formatteren met een specifieke breedte van 50 tekens:**
   ```csh
   fmt -w 50 tekstbestand.txt
   ```

3. **Formatteren van invoer vanuit de standaardinvoer:**
   ```csh
   echo "Dit is een voorbeeld van een lange zin die we willen formatteren." | fmt
   ```

4. **Formatteren zonder lege regels samen te voegen:**
   ```csh
   fmt -s tekstbestand.txt
   ```

## Tips
- Gebruik de `-w` optie om de breedte aan te passen aan de lay-out van uw document of scherm.
- Controleer altijd de uitvoer om er zeker van te zijn dat de tekst correct is geformatteerd, vooral bij gebruik van de `-s` optie.
- Combineer `fmt` met andere commando's zoals `cat` of `echo` voor meer geavanceerde tekstverwerking.