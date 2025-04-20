# [Linux] C Shell (csh) netstat gebruik: Netwerkverbindingen en statistieken weergeven

## Overzicht
Het `netstat`-commando is een krachtig hulpmiddel in de C Shell (csh) dat netwerkverbindingen, routingtabellen, interface-statistieken en andere netwerkgerelateerde informatie weergeeft. Het helpt gebruikers om inzicht te krijgen in de netwerkstatus van hun systeem.

## Gebruik
De basis syntaxis van het `netstat`-commando is als volgt:

```
netstat [opties] [argumenten]
```

## Veelvoorkomende opties
- `-a`: Toont alle verbindingen en luisterende poorten.
- `-n`: Toont adressen en poorten in numerieke vorm in plaats van de hostnamen.
- `-r`: Toont de routingtabel.
- `-i`: Toont informatie over netwerkinterfaces.
- `-p`: Toont het proces dat de verbinding heeft gemaakt (vereist vaak root-rechten).

## Veelvoorkomende voorbeelden

1. **Toon alle actieve verbindingen:**
   ```csh
   netstat -a
   ```

2. **Toon verbindingen in numerieke vorm:**
   ```csh
   netstat -an
   ```

3. **Toon de routingtabel:**
   ```csh
   netstat -r
   ```

4. **Toon informatie over netwerkinterfaces:**
   ```csh
   netstat -i
   ```

5. **Toon actieve verbindingen met procesinformatie:**
   ```csh
   netstat -p
   ```

## Tips
- Gebruik de optie `-n` om de uitvoer te versnellen door DNS-resolutie te vermijden.
- Combineer opties voor meer gedetailleerde informatie, bijvoorbeeld `netstat -anp` voor actieve verbindingen met procesinformatie.
- Controleer regelmatig de netwerkstatus om ongebruikelijke verbindingen of activiteiten te detecteren.