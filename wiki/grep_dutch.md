# [Linux] C Shell (csh) grep Gebruik: Zoek naar tekst in bestanden

## Overzicht
De `grep`-opdracht is een krachtige tool die wordt gebruikt om tekstpatronen in bestanden te zoeken. Het kan worden gebruikt om specifieke lijnen te vinden die overeenkomen met een opgegeven patroon, wat het een onmisbaar hulpmiddel maakt voor programmeurs en systeembeheerders.

## Gebruik
De basis syntaxis van de `grep`-opdracht is als volgt:

```csh
grep [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-i`: Negeert hoofdlettergebruik bij het zoeken.
- `-v`: Toont alleen de lijnen die **niet** overeenkomen met het patroon.
- `-r`: Doorzoekt bestanden in subdirectory's.
- `-n`: Toont het regelnummer van de overeenkomende lijnen.
- `-l`: Toont alleen de namen van de bestanden die het patroon bevatten.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `grep`:

1. Zoek naar een specifiek woord in een bestand:
   ```csh
   grep "woord" bestand.txt
   ```

2. Zoek naar een woord zonder hoofdlettergebruik:
   ```csh
   grep -i "woord" bestand.txt
   ```

3. Zoek naar een woord in alle tekstbestanden in de huidige directory:
   ```csh
   grep "woord" *.txt
   ```

4. Zoek naar een woord in alle bestanden binnen een directory en subdirectory's:
   ```csh
   grep -r "woord" /pad/naar/directory
   ```

5. Toon de regelnummer van de overeenkomende lijnen:
   ```csh
   grep -n "woord" bestand.txt
   ```

## Tips
- Gebruik de `-v` optie om snel te filteren op lijnen die niet overeenkomen met je zoekopdracht.
- Combineer `grep` met andere commando's zoals `ls` of `find` voor meer geavanceerde zoekopdrachten.
- Maak gebruik van reguliere expressies voor complexere zoekpatronen, wat de kracht van `grep` verder vergroot.