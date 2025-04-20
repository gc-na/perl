# [Linux] C Shell (csh) top gebruik: Toont actieve processen

## Overzicht
De `top`-opdracht is een krachtige tool die een dynamisch overzicht geeft van de actieve processen op een systeem. Het toont informatie zoals CPU- en geheugengebruik, waardoor gebruikers snel kunnen zien welke processen veel middelen verbruiken.

## Gebruik
De basis syntaxis van de `top`-opdracht is als volgt:

```csh
top [opties] [argumenten]
```

## Veelvoorkomende Opties
Hier zijn enkele veelvoorkomende opties die je kunt gebruiken met de `top`-opdracht:

- `-d <tijd>`: Stel de vertraging in tussen updates (in seconden).
- `-p <PID>`: Toon alleen de processen met de opgegeven proces-ID.
- `-u <gebruiker>`: Toon alleen de processen die door de opgegeven gebruiker worden uitgevoerd.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `top`-opdracht:

1. Gewoon `top` uitvoeren om de actieve processen te bekijken:
   ```csh
   top
   ```

2. De update-interval instellen op 5 seconden:
   ```csh
   top -d 5
   ```

3. Alleen de processen van een specifieke gebruiker tonen:
   ```csh
   top -u username
   ```

4. Specifieke processen volgen met hun PID:
   ```csh
   top -p 1234
   ```

## Tips
- Gebruik de toetsen `h` of `?` binnen de `top`-interface voor hulp en meer informatie over de beschikbare functies.
- Druk op `q` om de `top`-weergave te verlaten.
- Experimenteer met de sorteeropties door op de kolomkoppen te klikken (in een interactieve sessie) om processen te sorteren op basis van verschillende criteria, zoals CPU- of geheugengebruik.