# [Nederlands] C Shell (csh) lvs gebruik: Toon logische volumenaam en status

## Overzicht
De `lvs` opdracht in C Shell (csh) wordt gebruikt om informatie over logische volumes in een volume group te tonen. Het geeft een overzicht van de logische volumes, inclusief hun naam, status en andere relevante details.

## Gebruik
De basis syntaxis van de `lvs` opdracht is als volgt:

```csh
lvs [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-o` : Specificeer welke velden moeten worden weergegeven.
- `-a` : Toon ook inactieve logische volumes.
- `-n` : Geef alleen de namen van de logische volumes weer.
- `--units` : Specificeer de eenheden voor de uitvoer.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `lvs` opdracht:

1. Toon een lijst van alle logische volumes:
    ```csh
    lvs
    ```

2. Toon specifieke velden zoals naam en grootte:
    ```csh
    lvs -o lv_name,size
    ```

3. Toon ook inactieve logische volumes:
    ```csh
    lvs -a
    ```

4. Geef alleen de namen van de logische volumes weer:
    ```csh
    lvs -n
    ```

5. Toon logische volumes met een specifieke eenheid (bijvoorbeeld gigabytes):
    ```csh
    lvs --units g
    ```

## Tips
- Gebruik de `-o` optie om de uitvoer aan te passen aan uw behoeften en alleen de relevante informatie weer te geven.
- Combineer opties voor meer gedetailleerde informatie, bijvoorbeeld `lvs -a -o +devices` om inactieve volumes en hun apparaten te tonen.
- Controleer regelmatig de status van uw logische volumes om problemen vroegtijdig te identificeren.