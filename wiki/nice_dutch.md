# [Linux] C Shell (csh) nice gebruik: Beheer de prioriteit van processen

## Overzicht
De `nice`-opdracht in C Shell (csh) wordt gebruikt om de prioriteit van processen te beheren. Hiermee kun je de CPU-tijd die aan een proces wordt toegewezen, verhogen of verlagen, afhankelijk van de gewenste prioriteit.

## Gebruik
De basis syntaxis van de `nice`-opdracht is als volgt:

```csh
nice [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-n` : Hiermee kun je de prioriteit specificeren. De standaardwaarde is 10. Een hogere waarde betekent een lagere prioriteit.
- `-h` : Geeft een helpbericht weer met informatie over het gebruik van de opdracht.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `nice`:

1. Start een proces met een lagere prioriteit:
   ```csh
   nice -n 10 myscript.sh
   ```

2. Start een proces met een hogere prioriteit:
   ```csh
   nice -n -5 myscript.sh
   ```

3. Controleer de huidige prioriteit van een proces:
   ```csh
   ps -o pid,nice,cmd
   ```

4. Verhoog de prioriteit van een lopend proces:
   ```csh
   renice -n -5 -p 1234
   ```

## Tips
- Gebruik `nice` om ervoor te zorgen dat achtergrondprocessen de prestaties van belangrijke taken niet beïnvloeden.
- Wees voorzichtig met het verlagen van de prioriteit van processen, omdat dit kan leiden tot langere wachttijden voor gebruikersinteracties.
- Controleer regelmatig de prioriteiten van actieve processen met `ps` om een goed overzicht te behouden.