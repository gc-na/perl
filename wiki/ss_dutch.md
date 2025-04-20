# [Linux] C Shell (csh) ss gebruik: Netwerkverbindingen weergeven

## Overzicht
De `ss`-opdracht is een krachtig hulpmiddel voor het weergeven van socketstatistieken en netwerkverbindingen op een systeem. Het biedt gedetailleerde informatie over actieve verbindingen, inclusief TCP, UDP en andere sockettypes.

## Gebruik
De basis syntaxis van de `ss`-opdracht is als volgt:

```csh
ss [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-t`: Toon alleen TCP-sockets.
- `-u`: Toon alleen UDP-sockets.
- `-l`: Toon alleen luisterende sockets.
- `-p`: Toon het proces dat de socket gebruikt.
- `-n`: Toon IP-adressen en poorten in numerieke vorm in plaats van de hostnamen.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `ss`-opdracht:

1. **Toon alle actieve TCP-verbindingen:**
   ```csh
   ss -t
   ```

2. **Toon alle actieve UDP-verbindingen:**
   ```csh
   ss -u
   ```

3. **Toon alleen luisterende sockets:**
   ```csh
   ss -l
   ```

4. **Toon actieve verbindingen met procesinformatie:**
   ```csh
   ss -t -p
   ```

5. **Toon verbindingen met numerieke adressen:**
   ```csh
   ss -n
   ```

## Tips
- Gebruik de `-p` optie om te zien welke processen de verbindingen gebruiken; dit kan nuttig zijn voor probleemoplossing.
- Combineer opties voor meer gerichte resultaten, bijvoorbeeld `ss -t -l` om alleen luisterende TCP-sockets te zien.
- Vergeet niet dat je mogelijk root-rechten nodig hebt om bepaalde socketinformatie te bekijken, vooral die van andere gebruikers.