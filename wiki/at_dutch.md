# [Linux] C Shell (csh) at: Tijdstippen voor het uitvoeren van opdrachten plannen

## Overview
Het `at` commando in C Shell (csh) wordt gebruikt om opdrachten op een specifieke tijd in de toekomst uit te voeren. Dit is handig voor het automatiseren van taken die op een later tijdstip moeten worden uitgevoerd.

## Usage
De basis syntaxis van het `at` commando is als volgt:

```csh
at [opties] [tijd]
```

## Common Options
Hier zijn enkele veelvoorkomende opties voor het `at` commando:

- `-f bestand`: Voer de opdrachten uit die in het opgegeven bestand staan.
- `-m`: Stuur een e-mail naar de gebruiker wanneer de taak is voltooid.
- `-q wachtrij`: Specificeer de wachtrij voor de taak (bijvoorbeeld 'a', 'b', 'c').
- `-V`: Toon de versie van het `at` commando.

## Common Examples
Hier zijn enkele praktische voorbeelden van het gebruik van het `at` commando:

1. **Een opdracht plannen voor 5 minuten later:**
   ```csh
   echo "echo 'Hallo, wereld!'" | at now + 5 minutes
   ```

2. **Een script uitvoeren om 14:00 uur:**
   ```csh
   at 14:00 < script.sh
   ```

3. **Een opdracht plannen voor morgen om 10:30 uur:**
   ```csh
   echo "backup.sh" | at 10:30 tomorrow
   ```

4. **Een opdracht vanuit een bestand uitvoeren:**
   ```csh
   at -f mijn_opdrachten.txt 15:00
   ```

## Tips
- Zorg ervoor dat je de juiste tijdsnotatie gebruikt, zoals 'now', 'tomorrow', of specifieke tijdstippen.
- Gebruik de `-m` optie als je een bevestiging wilt ontvangen via e-mail na het uitvoeren van de taak.
- Controleer je geplande taken met het `atq` commando om te zien welke opdrachten nog moeten worden uitgevoerd.