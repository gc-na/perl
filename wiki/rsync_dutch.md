# [Linux] C Shell (csh) rsync gebruik: Bestanden synchroniseren en overdragen

## Overzicht
De `rsync`-opdracht is een krachtige tool voor het synchroniseren en overdragen van bestanden en mappen tussen verschillende locaties, zowel lokaal als op afstand. Het is efficiënt omdat het alleen de gewijzigde delen van bestanden overzet, wat tijd en bandbreedte bespaart.

## Gebruik
De basis syntaxis van de `rsync`-opdracht is als volgt:

```csh
rsync [opties] [bronnen] [doel]
```

## Veelvoorkomende Opties
- `-a`: Archiveer modus; behoudt bestandspermissies, tijdstempels en symlinks.
- `-v`: Verbose; toont gedetailleerde uitvoer van het proces.
- `-z`: Comprimeert de gegevens tijdens de overdracht.
- `-r`: Recursief; kopieert mappen en hun inhoud.
- `--delete`: Verwijdert bestanden in de doelmap die niet meer in de brondirectory staan.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `rsync`:

1. **Bestanden kopiëren van een lokale map naar een andere lokale map:**

   ```csh
   rsync -av /pad/naar/bronnen/ /pad/naar/doel/
   ```

2. **Bestanden synchroniseren van een lokale map naar een externe server:**

   ```csh
   rsync -av /pad/naar/bronnen/ gebruiker@server:/pad/naar/doel/
   ```

3. **Bestanden synchroniseren van een externe server naar een lokale map:**

   ```csh
   rsync -av gebruiker@server:/pad/naar/bronnen/ /pad/naar/doel/
   ```

4. **Bestanden synchroniseren met compressie:**

   ```csh
   rsync -avz /pad/naar/bronnen/ gebruiker@server:/pad/naar/doel/
   ```

5. **Bestanden synchroniseren en verwijderen van niet-bestaande bestanden in de doelmap:**

   ```csh
   rsync -av --delete /pad/naar/bronnen/ /pad/naar/doel/
   ```

## Tips
- Gebruik de `-n` of `--dry-run` optie om te zien welke bestanden er gekopieerd zullen worden zonder daadwerkelijk iets te veranderen.
- Zorg ervoor dat je altijd een back-up hebt van belangrijke gegevens voordat je de `--delete` optie gebruikt.
- Combineer `rsync` met cronjobs voor automatische back-ups op regelmatige tijdstippen.