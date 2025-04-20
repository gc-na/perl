# [Linux] C Shell (csh) rpm gebruik: Beheer van RPM-pakketten

## Overzicht
De `rpm`-opdracht is een pakketbeheerder voor het installeren, verwijderen en beheren van RPM-pakketten op Linux-systemen. Het biedt een manier om software te installeren en te onderhouden die in het RPM-formaat is verpakt.

## Gebruik
De basis syntaxis van de `rpm`-opdracht is als volgt:

```bash
rpm [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-i`: Installeer een nieuw pakket.
- `-e`: Verwijder een geïnstalleerd pakket.
- `-U`: Werk een geïnstalleerd pakket bij naar een nieuwere versie.
- `-q`: Vraag informatie op over een geïnstalleerd pakket.
- `--verify`: Controleer de integriteit van een pakket.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `rpm`-opdracht:

### Een nieuw pakket installeren
```bash
rpm -i pakketnaam.rpm
```

### Een geïnstalleerd pakket verwijderen
```bash
rpm -e pakketnaam
```

### Een pakket bijwerken
```bash
rpm -U pakketnaam.rpm
```

### Informatie opvragen over een geïnstalleerd pakket
```bash
rpm -q pakketnaam
```

### De integriteit van een pakket controleren
```bash
rpm --verify pakketnaam
```

## Tips
- Zorg ervoor dat je root-toegang hebt bij het installeren of verwijderen van pakketten.
- Gebruik de `-v` optie voor meer gedetailleerde uitvoer tijdens het uitvoeren van `rpm`-opdrachten.
- Controleer altijd de afhankelijkheden van een pakket voordat je het installeert om problemen te voorkomen.