# [Linux] C Shell (csh) script gebruik: Maak een opname van terminalsessies

## Overzicht
Het `script` commando wordt gebruikt om een opname van een terminalsessie te maken. Dit is handig voor het vastleggen van uitvoer en interacties in de terminal, wat nuttig kan zijn voor documentatie of het delen van informatie.

## Gebruik
De basis syntaxis van het `script` commando is als volgt:

```
script [opties] [bestandsnaam]
```

Hierbij is `bestandsnaam` de naam van het bestand waarin de sessie-opname wordt opgeslagen. Als geen bestandsnaam wordt opgegeven, wordt de opname standaard opgeslagen in een bestand genaamd `typescript`.

## Veelvoorkomende Opties
- `-a`: Voeg de uitvoer toe aan een bestaand bestand in plaats van het te overschrijven.
- `-f`: Schrijf de uitvoer onmiddellijk naar het bestand, in plaats van te bufferen.
- `-q`: Voer het script uit zonder een welkomstbericht weer te geven.

## Veelvoorkomende Voorbeelden

1. **Basis gebruik zonder bestandsnaam**:
   ```csh
   script
   ```
   Dit start een nieuwe sessie en slaat de uitvoer op in `typescript`.

2. **Opname naar een specifiek bestand**:
   ```csh
   script mijn_opname.txt
   ```
   Dit start een sessie en slaat de uitvoer op in `mijn_opname.txt`.

3. **Voeg uitvoer toe aan een bestaand bestand**:
   ```csh
   script -a bestaande_opname.txt
   ```
   Dit voegt nieuwe uitvoer toe aan `bestaande_opname.txt`.

4. **Directe uitvoer naar bestand zonder bufferen**:
   ```csh
   script -f snelle_opname.txt
   ```
   Dit schrijft de uitvoer onmiddellijk naar `snelle_opname.txt`.

5. **Gebruik zonder welkomstbericht**:
   ```csh
   script -q stille_opname.txt
   ```
   Dit start de opname zonder een welkomstbericht weer te geven.

## Tips
- Zorg ervoor dat je het `script` commando afsluit met `exit` om de opname correct te beëindigen.
- Controleer de inhoud van het opnamebestand met `cat` of `less` om te zien wat er is vastgelegd.
- Gebruik de `-f` optie als je real-time uitvoer wilt vastleggen, wat handig kan zijn voor lange processen.