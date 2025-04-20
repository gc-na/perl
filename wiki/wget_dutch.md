# [Linux] C Shell (csh) wget gebruik: Bestanden downloaden van het web

## Overzicht
De `wget`-opdracht is een krachtige tool voor het downloaden van bestanden van het internet. Het ondersteunt verschillende protocollen zoals HTTP, HTTPS en FTP, en kan worden gebruikt om bestanden te downloaden, websites te mirroren en meer.

## Gebruik
De basisstructuur van de `wget`-opdracht is als volgt:

```
wget [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-O <bestandsnaam>`: Specificeert de naam van het bestand waarin de gedownloade inhoud moet worden opgeslagen.
- `-c`: Hervat een onderbroken download.
- `-r`: Download bestanden recursief, wat handig is voor het mirroren van websites.
- `--limit-rate=<snelheid>`: Beperk de downloadsnelheid tot een bepaalde waarde.
- `-q`: Voer de opdracht uit in stille modus, zonder uitvoer naar de terminal.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `wget`:

1. **Een enkel bestand downloaden:**
   ```csh
   wget https://example.com/bestand.zip
   ```

2. **Een bestand downloaden met een specifieke naam:**
   ```csh
   wget -O nieuwe_naam.zip https://example.com/bestand.zip
   ```

3. **Een download hervatten:**
   ```csh
   wget -c https://example.com/bestand.zip
   ```

4. **Een hele website mirroren:**
   ```csh
   wget -r https://example.com
   ```

5. **De downloadsnelheid beperken:**
   ```csh
   wget --limit-rate=200k https://example.com/bestand.zip
   ```

## Tips
- Gebruik de `-q` optie als je niet wilt dat de terminal volloopt met uitvoer, vooral bij grote downloads.
- Combineer de `-c` optie met `-r` als je een grote website wilt mirroren en je wilt dat de download kan worden hervat.
- Controleer altijd de URL voordat je een download start om te zorgen dat je het juiste bestand downloadt.