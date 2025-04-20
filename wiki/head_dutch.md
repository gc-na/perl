# [Linux] C Shell (csh) head gebruik: Toont de eerste regels van een bestand

## Overzicht
De `head` opdracht in C Shell (csh) wordt gebruikt om de eerste regels van een bestand weer te geven. Dit is handig wanneer je snel een overzicht wilt krijgen van de inhoud van een bestand zonder het volledig te openen.

## Gebruik
De basis syntaxis van de `head` opdracht is als volgt:

```csh
head [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-n [aantal]`: Geeft het opgegeven aantal regels weer. Standaard toont `head` de eerste 10 regels.
- `-q`: Vermijdt het weergeven van bestandsnamen bij meerdere bestanden.
- `-v`: Toont altijd de bestandsnaam, zelfs als er maar één bestand is.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `head` opdracht:

1. Toon de eerste 10 regels van een bestand:
   ```csh
   head bestand.txt
   ```

2. Toon de eerste 5 regels van een bestand:
   ```csh
   head -n 5 bestand.txt
   ```

3. Toon de eerste 15 regels van meerdere bestanden:
   ```csh
   head -n 15 bestand1.txt bestand2.txt
   ```

4. Toon de eerste 10 regels van een bestand zonder bestandsnaam:
   ```csh
   head -q bestand1.txt bestand2.txt
   ```

## Tips
- Gebruik `head` in combinatie met andere opdrachten, zoals `grep`, om snel de eerste regels van gefilterde resultaten te bekijken.
- Als je vaak met grote bestanden werkt, kan `head` je helpen om snel een idee te krijgen van de structuur en inhoud zonder het hele bestand te hoeven openen.
- Vergeet niet dat je de `-n` optie kunt gebruiken om een specifiek aantal regels aan te geven, wat handig is voor verschillende situaties.