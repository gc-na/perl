# [Linux] C Shell (csh) vmstat gebruik: Toegang tot systeemstatistieken

## Overzicht
Het `vmstat` commando geeft informatie over processen, geheugen, paging, block I/O, traps en CPU-activiteit. Het is een nuttig hulpmiddel voor systeembeheerders om de prestaties van een systeem te monitoren en te analyseren.

## Gebruik
De basis syntaxis van het `vmstat` commando is als volgt:

```csh
vmstat [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-a`: Toon actieve en inactieve geheugenstatistieken.
- `-m`: Toon informatie over geheugenpagina's.
- `-s`: Toon een samenvatting van systeemstatistieken.
- `interval`: Geef een tijdsinterval in seconden op voor herhaalde uitvoer.
- `count`: Het aantal keren dat de uitvoer herhaald moet worden.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `vmstat`:

1. **Basis uitvoer van systeemstatistieken**:
   ```csh
   vmstat
   ```

2. **Herhaalde uitvoer elke 5 seconden**:
   ```csh
   vmstat 5
   ```

3. **Toon actieve en inactieve geheugenstatistieken**:
   ```csh
   vmstat -a
   ```

4. **Toon een samenvatting van systeemstatistieken**:
   ```csh
   vmstat -s
   ```

5. **Herhaalde uitvoer elke 2 seconden, 10 keer**:
   ```csh
   vmstat 2 10
   ```

## Tips
- Gebruik `vmstat` in combinatie met andere monitoring tools voor een vollediger beeld van de systeemprestaties.
- Let op de CPU-activiteit en geheugenstatistieken om knelpunten in de prestaties te identificeren.
- Experimenteer met verschillende opties om de meest relevante informatie voor jouw situatie te verkrijgen.