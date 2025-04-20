# [Linux] C Shell (csh) nl: Lijnnummering van bestanden

## Overview
De `nl` opdracht in C Shell (csh) wordt gebruikt om de regels van een tekstbestand te nummeren. Dit is handig voor het verbeteren van de leesbaarheid en het verwijzen naar specifieke delen van een bestand.

## Usage
De basis syntaxis van de `nl` opdracht is als volgt:

```csh
nl [opties] [argumenten]
```

## Common Options
Hier zijn enkele veelvoorkomende opties voor de `nl` opdracht:

- `-b` : Bepaalt hoe regels worden genummerd. Bijvoorbeeld, `-b a` nummer alle regels.
- `-f` : Geeft aan dat lege regels niet moeten worden genummerd.
- `-n` : Bepaalt het nummerformaat. Bijvoorbeeld, `-n ln` voor links uitgelijnde nummers.
- `-w` : Bepaalt de breedte van het nummer.

## Common Examples
Hier zijn enkele praktische voorbeelden van het gebruik van de `nl` opdracht:

1. Nummer alle regels van een bestand:
   ```csh
   nl bestand.txt
   ```

2. Nummer alleen niet-lege regels:
   ```csh
   nl -b t bestand.txt
   ```

3. Nummer regels met een specifieke breedte:
   ```csh
   nl -w 5 bestand.txt
   ```

4. Nummer regels en sla de uitvoer op in een nieuw bestand:
   ```csh
   nl bestand.txt > genummerd_bestand.txt
   ```

## Tips
- Gebruik de `-b` optie om te bepalen welke regels genummerd moeten worden, afhankelijk van je behoeften.
- Experimenteer met de `-n` en `-w` opties om de opmaak van de nummering aan te passen aan je voorkeur.
- Combineer `nl` met andere commando's zoals `cat` of `more` voor een betere presentatie van genummerde bestanden.