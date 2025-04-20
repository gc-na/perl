# [Linux] C Shell (csh) yum gebruik: Beheer van softwarepakketten

## Overzicht
Het `yum`-commando is een pakketbeheerder voor Linux-distributies die RPM-pakketten gebruiken. Het stelt gebruikers in staat om software te installeren, bij te werken en te verwijderen, evenals om afhankelijkheden automatisch te beheren.

## Gebruik
De basis syntaxis van het `yum`-commando is als volgt:

```bash
yum [opties] [argumenten]
```

## Veelvoorkomende opties
- `install`: Installeert een nieuw pakket.
- `remove`: Verwijdert een geïnstalleerd pakket.
- `update`: Werkt geïnstalleerde pakketten bij naar de nieuwste versie.
- `search`: Zoekt naar pakketten in de repository.
- `info`: Toont informatie over een specifiek pakket.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `yum`:

### Een pakket installeren
```bash
yum install pakketnaam
```

### Een pakket verwijderen
```bash
yum remove pakketnaam
```

### Geïnstalleerde pakketten bijwerken
```bash
yum update
```

### Zoeken naar een pakket
```bash
yum search zoekterm
```

### Informatie over een specifiek pakket opvragen
```bash
yum info pakketnaam
```

## Tips
- Zorg ervoor dat je altijd de laatste versie van de repository's hebt door `yum update` regelmatig uit te voeren.
- Gebruik `yum clean all` om ongebruikte gegevens te verwijderen en schijfruimte vrij te maken.
- Controleer altijd de afhankelijkheden van een pakket voordat je het installeert of verwijdert om problemen te voorkomen.