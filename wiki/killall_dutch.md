# [Linux] C Shell (csh) killall gebruik: Beëindig processen op basis van naam

## Overzicht
De `killall` opdracht in C Shell (csh) wordt gebruikt om processen te beëindigen op basis van hun naam. Dit is handig wanneer je meerdere instanties van een programma wilt afsluiten zonder elk proces afzonderlijk te identificeren.

## Gebruik
De basis syntaxis van de `killall` opdracht is als volgt:

```csh
killall [opties] [argumenten]
```

## Veelvoorkomende opties
- `-u`: Beëindig alleen processen die door de opgegeven gebruiker worden uitgevoerd.
- `-9`: Dwingt het beëindigen van processen, vergelijkbaar met het gebruik van `SIGKILL`.
- `-v`: Toon gedetailleerde uitvoer van de processen die worden beëindigd.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `killall`:

1. Beëindig alle processen met de naam `firefox`:

    ```csh
    killall firefox
    ```

2. Beëindig alle processen met de naam `gedit` met een dwingende optie:

    ```csh
    killall -9 gedit
    ```

3. Beëindig alle processen van een specifieke gebruiker, bijvoorbeeld `jan`:

    ```csh
    killall -u jan
    ```

4. Toon gedetailleerde uitvoer terwijl je processen beëindigt:

    ```csh
    killall -v firefox
    ```

## Tips
- Gebruik `killall` met voorzichtigheid, vooral met de `-9` optie, omdat dit processen onmiddellijk beëindigt zonder ze de kans te geven om hun werk op te slaan.
- Controleer altijd welke processen je wilt beëindigen met `ps` of `pgrep` voordat je `killall` gebruikt.
- Overweeg het gebruik van `kill` voor specifieke proces-ID's als je slechts één proces wilt beëindigen.