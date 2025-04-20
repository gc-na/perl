# [Linux] C Shell (csh) pidstat gebruik: Monitoren van processtatistieken

## Overzicht
De `pidstat`-opdracht is een hulpmiddel dat wordt gebruikt om statistieken van actieve processen in een Linux-systeem te monitoren. Het biedt gedetailleerde informatie over CPU-gebruik, geheugenverbruik en andere belangrijke prestatie-indicatoren van processen.

## Gebruik
De basis syntaxis van de `pidstat`-opdracht is als volgt:

```bash
pidstat [opties] [argumenten]
```

## Veelvoorkomende opties
- `-h`: Toon de koptekst in een leesbaar formaat.
- `-r`: Toon geheugenstatistieken.
- `-u`: Toon CPU-gebruik per proces.
- `-p <PID>`: Specificeer een specifieke proces-ID om te monitoren.
- `-t`: Toon de statistieken voor alle threads van een proces.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `pidstat`:

1. **Basis CPU-gebruik weergeven:**
   ```bash
   pidstat
   ```

2. **CPU-gebruik voor een specifieke proces-ID (bijvoorbeeld PID 1234):**
   ```bash
   pidstat -p 1234
   ```

3. **Geheugenstatistieken weergeven:**
   ```bash
   pidstat -r
   ```

4. **Statistieken voor alle processen en hun threads weergeven:**
   ```bash
   pidstat -t
   ```

5. **Statistieken elke 2 seconden bijwerken:**
   ```bash
   pidstat 2
   ```

## Tips
- Gebruik de `-h` optie om de uitvoer beter leesbaar te maken, vooral als je met veel processen werkt.
- Combineer opties zoals `-u` en `-r` om zowel CPU- als geheugenstatistieken in één uitvoer te zien.
- Overweeg om `pidstat` te gebruiken in combinatie met andere monitoringtools voor een uitgebreidere analyse van systeembronnen.