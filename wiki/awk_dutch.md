# [Linux] C Shell (csh) awk gebruik: tekstverwerking en patroonherkenning

## Overzicht
De `awk`-opdracht is een krachtige tekstverwerkings- en patroonherkenningstool die vaak wordt gebruikt voor het analyseren van tekstbestanden en het uitvoeren van bewerkingen op gegevens. Het is bijzonder nuttig voor het verwerken van gestructureerde gegevens zoals CSV-bestanden.

## Gebruik
De basis syntaxis van de `awk`-opdracht is als volgt:

```bash
awk [opties] [argumenten]
```

## Veelvoorkomende opties
- `-F`: Stelt de scheidingsteken in voor de invoer (bijvoorbeeld `-F,` voor komma's).
- `-v`: Definieert variabelen die in de `awk`-script kunnen worden gebruikt.
- `-f`: Specificeert een bestand dat een `awk`-script bevat.

## Veelvoorkomende voorbeelden

1. **Basis tekstverwerking**
   Dit voorbeeld toont de inhoud van een bestand:

   ```bash
   awk '{print}' bestand.txt
   ```

2. **Specifieke kolom afdrukken**
   Dit voorbeeld drukt alleen de tweede kolom van een bestand af:

   ```bash
   awk '{print $2}' bestand.txt
   ```

3. **Gebruik van een scheidingsteken**
   Dit voorbeeld gebruikt een komma als scheidingsteken en drukt de eerste kolom af:

   ```bash
   awk -F, '{print $1}' bestand.csv
   ```

4. **Voorwaarden toepassen**
   Dit voorbeeld drukt alleen regels af waarin de waarde in de derde kolom groter is dan 100:

   ```bash
   awk '$3 > 100 {print}' bestand.txt
   ```

5. **Variabelen gebruiken**
   Dit voorbeeld definieert een variabele en gebruikt deze in de `awk`-opdracht:

   ```bash
   awk -v d=10 '$1 > d {print}' bestand.txt
   ```

## Tips
- Gebruik `-F` om het scheidingsteken in te stellen voor een betere controle over de invoer.
- Combineer `awk` met andere commando's zoals `grep` en `sort` voor complexe dataverwerking.
- Test je `awk`-scripts met kleine datasets voordat je ze op grotere bestanden toepast om fouten te voorkomen.