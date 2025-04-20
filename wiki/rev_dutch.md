# [Linux] C Shell (csh) rev: Tekst omkeren

## Overzicht
De `rev` opdracht in C Shell (csh) wordt gebruikt om de volgorde van de karakters in elke regel van een bestand om te keren. Dit kan nuttig zijn voor verschillende tekstverwerkingsdoeleinden.

## Gebruik
De basis syntaxis van de `rev` opdracht is als volgt:

```csh
rev [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-` : Leest de invoer van de standaardinvoer in plaats van een bestand.
- `-o` : Schrijft de omgekeerde tekst naar een specifiek uitvoerbestand.

## Veelvoorkomende Voorbeelden

1. **Omgekeerde tekst van een bestand weergeven:**
   ```csh
   rev bestand.txt
   ```

2. **Omgekeerde tekst van de standaardinvoer:**
   ```csh
   echo "Hallo Wereld" | rev
   ```

3. **Omgekeerde tekst naar een nieuw bestand schrijven:**
   ```csh
   rev bestand.txt > omgekeerd.txt
   ```

4. **Omgekeerde tekst met een specifieke uitvoer:**
   ```csh
   rev -o uitvoer.txt bestand.txt
   ```

## Tips
- Gebruik `rev` in combinatie met andere commando's via een pijp (`|`) voor meer complexe tekstverwerking.
- Controleer altijd de uitvoer van `rev` met een klein bestand voordat je het op grotere bestanden toepast om onverwachte resultaten te voorkomen.
- Vergeet niet dat `rev` de tekst per regel omkeert, dus als je meerdere regels hebt, wordt elke regel afzonderlijk omgekeerd.