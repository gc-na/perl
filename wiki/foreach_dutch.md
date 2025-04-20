# [Linux] C Shell (csh) foreach gebruik: Herhaal een commando voor elke waarde in een lijst

## Overview
De `foreach`-opdracht in C Shell (csh) wordt gebruikt om een commando of een reeks commando's uit te voeren voor elke waarde in een opgegeven lijst. Dit maakt het mogelijk om taken efficiënt te automatiseren en herhalende processen te vereenvoudigen.

## Usage
De basis syntaxis van de `foreach`-opdracht is als volgt:

```csh
foreach variable (lijst)
    commando's
end
```

## Common Options
De `foreach`-opdracht heeft geen specifieke opties, maar het is belangrijk om de juiste syntaxis te volgen en de juiste commando's binnen de loop te plaatsen.

## Common Examples

### Voorbeeld 1: Eenvoudige loop
Dit voorbeeld toont hoe je een eenvoudige loop kunt maken om een reeks getallen af te drukken.

```csh
foreach i (1 2 3 4 5)
    echo "Getal: $i"
end
```

### Voorbeeld 2: Bestanden verwerken
Hier is een voorbeeld dat alle `.txt`-bestanden in de huidige directory afdrukt.

```csh
foreach bestand (*.txt)
    echo "Bestand: $bestand"
end
```

### Voorbeeld 3: Combineren met andere commando's
Je kunt `foreach` ook combineren met andere commando's, zoals `mv`, om bestanden te hernoemen.

```csh
foreach bestand (*.jpg)
    mv $bestand $bestand:r.old
end
```

## Tips
- Zorg ervoor dat je de `end`-instructie niet vergeet; dit sluit de `foreach`-loop af.
- Gebruik haakjes om de lijst van waarden correct te definiëren.
- Test je commando's met een kleine dataset voordat je ze op een grote hoeveelheid gegevens toepast, om onbedoelde wijzigingen te voorkomen.