# [Linux] C Shell (csh) lvextend gebruik: Vergroot logische volumes

## Overzicht
De `lvextend` opdracht wordt gebruikt om de grootte van een logisch volume in een Logical Volume Manager (LVM) configuratie te vergroten. Dit is nuttig wanneer je meer schijfruimte nodig hebt voor een bestaand volume.

## Gebruik
De basis syntaxis van de `lvextend` opdracht is als volgt:

```csh
lvextend [opties] [argumenten]
```

## Veelvoorkomende opties
- `-L +<size>`: Verhoog de grootte van het volume met een specifieke hoeveelheid.
- `-L <size>`: Stel de nieuwe totale grootte van het volume in.
- `-r`: Vergroot het bestandssysteem automatisch samen met het volume.
- `-n`: Geef de naam van het logische volume op.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `lvextend`:

1. Vergroot een logisch volume met 10 GB:
   ```csh
   lvextend -L +10G /dev/vg1/lv1
   ```

2. Stel de totale grootte van een logisch volume in op 50 GB:
   ```csh
   lvextend -L 50G /dev/vg1/lv1
   ```

3. Vergroot een logisch volume en het bestandssysteem automatisch:
   ```csh
   lvextend -r -L +5G /dev/vg1/lv1
   ```

4. Vergroot een logisch volume met een specifieke naam:
   ```csh
   lvextend -L +20G /dev/vg1/lv2
   ```

## Tips
- Zorg ervoor dat je voldoende vrije ruimte hebt in de volume group voordat je een logisch volume vergroot.
- Gebruik de `-r` optie om het bestandssysteem automatisch aan te passen, dit bespaart tijd en voorkomt fouten.
- Controleer altijd de status van je volumes na het uitvoeren van de `lvextend` opdracht met `lvdisplay` of `df -h` om te bevestigen dat de wijzigingen zijn doorgevoerd.