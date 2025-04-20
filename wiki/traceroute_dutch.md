# [Linux] C Shell (csh) traceroute gebruik: Netwerkpaden traceren

## Overzicht
De `traceroute`-opdracht is een netwerkdiagnosetool die de route toont die pakketten volgen van de bron naar een opgegeven doel. Het helpt bij het identificeren van netwerkproblemen door de verschillende knooppunten (routers) te tonen die de gegevens passeren.

## Gebruik
De basis syntaxis van de `traceroute`-opdracht is als volgt:

```
traceroute [opties] [doel]
```

## Veelvoorkomende Opties
- `-m <max_hops>`: Bepaalt het maximale aantal hops (routers) dat traceroute zal volgen.
- `-w <timeout>`: Stelt de timeout in voor elke hop in seconden.
- `-q <aantal>`: Bepaalt het aantal probe-pakketten dat naar elke hop wordt verzonden.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `traceroute`:

1. Basis traceroute naar een domein:
   ```csh
   traceroute example.com
   ```

2. Traceroute met een maximum van 15 hops:
   ```csh
   traceroute -m 15 example.com
   ```

3. Traceroute met een timeout van 2 seconden per hop:
   ```csh
   traceroute -w 2 example.com
   ```

4. Traceroute met 5 probes per hop:
   ```csh
   traceroute -q 5 example.com
   ```

## Tips
- Gebruik `traceroute` samen met andere netwerktools zoals `ping` om een completer beeld van netwerkproblemen te krijgen.
- Probeer verschillende opties om te zien hoe ze de uitvoer beïnvloeden en om meer inzicht te krijgen in de netwerkstructuur.
- Houd er rekening mee dat sommige netwerken ICMP-pakketten kunnen blokkeren, wat de resultaten van traceroute kan beïnvloeden.