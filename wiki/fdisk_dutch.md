# [Linux] C Shell (csh) fdisk gebruik: Schijfpartities beheren

## Overzicht
Het `fdisk`-commando is een krachtig hulpmiddel dat wordt gebruikt voor het beheren van schijfpartities op Linux-systemen. Met `fdisk` kunt u partities aanmaken, verwijderen en wijzigen, evenals informatie over de schijf en de partities bekijken.

## Gebruik
De basis syntaxis van het `fdisk`-commando is als volgt:

```bash
fdisk [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-l`: Lijst alle beschikbare schijven en hun partities.
- `-u`: Gebruik sectoren in plaats van cilinders voor de weergave van partitie-informatie.
- `-s`: Toon de grootte van een specifieke partitie.
- `-n`: Maak een nieuwe partitie aan.
- `-d`: Verwijder een bestaande partitie.

## Veelvoorkomende Voorbeelden

1. **Lijst alle schijven en hun partities**:
   ```bash
   fdisk -l
   ```

2. **Nieuwe partitie aanmaken**:
   ```bash
   fdisk /dev/sda
   ```
   Volg de instructies in de interactieve prompt om een nieuwe partitie aan te maken.

3. **Verwijder een partitie**:
   ```bash
   fdisk /dev/sda
   ```
   Gebruik de optie `d` in de interactieve prompt om een partitie te verwijderen.

4. **Bekijk de grootte van een specifieke partitie**:
   ```bash
   fdisk -s /dev/sda1
   ```

## Tips
- Maak altijd een back-up van uw gegevens voordat u wijzigingen aanbrengt in partities.
- Gebruik `man fdisk` om de handleiding te bekijken voor meer gedetailleerde informatie over het gebruik van het commando.
- Wees voorzichtig met het verwijderen van partities, aangezien dit kan leiden tot gegevensverlies.