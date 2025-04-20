# [Linux] C Shell (csh) iconv gebruik: Tekstcodering converteren

## Overzicht
De `iconv`-opdracht wordt gebruikt om tekstbestanden van de ene codering naar de andere te converteren. Dit is handig wanneer je bestanden hebt die in verschillende tekencoderingen zijn opgeslagen en je ze wilt uniformeren.

## Gebruik
De basis syntaxis van de `iconv`-opdracht is als volgt:

```csh
iconv [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-f, --from-code CODE`: Specificeert de broncodering van het invoerbestand.
- `-t, --to-code CODE`: Specificeert de doelcodering voor het uitvoerbestand.
- `-o, --output FILE`: Bepaalt het uitvoerbestand. Als dit niet wordt opgegeven, wordt de uitvoer naar de standaarduitvoer gestuurd.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `iconv`:

1. **Converteer een bestand van ISO-8859-1 naar UTF-8**:
   ```csh
   iconv -f ISO-8859-1 -t UTF-8 input.txt -o output.txt
   ```

2. **Converteer een bestand van UTF-16 naar UTF-8**:
   ```csh
   iconv -f UTF-16 -t UTF-8 input.txt -o output.txt
   ```

3. **Directe conversie naar de standaarduitvoer**:
   ```csh
   iconv -f WINDOWS-1252 -t UTF-8 input.txt
   ```

4. **Converteer meerdere bestanden**:
   ```csh
   for file in *.txt; do
       iconv -f ISO-8859-1 -t UTF-8 "$file" -o "converted_$file"
   done
   ```

## Tips
- Controleer altijd de codering van je bestanden voordat je ze converteert, om fouten te voorkomen.
- Gebruik de `-o` optie om uitvoerbestanden te specificeren, zodat je de originele bestanden niet overschrijft.
- Test de conversie met een klein bestand voordat je grote bestanden verwerkt, om te controleren of de resultaten naar wens zijn.