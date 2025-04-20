# [Linux] C Shell (csh) w gebruik: Toon ingelogde gebruikers en hun activiteiten

## Overzicht
De `w` opdracht in C Shell (csh) toont een lijst van ingelogde gebruikers op het systeem, samen met informatie over hun activiteiten. Dit kan nuttig zijn voor systeembeheerders en gebruikers die willen weten wie er op het systeem is ingelogd en wat ze aan het doen zijn.

## Gebruik
De basis syntaxis van de `w` opdracht is als volgt:

```
w [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-h`: Verberg de header van de uitvoer.
- `-s`: Toon een kortere uitvoer zonder extra informatie.
- `-u`: Sorteer de uitvoer op gebruikersnaam.

## Veelvoorkomende Voorbeelden

1. **Basisgebruik**: Toont alle ingelogde gebruikers en hun activiteiten.
   ```csh
   w
   ```

2. **Verberg de header**: Toont alleen de lijst van ingelogde gebruikers zonder de koptekst.
   ```csh
   w -h
   ```

3. **Korte uitvoer**: Toont een beknopte versie van de informatie.
   ```csh
   w -s
   ```

4. **Sorteer op gebruikersnaam**: Toont de lijst van ingelogde gebruikers gesorteerd op naam.
   ```csh
   w -u
   ```

## Tips
- Gebruik `w` regelmatig om een overzicht te krijgen van wie er op het systeem is ingelogd en wat ze doen.
- Combineer de opties voor een meer gerichte uitvoer, bijvoorbeeld `w -hu` om een korte lijst zonder header te krijgen.
- Houd rekening met privacy; deel de uitvoer van `w` niet openbaar, omdat het informatie over andere gebruikers bevat.