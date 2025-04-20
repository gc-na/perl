# [Linux] C Shell (csh) dstat gebruik: systeemstatistieken in real-time bekijken

## Overzicht
De `dstat`-opdracht is een veelzijdig hulpprogramma dat systeemstatistieken in real-time weergeeft. Het combineert de functionaliteit van verschillende andere tools zoals `vmstat`, `iostat`, en `netstat`, en biedt een uitgebreide weergave van systeembronnen zoals CPU-gebruik, geheugen, schijfactiviteit en netwerkverkeer.

## Gebruik
De basis syntaxis van de `dstat`-opdracht is als volgt:

```csh
dstat [opties] [argumenten]
```

## Veelvoorkomende opties
- `-c`: Toon CPU-statistieken.
- `-d`: Toon schijfactiviteit.
- `-n`: Toon netwerkactiviteit.
- `-m`: Toon geheugenstatistieken.
- `--help`: Toon de help-informatie voor dstat.

## Veelvoorkomende voorbeelden

1. **Basisgebruik**: Toon standaard systeemstatistieken.
   ```csh
   dstat
   ```

2. **CPU- en geheugenstatistieken**: Toon alleen CPU- en geheugeninformatie.
   ```csh
   dstat -c -m
   ```

3. **Schijf- en netwerkactiviteit**: Toon schijf- en netwerkactiviteit.
   ```csh
   dstat -d -n
   ```

4. **Gecombineerde statistieken**: Toon CPU, schijf en netwerk in één weergave.
   ```csh
   dstat -c -d -n
   ```

5. **Statistieken met tijdstempel**: Voeg tijdstempels toe aan de uitvoer.
   ```csh
   dstat --time
   ```

## Tips
- Gebruik `dstat` met verschillende opties om een beter inzicht te krijgen in de prestaties van je systeem.
- Experimenteer met het combineren van opties voor een meer gedetailleerde weergave van systeemstatistieken.
- Overweeg om `dstat` te gebruiken in combinatie met andere monitoringtools voor een uitgebreidere analyse van systeembronnen.