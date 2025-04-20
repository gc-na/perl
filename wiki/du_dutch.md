# [Linux] C Shell (csh) du gebruik: Toon schijfruimtegebruik

## Overzicht
De `du` (disk usage) opdracht in C Shell wordt gebruikt om de schijfruimte te rapporteren die door bestanden en directories wordt gebruikt. Het helpt gebruikers om inzicht te krijgen in hoeveel ruimte verschillende bestanden en mappen innemen op hun systeem.

## Gebruik
De basis syntaxis van de `du` opdracht is als volgt:

```csh
du [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-h`: Toont de schijfruimte in een leesbaar formaat (bijv. KB, MB).
- `-s`: Geeft alleen de totale grootte van de opgegeven directory weer.
- `-a`: Toont de grootte van alle bestanden en directories, niet alleen de directories.
- `-c`: Geeft een totaal weer van de schijfruimte aan het einde van de uitvoer.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `du` opdracht:

1. Toon de schijfruimte van de huidige directory in een leesbaar formaat:
   ```csh
   du -h
   ```

2. Toon alleen de totale grootte van een specifieke directory:
   ```csh
   du -sh /pad/naar/directory
   ```

3. Toon de grootte van alle bestanden en directories in de huidige directory:
   ```csh
   du -ah
   ```

4. Toon de schijfruimte van een directory en geef een totaal weer:
   ```csh
   du -ch /pad/naar/directory
   ```

## Tips
- Gebruik de `-h` optie om de uitvoer gemakkelijker te lezen, vooral bij grote bestanden.
- Combineer de `-s` en `-c` opties om snel een overzicht van de totale schijfruimte te krijgen voor meerdere directories.
- Houd rekening met de schijfruimte van verborgen bestanden door de `-a` optie te gebruiken.