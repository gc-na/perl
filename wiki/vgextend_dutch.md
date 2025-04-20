# [Linux] C Shell (csh) vgextend gebruik: Voeg fysieke volumes toe aan een volume group

## Overzicht
De `vgextend` opdracht wordt gebruikt om fysieke volumes toe te voegen aan een bestaande volume group in een Logical Volume Manager (LVM) omgeving. Dit stelt gebruikers in staat om de opslagcapaciteit van een volume group uit te breiden.

## Gebruik
De basis syntaxis van de `vgextend` opdracht is als volgt:

```csh
vgextend [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-l, --extents`: Specificeer het aantal extents dat moet worden toegevoegd.
- `-n, --noheadings`: Voorkom dat kopteksten worden weergegeven in de uitvoer.
- `--test`: Voer een test uit zonder wijzigingen aan te brengen.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `vgextend` opdracht:

1. Voeg een fysiek volume toe aan een volume group:
   ```csh
   vgextend mijn_volume_group /dev/sdb1
   ```

2. Voeg meerdere fysieke volumes toe aan een volume group:
   ```csh
   vgextend mijn_volume_group /dev/sdb1 /dev/sdc1
   ```

3. Voer een test uit om te controleren wat er zou gebeuren zonder wijzigingen aan te brengen:
   ```csh
   vgextend --test mijn_volume_group /dev/sdb1
   ```

## Tips
- Zorg ervoor dat de fysieke volumes die je wilt toevoegen, geconfigureerd zijn en beschikbaar zijn voordat je de `vgextend` opdracht uitvoert.
- Controleer altijd de status van je volume group na het uitvoeren van de `vgextend` opdracht met `vgdisplay` om te bevestigen dat de volumes correct zijn toegevoegd.
- Gebruik de `--test` optie om te voorkomen dat je onbedoeld wijzigingen aanbrengt tijdens het testen van je commando's.