# [Linux] C Shell (csh) iostat gebruik: Monitoren van systeeminvoer/uitvoer

## Overzicht
De `iostat`-opdracht is een hulpmiddel dat informatie biedt over de invoer- en uitvoeractiviteit van schijven en de CPU-belasting. Het helpt systeembeheerders bij het analyseren van de prestaties van opslagapparaten en het identificeren van knelpunten.

## Gebruik
De basisstructuur van de `iostat`-opdracht is als volgt:

```csh
iostat [opties] [argumenten]
```

## Veelvoorkomende opties
- `-c`: Toont alleen CPU-statistieken.
- `-d`: Toont alleen schijfstatistieken.
- `-x`: Toont uitgebreide schijfstatistieken.
- `-k`: Geeft de resultaten weer in kilobytes per seconde.
- `-t`: Toont de tijdstempel bij de uitvoer.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `iostat`-opdracht:

1. **Basisinformatie over CPU en schijven weergeven:**
   ```csh
   iostat
   ```

2. **Alleen CPU-statistieken weergeven:**
   ```csh
   iostat -c
   ```

3. **Uitgebreide schijfstatistieken weergeven:**
   ```csh
   iostat -x
   ```

4. **Statistieken in kilobytes per seconde weergeven:**
   ```csh
   iostat -k
   ```

5. **Statistieken met tijdstempel weergeven:**
   ```csh
   iostat -t
   ```

## Tips
- Gebruik de `-x` optie voor gedetailleerde informatie over schijfprestaties, wat nuttig kan zijn voor diepgaande analyses.
- Combineer opties om specifieke informatie te krijgen die relevant is voor jouw situatie, zoals `iostat -cx` voor zowel CPU als uitgebreide schijfstatistieken.
- Monitor regelmatig de uitvoer van `iostat` om trends in systeemgebruik te identificeren en proactief te reageren op mogelijke problemen.