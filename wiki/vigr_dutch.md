# [Linux] C Shell (csh) vigr gebruik: Bewerken van de /etc/hosts-bestanden

## Overzicht
De `vigr`-opdracht wordt gebruikt om het `/etc/passwd`- of `/etc/group`-bestand veilig te bewerken. Het opent deze bestanden in een teksteditor en zorgt ervoor dat er geen gelijktijdige wijzigingen plaatsvinden, wat kan leiden tot corruptie van de bestanden.

## Gebruik
De basis syntaxis van de `vigr`-opdracht is als volgt:

```csh
vigr [opties] [bestanden]
```

## Veelvoorkomende Opties
- `-s`: Voer een syntaxiscontrole uit op het bestand voordat het wordt geopend.
- `-f`: Specificeer een ander bestand dan de standaard `/etc/passwd` of `/etc/group` om te bewerken.

## Veelvoorkomende Voorbeelden

1. **Basisgebruik van vigr**:
   Open het standaard `/etc/passwd`-bestand voor bewerking.
   ```csh
   vigr
   ```

2. **Bewerken van het group-bestand**:
   Open het `/etc/group`-bestand voor bewerking.
   ```csh
   vigr /etc/group
   ```

3. **Syntaxiscontrole uitvoeren**:
   Voer een syntaxiscontrole uit op het `/etc/passwd`-bestand voordat je het opent.
   ```csh
   vigr -s
   ```

4. **Een ander bestand bewerken**:
   Open een specifiek bestand, bijvoorbeeld `/etc/myconfig`, voor bewerking.
   ```csh
   vigr -f /etc/myconfig
   ```

## Tips
- Gebruik `vigr` altijd in plaats van een gewone teksteditor voor het bewerken van systeemconfiguratiebestanden om gegevenscorruptie te voorkomen.
- Maak altijd een back-up van belangrijke bestanden voordat je ze bewerkt.
- Zorg ervoor dat je voldoende rechten hebt om de bestanden te bewerken, meestal is root-toegang vereist.