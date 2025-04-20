# [Linux] C Shell (csh) mpstat gebruik: Monitoren van CPU-activiteit

## Overzicht
De `mpstat` opdracht is een nuttig hulpmiddel voor het monitoren van de CPU-activiteit op een systeem. Het geeft gedetailleerde informatie over de prestaties van de CPU's, inclusief het percentage tijd dat elke CPU bezig is met verschillende taken zoals gebruikersprocessen, systeemprocessen en idle tijd.

## Gebruik
De basis syntaxis van de `mpstat` opdracht is als volgt:

```csh
mpstat [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-P ALL`: Toon statistieken voor alle CPU's.
- `-u`: Toon alleen de CPU-gebruikstatistieken.
- `-h`: Toon een helpbericht met informatie over het gebruik van de opdracht.
- `interval`: Geef de tijdsinterval in seconden op voor herhaalde metingen.

## Veelvoorkomende Voorbeelden

1. **Basisgebruik**: Toon de CPU-statistieken voor alle CPU's.
   ```csh
   mpstat -P ALL
   ```

2. **CPU-gebruikstatistieken**: Toon alleen de CPU-gebruikstatistieken.
   ```csh
   mpstat -u
   ```

3. **Herhaalde metingen**: Toon de CPU-statistieken elke 5 seconden.
   ```csh
   mpstat 5
   ```

4. **Statistieken voor specifieke CPU**: Toon de statistieken voor CPU 0.
   ```csh
   mpstat -P 0
   ```

## Tips
- Gebruik de `-P ALL` optie om een volledig overzicht van alle CPU's te krijgen, wat handig is voor systemen met meerdere CPU's.
- Combineer `mpstat` met andere monitoringtools zoals `top` of `htop` voor een uitgebreidere analyse van systeemprestaties.
- Controleer regelmatig de CPU-statistieken om trends in gebruik te identificeren en mogelijke knelpunten in de prestaties te ontdekken.