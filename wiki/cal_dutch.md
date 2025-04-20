# [Linux] C Shell (csh) cal gebruik: Weergave van kalenders

## Overzicht
De `cal` opdracht in C Shell (csh) wordt gebruikt om een kalender weer te geven. Het toont de kalender voor een specifieke maand of jaar, wat handig kan zijn voor het plannen van afspraken of het bekijken van datums.

## Gebruik
De basis syntaxis van de `cal` opdracht is als volgt:

```csh
cal [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-m`: Begin de week op maandag in plaats van zondag.
- `-3`: Toon de kalender van de huidige maand, de vorige maand en de volgende maand.
- `-y`: Toon de kalender voor het huidige jaar.
- `-j`: Toon de kalender met de dagen van het jaar (julian).

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `cal` opdracht:

1. **Toon de kalender voor de huidige maand:**
   ```csh
   cal
   ```

2. **Toon de kalender voor een specifieke maand en jaar (bijvoorbeeld maart 2023):**
   ```csh
   cal 03 2023
   ```

3. **Toon de kalender voor het huidige jaar:**
   ```csh
   cal -y
   ```

4. **Toon de kalender voor de huidige, vorige en volgende maand:**
   ```csh
   cal -3
   ```

5. **Toon de kalender voor een specifiek jaar met julian dagen:**
   ```csh
   cal -j 2023
   ```

## Tips
- Gebruik de `-m` optie als je de week op maandag wilt laten beginnen, wat gebruikelijker is in sommige landen.
- Combineer opties voor meer specifieke weergaven, bijvoorbeeld `cal -3 -m` om drie maanden te tonen met maandag als eerste dag.
- Controleer altijd de man-pagina (`man cal`) voor meer gedetailleerde informatie en opties.