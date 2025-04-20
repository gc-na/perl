# [Linux] C Shell (csh) fsck gebruik: Controleer en repareer bestandssystemen

## Overzicht
De `fsck` (file system check) opdracht wordt gebruikt om bestandssystemen te controleren en te repareren. Het is een essentieel hulpmiddel voor systeembeheerders om de integriteit van schijven te waarborgen en eventuele fouten te verhelpen.

## Gebruik
De basis syntaxis van de `fsck` opdracht is als volgt:

```csh
fsck [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-a`: Probeert automatisch fouten te repareren zonder bevestiging.
- `-n`: Voert een controle uit zonder wijzigingen aan te brengen.
- `-y`: Bevestigt automatisch alle reparaties.
- `-t`: Geeft de tijd weer die nodig is voor de controle.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `fsck`:

1. Controleer een specifiek bestandssysteem:
   ```csh
   fsck /dev/sda1
   ```

2. Voer een automatische reparatie uit:
   ```csh
   fsck -a /dev/sda1
   ```

3. Controleer zonder wijzigingen aan te brengen:
   ```csh
   fsck -n /dev/sda1
   ```

4. Bevestig automatisch alle reparaties:
   ```csh
   fsck -y /dev/sda1
   ```

## Tips
- Zorg ervoor dat het bestandssysteem niet in gebruik is voordat je `fsck` uitvoert, om gegevensverlies te voorkomen.
- Maak altijd een back-up van belangrijke gegevens voordat je reparaties uitvoert.
- Gebruik `fsck` regelmatig om de gezondheid van je bestandssystemen te waarborgen.