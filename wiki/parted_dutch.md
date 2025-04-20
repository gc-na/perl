# [Linux] C Shell (csh) parted gebruik: Schijfpartitionering en -beheer

## Overzicht
Het `parted` commando is een krachtige tool voor het beheren van schijfpartities. Het stelt gebruikers in staat om partities te maken, te verwijderen, te vergroten of te verkleinen, en biedt ondersteuning voor verschillende bestandssystemen.

## Gebruik
De basis syntaxis van het `parted` commando is als volgt:
```
parted [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-l` : Lijst alle schijven en hun partities.
- `mkpart` : Maak een nieuwe partitie aan.
- `rm` : Verwijder een bestaande partitie.
- `resizepart` : Wijzig de grootte van een bestaande partitie.
- `print` : Toon de partitie-informatie van de geselecteerde schijf.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `parted`:

1. **Lijst alle schijven en hun partities:**
   ```bash
   parted -l
   ```

2. **Maak een nieuwe partitie aan:**
   ```bash
   parted /dev/sda mkpart primary ext4 1MiB 100MiB
   ```

3. **Verwijder een bestaande partitie:**
   ```bash
   parted /dev/sda rm 1
   ```

4. **Wijzig de grootte van een bestaande partitie:**
   ```bash
   parted /dev/sda resizepart 1 200MiB
   ```

5. **Toon de partitie-informatie van de geselecteerde schijf:**
   ```bash
   parted /dev/sda print
   ```

## Tips
- Zorg ervoor dat je een back-up maakt van belangrijke gegevens voordat je wijzigingen aanbrengt aan partities.
- Gebruik `parted` met voorzichtigheid, aangezien onjuiste commando's gegevensverlies kunnen veroorzaken.
- Controleer altijd de huidige partitie-indeling met `print` voordat je wijzigingen aanbrengt.