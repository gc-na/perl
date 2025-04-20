# [Nederlands] C Shell (csh) jobs gebruik: Toont actieve en achtergronddjobs

## Overzicht
De `jobs` opdracht in C Shell (csh) toont een lijst van alle actieve en achtergronddjobs die zijn gestart vanuit de huidige shell. Dit is handig om te zien welke processen er op de achtergrond draaien en om hun status te controleren.

## Gebruik
De basis syntaxis van de `jobs` opdracht is als volgt:

```csh
jobs [options] [arguments]
```

## Veelvoorkomende Opties
- `-l`: Toont de proces-ID's (PID) van de jobs.
- `-n`: Toont alleen de jobs die recentelijk zijn gewijzigd.
- `-p`: Toont alleen de proces-ID's van de jobs.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `jobs` opdracht:

1. **Basis gebruik**: Toont alle actieve jobs.
   ```csh
   jobs
   ```

2. **Toon jobs met PID**: Toont jobs met hun proces-ID's.
   ```csh
   jobs -l
   ```

3. **Toon recente jobs**: Toont alleen jobs die recentelijk zijn gewijzigd.
   ```csh
   jobs -n
   ```

4. **Toon alleen PID's**: Toont alleen de proces-ID's van de actieve jobs.
   ```csh
   jobs -p
   ```

## Tips
- Gebruik `jobs` regelmatig om een overzicht te houden van je actieve processen, vooral als je meerdere taken op de achtergrond uitvoert.
- Combineer `jobs` met de `fg` of `bg` opdrachten om jobs eenvoudig naar de voorgrond of achtergrond te verplaatsen.
- Vergeet niet dat jobs die zijn beëindigd, niet meer worden weergegeven in de lijst, dus controleer regelmatig om ervoor te zorgen dat je geen actieve processen mist.