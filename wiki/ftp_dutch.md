# [Nederlandse] C Shell (csh) ftp gebruik: Bestandsoverdracht via het netwerk

## Overzicht
De `ftp`-opdracht in de C Shell (csh) wordt gebruikt voor het overdragen van bestanden tussen computers via het File Transfer Protocol (FTP). Het stelt gebruikers in staat om bestanden te uploaden en te downloaden van en naar een FTP-server.

## Gebruik
De basis syntaxis van de `ftp`-opdracht is als volgt:

```csh
ftp [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-v`: Verhoogt de uitvoer van de opdracht, waardoor meer details over de verbinding en overdracht worden weergegeven.
- `-n`: Voorkomt dat ftp automatisch verbinding maakt met de standaardserver.
- `-i`: Zet de interactieve modus uit, zodat bestanden zonder bevestiging worden overgedragen.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `ftp`-opdracht:

### Verbinden met een FTP-server
```csh
ftp ftp.example.com
```

### Downloaden van een bestand
```csh
get bestand.txt
```

### Uploaden van een bestand
```csh
put lokaal_bestand.txt
```

### Lijst van bestanden op de server
```csh
ls
```

### Afsluiten van de FTP-sessie
```csh
bye
```

## Tips
- Zorg ervoor dat je de juiste inloggegevens hebt voor de FTP-server voordat je verbinding maakt.
- Gebruik de `-v` optie voor meer inzicht in de overdracht, vooral als je problemen ondervindt.
- Vergeet niet om de juiste bestandspermissies in te stellen op de server na het uploaden van bestanden.