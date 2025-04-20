# [Linux] C Shell (csh) tar Gebruik: Archiveren en comprimeren van bestanden

## Overzicht
De `tar`-opdracht, wat staat voor "tape archive", wordt gebruikt om meerdere bestanden en mappen samen te voegen in één archiefbestand. Dit is handig voor back-ups en het delen van bestanden. Het kan ook bestanden comprimeren om opslagruimte te besparen.

## Gebruik
De basis syntaxis van de `tar`-opdracht is als volgt:

```bash
tar [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-c`: Maak een nieuw archief.
- `-x`: Extraheer bestanden uit een archief.
- `-f`: Specificeer de naam van het archiefbestand.
- `-v`: Toon de voortgang van de bewerking (verbose).
- `-z`: Comprimeer of decomprimeer met gzip.
- `-j`: Comprimeer of decomprimeer met bzip2.

## Veelvoorkomende Voorbeelden

1. **Een archief maken:**
   ```bash
   tar -cvf archief.tar /pad/naar/mappen
   ```

2. **Een archief maken met compressie:**
   ```bash
   tar -czvf archief.tar.gz /pad/naar/mappen
   ```

3. **Bestanden extraheren uit een archief:**
   ```bash
   tar -xvf archief.tar
   ```

4. **Bestanden extraheren uit een gecomprimeerd archief:**
   ```bash
   tar -xzvf archief.tar.gz
   ```

5. **Lijst van bestanden in een archief bekijken:**
   ```bash
   tar -tvf archief.tar
   ```

## Tips
- Gebruik de `-v` optie om te zien welke bestanden worden verwerkt, vooral bij grote archieven.
- Vergeet niet om de juiste compressie-optie (`-z` of `-j`) te gebruiken afhankelijk van het type archief dat je maakt.
- Controleer altijd de inhoud van een archief met de `-t` optie voordat je bestanden extraheert, om te bevestigen dat je de juiste bestanden hebt.