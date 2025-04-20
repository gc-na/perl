# [Linux] C Shell (csh) traceroute6 gebruik: Netwerkroute traceren voor IPv6

## Overzicht
De `traceroute6` opdracht is een netwerkdiagnosetool die de route toont die pakketten volgen van de bron naar een opgegeven IPv6-doel. Het helpt bij het identificeren van netwerkproblemen door de verschillende knooppunten (routers) te tonen die de gegevens passeren.

## Gebruik
De basis syntaxis van de `traceroute6` opdracht is als volgt:

```csh
traceroute6 [opties] [doel]
```

## Veelvoorkomende Opties
- `-m <max_hops>`: Stel het maximale aantal hops in dat traceren kan.
- `-n`: Toon IP-adressen in plaats van hostnamen.
- `-p <poort>`: Specificeer de poort die gebruikt moet worden voor de traceroute.
- `-w <timeout>`: Stel de timeout in voor het wachten op een antwoord van elke hop.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `traceroute6`:

1. Basis traceroute naar een IPv6-adres:
   ```csh
   traceroute6 2001:db8::1
   ```

2. Traceroute met een maximum van 15 hops:
   ```csh
   traceroute6 -m 15 2001:db8::1
   ```

3. Traceroute zonder hostnamen, alleen IP-adressen:
   ```csh
   traceroute6 -n 2001:db8::1
   ```

4. Traceroute met een specifieke poort (bijvoorbeeld poort 80):
   ```csh
   traceroute6 -p 80 2001:db8::1
   ```

5. Traceroute met een aangepaste timeout van 2 seconden:
   ```csh
   traceroute6 -w 2 2001:db8::1
   ```

## Tips
- Gebruik de `-n` optie als je snel resultaten wilt zonder dat de resolutie van hostnamen de snelheid beïnvloedt.
- Experimenteer met de `-m` optie om te begrijpen hoe ver de pakketten reizen in je netwerk.
- Houd rekening met firewalls die ICMP-pakketten kunnen blokkeren, wat de resultaten kan beïnvloeden.