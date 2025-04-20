# [Nederlandse] C Shell (csh) mtr gebruik: Netwerkdiagnose en traceroute

## Overzicht
De `mtr` (My Traceroute) opdracht is een netwerkdiagnosetool die de functionaliteit van `ping` en `traceroute` combineert. Het helpt gebruikers om de route die gegevenspakketten volgen naar een specifieke host te analyseren en de netwerkprestaties te evalueren.

## Gebruik
De basis syntaxis van de `mtr` opdracht is als volgt:

```csh
mtr [opties] [doel]
```

## Veelvoorkomende Opties
- `-r`: Voer een rapportmodus uit, wat betekent dat de uitvoer in een meer gestructureerd formaat wordt weergegeven.
- `-c <aantal>`: Specificeert het aantal pings dat moet worden verzonden.
- `-i <interval>`: Bepaalt het interval tussen de pings in seconden.
- `-p`: Voer de opdracht uit in de 'ping'-modus, wat betekent dat het alleen de pingresultaten toont zonder de traceroute-informatie.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `mtr`:

1. Basisgebruik om de route naar een host te traceren:
    ```csh
    mtr example.com
    ```

2. Rapportmodus gebruiken om een gestructureerd overzicht te krijgen:
    ```csh
    mtr -r example.com
    ```

3. Een specifiek aantal pings verzenden:
    ```csh
    mtr -c 10 example.com
    ```

4. Pings met een interval van 2 seconden verzenden:
    ```csh
    mtr -i 2 example.com
    ```

5. Alleen de pingresultaten tonen:
    ```csh
    mtr -p example.com
    ```

## Tips
- Gebruik de rapportmodus (`-r`) voor een overzichtelijke weergave van de resultaten, vooral als je de gegevens wilt delen.
- Experimenteer met verschillende intervallen en aantallen pings om een beter beeld te krijgen van de netwerkprestaties.
- Combineer `mtr` met andere netwerktools zoals `ping` en `traceroute` voor een uitgebreide diagnose van netwerkproblemen.