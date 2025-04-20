# [Linux] C Shell (csh) mv gebruik: Verplaatsen of hernoemen van bestanden

## Overzicht
De `mv`-opdracht in C Shell (csh) wordt gebruikt om bestanden of mappen te verplaatsen of te hernoemen. Het is een essentieel hulpmiddel voor het beheren van bestanden in een Unix-achtige omgeving.

## Gebruik
De basis syntaxis van de `mv`-opdracht is als volgt:

```csh
mv [opties] [argumenten]
```

## Veelvoorkomende opties
- `-i`: Vraagt om bevestiging voordat een bestaand bestand wordt overschreven.
- `-u`: Verplaatst alleen als de bron nieuwere bestanden bevat dan de bestemming.
- `-v`: Toont gedetailleerde uitvoer van wat er gebeurt tijdens het verplaatsen of hernoemen.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `mv`-opdracht:

1. **Een bestand hernoemen:**
   ```csh
   mv oud_bestand.txt nieuw_bestand.txt
   ```

2. **Een bestand verplaatsen naar een andere map:**
   ```csh
   mv bestand.txt /pad/naar/doelmap/
   ```

3. **Meerdere bestanden verplaatsen:**
   ```csh
   mv bestand1.txt bestand2.txt /pad/naar/doelmap/
   ```

4. **Een bestand verplaatsen met bevestiging bij overschrijven:**
   ```csh
   mv -i bestand.txt /pad/naar/doelmap/
   ```

## Tips
- Gebruik de `-i` optie om onbedoeld overschrijven van bestanden te voorkomen.
- Controleer altijd de bestandsnamen en paden voordat je de `mv`-opdracht uitvoert om fouten te vermijden.
- Maak gebruik van de `-v` optie om te zien wat er precies gebeurt, vooral bij het verplaatsen van meerdere bestanden.