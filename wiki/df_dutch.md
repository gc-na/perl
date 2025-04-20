# [Linux] C Shell (csh) df Gebruik: Toont schijfruimte-informatie

## Overzicht
De `df`-opdracht in C Shell (csh) wordt gebruikt om informatie weer te geven over de beschikbare schijfruimte op de bestandssystemen van een systeem. Het toont de totale, gebruikte en beschikbare ruimte op elk gemonteerd bestandssysteem.

## Gebruik
De basis syntaxis van de `df`-opdracht is als volgt:

```csh
df [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-h`: Toont de schijfruimte in een leesbaar formaat (bijv. KB, MB, GB).
- `-T`: Toont het type van elk bestandssysteem.
- `-a`: Toont ook de bestandssystemen die geen ruimte gebruiken.
- `-i`: Toont informatie over inodes in plaats van schijfruimte.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `df`-opdracht:

1. **Basisinformatie over schijfruimte:**
   ```csh
   df
   ```

2. **Leesbare schijfruimte-informatie:**
   ```csh
   df -h
   ```

3. **Toon het type van elk bestandssysteem:**
   ```csh
   df -T
   ```

4. **Toon ook lege bestandssystemen:**
   ```csh
   df -a
   ```

5. **Informatie over inodes:**
   ```csh
   df -i
   ```

## Tips
- Gebruik de `-h` optie voor een gemakkelijker te begrijpen weergave van schijfruimte.
- Combineer opties om meer gedetailleerde informatie te krijgen, bijvoorbeeld `df -hT`.
- Controleer regelmatig de schijfruimte om te voorkomen dat je schijf vol raakt, wat kan leiden tot systeemproblemen.