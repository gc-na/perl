# [Linux] C Shell (csh) tee gebruik: Schrijven naar bestanden en naar de standaarduitvoer

## Overzicht
De `tee`-opdracht in C Shell (csh) wordt gebruikt om de uitvoer van een commando zowel naar de standaarduitvoer (meestal het scherm) als naar één of meer bestanden te schrijven. Dit is handig wanneer je de uitvoer wilt bekijken en tegelijkertijd wilt opslaan.

## Gebruik
De basis syntaxis van de `tee`-opdracht is als volgt:

```csh
tee [opties] [argumenten]
```

## Veelvoorkomende opties
- `-a`: Voeg de uitvoer toe aan het bestand in plaats van het te overschrijven.
- `-i`: Negeer signalen, wat handig kan zijn in bepaalde situaties.

## Veelvoorkomende voorbeelden

1. **Basisgebruik**: Schrijf de uitvoer van een commando naar een bestand en naar het scherm.
   ```csh
   echo "Hallo, wereld!" | tee output.txt
   ```

2. **Uitvoer toevoegen aan een bestand**: Voeg uitvoer toe aan een bestaand bestand zonder het te overschrijven.
   ```csh
   echo "Een nieuwe regel" | tee -a output.txt
   ```

3. **Meerdere bestanden**: Schrijf de uitvoer naar meerdere bestanden.
   ```csh
   echo "Dit is een test" | tee bestand1.txt bestand2.txt
   ```

4. **Gebruik met andere commando's**: Combineer `tee` met andere commando's in een pijplijn.
   ```csh
   ls -l | tee bestand_lijst.txt | grep "txt"
   ```

## Tips
- Gebruik de `-a` optie als je niet wilt dat bestaande bestanden worden overschreven.
- Combineer `tee` met andere commando's om de uitvoer te filteren of te manipuleren voordat je deze opslaat.
- Vergeet niet dat `tee` de uitvoer naar het scherm toont, dus als je alleen naar een bestand wilt schrijven, moet je de uitvoer omleiden met `>` in plaats van `| tee`.