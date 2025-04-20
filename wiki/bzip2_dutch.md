# [Linux] C Shell (csh) bzip2 Gebruik: Bestanden comprimeren en decomprimeren

## Overzicht
De `bzip2` opdracht wordt gebruikt om bestanden te comprimeren en te decomprimeren. Het maakt gebruik van de Burrows-Wheeler-algoritme om bestanden efficiënter te verkleinen dan andere compressieprogramma's.

## Gebruik
De basis syntaxis van de `bzip2` opdracht is als volgt:

```csh
bzip2 [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-d` : Decomprimeert een bestand.
- `-k` : Houdt het originele bestand intact na compressie.
- `-f` : Dwingt compressie, zelfs als het doelbestand al bestaat.
- `-v` : Toont gedetailleerde informatie over het compressieproces.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `bzip2`:

1. **Een bestand comprimeren:**
   ```csh
   bzip2 bestand.txt
   ```
   Dit zal `bestand.txt` comprimeren naar `bestand.txt.bz2`.

2. **Een bestand decomprimeren:**
   ```csh
   bzip2 -d bestand.txt.bz2
   ```
   Dit zal `bestand.txt.bz2` decomprimeren naar `bestand.txt`.

3. **Een bestand comprimeren en het origineel behouden:**
   ```csh
   bzip2 -k bestand.txt
   ```
   Dit zal `bestand.txt` comprimeren naar `bestand.txt.bz2`, terwijl `bestand.txt` behouden blijft.

4. **Dwingen om een bestaand bestand te overschrijven:**
   ```csh
   bzip2 -f bestand.txt
   ```
   Dit zal `bestand.txt` comprimeren en een bestaande `bestand.txt.bz2` overschrijven.

5. **Gedetailleerde informatie tijdens compressie tonen:**
   ```csh
   bzip2 -v bestand.txt
   ```
   Dit toont informatie over het compressieproces terwijl het bestand wordt gecomprimeerd.

## Tips
- Gebruik de `-k` optie als je het originele bestand wilt behouden voor toekomstig gebruik.
- Controleer altijd de bestandsgrootte na compressie om te zien of de compressie succesvol was.
- Voor het decompressieproces, vergeet niet de `-d` optie te gebruiken, anders zal `bzip2` proberen het bestand opnieuw te comprimeren.