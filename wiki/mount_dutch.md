# [Linux] C Shell (csh) mount gebruik: Schijfpartities koppelen

## Overzicht
De `mount`-opdracht in C Shell (csh) wordt gebruikt om bestandssystemen te koppelen aan een bepaalde locatie in de directorystructuur. Dit stelt gebruikers in staat om toegang te krijgen tot bestanden op verschillende schijven of partities.

## Gebruik
De basis syntaxis van de `mount`-opdracht is als volgt:

```csh
mount [options] [arguments]
```

## Veelvoorkomende opties
- `-t type` : Specificeert het type bestandssysteem dat moet worden gemount (bijv. ext4, ntfs).
- `-o options` : Geeft extra opties op, zoals `ro` voor alleen-lezen of `rw` voor lezen en schrijven.
- `-a` : Mount alle bestandssystemen die zijn opgegeven in de `/etc/fstab`-configuratie.
- `-r` : Mount het bestandssysteem als alleen-lezen.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `mount`-opdracht:

1. Een ext4-bestandssysteem mounten:
   ```csh
   mount -t ext4 /dev/sda1 /mnt
   ```

2. Een NTFS-bestandssysteem mounten met alleen-lezen toegang:
   ```csh
   mount -t ntfs -o ro /dev/sdb1 /mnt/usb
   ```

3. Alle bestandssystemen mounten die zijn gedefinieerd in `/etc/fstab`:
   ```csh
   mount -a
   ```

4. Een bestandssysteem mounten met lees- en schrijfrechten:
   ```csh
   mount -o rw /dev/sdc1 /mnt/data
   ```

## Tips
- Zorg ervoor dat je de juiste rechten hebt om een bestandssysteem te mounten; vaak zijn root-rechten vereist.
- Controleer altijd of de schijf of partitie correct is ontkoppeld met de `umount`-opdracht voordat je deze fysiek verwijdert.
- Gebruik de `df -h`-opdracht om te controleren welke bestandssystemen momenteel zijn gemount en hun gebruik.