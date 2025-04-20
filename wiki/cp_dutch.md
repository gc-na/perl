# [Linux] C Shell (csh) cp gebruik: Bestanden kopiëren

## Overzicht
De `cp`-opdracht in C Shell (csh) wordt gebruikt om bestanden en mappen te kopiëren van de ene locatie naar de andere. Het is een essentieel hulpmiddel voor bestandsbeheer in een Unix-achtige omgeving.

## Gebruik
De basis syntaxis van de `cp`-opdracht is als volgt:

```csh
cp [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-i`: Vraagt om bevestiging voordat een bestaand bestand wordt overschreven.
- `-r`: Kopieert directories en hun inhoud recursief.
- `-u`: Kopieert alleen bestanden die nieuwer zijn dan de doelbestanden of als de doelbestanden niet bestaan.
- `-v`: Geeft gedetailleerde informatie over de kopieeroperaties weer.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `cp`-opdracht:

1. **Een bestand kopiëren naar een andere locatie:**
   ```csh
   cp bestand.txt /pad/naar/doel/
   ```

2. **Een bestand kopiëren en hernoemen:**
   ```csh
   cp bestand.txt nieuw_bestand.txt
   ```

3. **Een directory en zijn inhoud kopiëren:**
   ```csh
   cp -r /pad/naar/directory /pad/naar/doel/
   ```

4. **Een bestand kopiëren met bevestiging bij overschrijven:**
   ```csh
   cp -i bestand.txt /pad/naar/doel/
   ```

5. **Alleen nieuwere bestanden kopiëren:**
   ```csh
   cp -u bestand.txt /pad/naar/doel/
   ```

## Tips
- Gebruik de `-v` optie om te zien welke bestanden worden gekopieerd, dit kan handig zijn voor het controleren van de voortgang.
- Wees voorzichtig met de `-r` optie, vooral bij het kopiëren van grote directories, om onbedoeld gegevensverlies te voorkomen.
- Maak altijd een back-up van belangrijke bestanden voordat je ze overschrijft met de `cp`-opdracht.