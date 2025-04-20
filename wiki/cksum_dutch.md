# [Linux] C Shell (csh) cksum gebruik: Controleer de controlegetallen van bestanden

## Overzicht
De `cksum`-opdracht in C Shell (csh) wordt gebruikt om de controlegetallen (checksum) van bestanden te berekenen. Dit kan nuttig zijn voor het verifiëren van de integriteit van bestanden door te controleren of ze niet zijn gewijzigd.

## Gebruik
De basis syntaxis van de `cksum`-opdracht is als volgt:

```csh
cksum [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-a`: Specificeert het algoritme dat gebruikt moet worden voor het berekenen van de checksum.
- `-b`: Voert de controle uit in binaire modus.
- `-h`: Geeft een helpbericht weer met informatie over het gebruik van de opdracht.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `cksum`-opdracht:

1. Bereken de checksum van een enkel bestand:
   ```csh
   cksum bestand.txt
   ```

2. Bereken de checksums van meerdere bestanden:
   ```csh
   cksum bestand1.txt bestand2.txt bestand3.txt
   ```

3. Gebruik de `-a` optie om een specifiek algoritme te kiezen:
   ```csh
   cksum -a md5 bestand.txt
   ```

4. Sla de output van de checksum op in een bestand:
   ```csh
   cksum bestand.txt > checksum.txt
   ```

## Tips
- Controleer regelmatig de checksums van belangrijke bestanden om te zorgen dat ze niet zijn beschadigd of gewijzigd.
- Gebruik de `-b` optie als je werkt met binaire bestanden om nauwkeurige resultaten te garanderen.
- Bewaar de checksums van bestanden in een aparte tekstbestand voor toekomstige referentie en verificatie.