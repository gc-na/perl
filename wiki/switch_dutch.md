# [Linux] C Shell (csh) switch gebruik: Verander de uitvoer van een commando

## Overzicht
De `switch`-opdracht in C Shell (csh) wordt gebruikt om verschillende voorwaarden te evalueren en op basis daarvan acties uit te voeren. Het is vergelijkbaar met een reeks if-else-verklaringen, maar biedt een meer gestructureerde manier om meerdere opties te beheren.

## Gebruik
De basis syntaxis van de `switch`-opdracht is als volgt:

```csh
switch (expressie)
    case patroon1:
        commando's
        breaksw
    case patroon2:
        commando's
        breaksw
    default:
        commando's
        breaksw
endsw
```

## Veelvoorkomende opties
- `case`: Definieert een patroon dat vergeleken wordt met de expressie.
- `breaksw`: Beëindigt de huidige case en gaat verder met de uitvoering na de switch.
- `default`: Voert commando's uit als geen van de andere patronen overeenkomt.

## Veelvoorkomende voorbeelden

### Voorbeeld 1: Eenvoudige switch
```csh
set kleur = "rood"
switch ($kleur)
    case "rood":
        echo "De kleur is rood."
        breaksw
    case "blauw":
        echo "De kleur is blauw."
        breaksw
    default:
        echo "Onbekende kleur."
        breaksw
endsw
```

### Voorbeeld 2: Meerdere opties
```csh
set fruit = "appel"
switch ($fruit)
    case "appel":
        echo "Je hebt een appel gekozen."
        breaksw
    case "banaan":
        echo "Je hebt een banaan gekozen."
        breaksw
    case "sinaasappel":
        echo "Je hebt een sinaasappel gekozen."
        breaksw
    default:
        echo "Onbekend fruit."
        breaksw
endsw
```

### Voorbeeld 3: Gebruik van variabelen
```csh
set getal = 2
switch ($getal)
    case 1:
        echo "Het getal is één."
        breaksw
    case 2:
        echo "Het getal is twee."
        breaksw
    case 3:
        echo "Het getal is drie."
        breaksw
    default:
        echo "Getal niet herkend."
        breaksw
endsw
```

## Tips
- Zorg ervoor dat je de juiste haakjes gebruikt bij de expressie.
- Gebruik `breaksw` om te voorkomen dat de uitvoering doorloopt naar de volgende case.
- Houd de patronen eenvoudig en duidelijk voor betere leesbaarheid en onderhoudbaarheid van je scripts.