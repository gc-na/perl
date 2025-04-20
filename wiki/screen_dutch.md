# [Linux] C Shell (csh) schermgebruik: Beheer meerdere terminalsessies

## Overzicht
De `screen`-opdracht is een krachtige tool die gebruikers in staat stelt om meerdere terminalsessies te beheren binnen één enkele console. Het biedt de mogelijkheid om sessies te splitsen, te detacheren en opnieuw te verbinden, wat handig is voor langdurige processen of wanneer je je werk wilt voortzetten op een andere terminal.

## Gebruik
De basis syntaxis van de `screen`-opdracht is als volgt:

```csh
screen [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-S naam`: Geef een naam aan de nieuwe sessie.
- `-d -r`: Detacheren van een sessie en deze opnieuw verbinden.
- `-list`: Lijst alle actieve sessies.
- `-X commando`: Stuur een commando naar een actieve sessie.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `screen`-opdracht:

1. **Een nieuwe screen-sessie starten:**
   ```csh
   screen
   ```

2. **Een nieuwe sessie starten met een specifieke naam:**
   ```csh
   screen -S mijn_sessie
   ```

3. **Lijst van actieve screen-sessies weergeven:**
   ```csh
   screen -list
   ```

4. **Een detach sessie opnieuw verbinden:**
   ```csh
   screen -d -r mijn_sessie
   ```

5. **Een commando naar een actieve sessie sturen:**
   ```csh
   screen -S mijn_sessie -X stuff 'echo Hallo Wereld\n'
   ```

## Tips
- Gebruik `Ctrl-a d` om een sessie te detacheren zonder deze te beëindigen.
- Zorg ervoor dat je sessies een herkenbare naam hebben, vooral als je met meerdere sessies werkt.
- Maak gebruik van de `screen`-configuratiebestanden om je instellingen te personaliseren en je workflow te verbeteren.