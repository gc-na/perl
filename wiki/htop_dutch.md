# [Linux] C Shell (csh) htop gebruik: Procesbeheer en systeemmonitoring

## Overzicht
De `htop`-opdracht is een interactieve procesviewer voor Unix-systemen. Het biedt een real-time overzicht van de actieve processen op het systeem, inclusief informatie zoals CPU- en geheugengebruik, waardoor gebruikers eenvoudig processen kunnen beheren en monitoren.

## Gebruik
De basis syntaxis van de `htop`-opdracht is als volgt:

```csh
htop [opties] [argumenten]
```

## Veelvoorkomende opties
- `-h` : Toont de helpinformatie.
- `-u gebruikersnaam` : Toont alleen de processen die door de opgegeven gebruiker worden uitgevoerd.
- `-p PID` : Toont alleen het proces met het opgegeven proces-ID (PID).
- `--sort-key KEY` : Sorteert de processen op de opgegeven sleutel (bijv. `PID`, `USER`, `CPU`, `MEM`).

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `htop`:

1. Gewoon `htop` uitvoeren om de proceslijst te bekijken:
   ```csh
   htop
   ```

2. Alleen de processen van een specifieke gebruiker bekijken:
   ```csh
   htop -u gebruikersnaam
   ```

3. Een specifiek proces opzoeken met zijn PID:
   ```csh
   htop -p 1234
   ```

4. De processen sorteren op geheugengebruik:
   ```csh
   htop --sort-key MEM
   ```

## Tips
- Gebruik de pijltjestoetsen om door de lijst van processen te navigeren.
- Druk op `F9` om een proces te beëindigen en kies de gewenste signaaloptie.
- Gebruik `F2` om de instellingen te openen en de weergave aan te passen aan uw voorkeuren.
- Vergeet niet dat `htop` een interactieve tool is, dus experimenteer met de verschillende toetsen voor een betere ervaring.