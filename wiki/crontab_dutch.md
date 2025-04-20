# [Linux] C Shell (csh) crontab gebruik: Automatisch taken plannen

## Overzicht
De `crontab`-opdracht wordt gebruikt om taken (of "cron jobs") te plannen die op specifieke tijdstippen of intervallen moeten worden uitgevoerd. Dit is handig voor het automatiseren van routinetaken op een Unix-achtige besturingssysteem.

## Gebruik
De basis syntaxis van de `crontab`-opdracht is als volgt:

```csh
crontab [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-e`: Bewerk de huidige crontab.
- `-l`: Lijst de huidige crontab-taken.
- `-r`: Verwijder de huidige crontab.
- `-i`: Vraag bevestiging voordat de crontab wordt verwijderd.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `crontab`:

1. **Bewerk de crontab**:
   Om de crontab te bewerken, gebruik je de volgende opdracht:
   ```csh
   crontab -e
   ```

2. **Lijst de huidige crontab-taken**:
   Om de taken die momenteel zijn ingesteld te bekijken, gebruik je:
   ```csh
   crontab -l
   ```

3. **Verwijder de crontab**:
   Om je crontab te verwijderen, gebruik je:
   ```csh
   crontab -r
   ```

4. **Voeg een taak toe die elke dag om 2 uur 's nachts een script uitvoert**:
   In de crontab-editor, voeg de volgende regel toe:
   ```csh
   0 2 * * * /pad/naar/script.sh
   ```

5. **Voer een taak elke maandag om 5 uur 's ochtends uit**:
   Voeg deze regel toe aan de crontab:
   ```csh
   0 5 * * 1 /pad/naar/ander_script.sh
   ```

## Tips
- Zorg ervoor dat je het volledige pad naar scripts of commando's opgeeft in je crontab.
- Controleer regelmatig je crontab-taken om ervoor te zorgen dat ze correct zijn ingesteld.
- Gebruik logbestanden om de uitvoer van je cron-taken te controleren, dit kan helpen bij het oplossen van problemen.