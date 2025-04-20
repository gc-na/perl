# [Linux] C Shell (csh) vgs Gebruik: Toon informatie over volume groepen

## Overzicht
Het `vgs` commando wordt gebruikt om informatie weer te geven over volume groepen in een Logical Volume Management (LVM) systeem. Het biedt een overzicht van de beschikbare volume groepen, inclusief details zoals de grootte en het aantal logische volumes.

## Gebruik
De basis syntaxis van het `vgs` commando is als volgt:

```
vgs [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-o`: Specificeer welke velden moeten worden weergegeven.
- `--units`: Geef de eenheden aan voor de uitvoer.
- `-h`: Toon de uitvoer in een meer leesbaar formaat (human-readable).

## Veelvoorkomende Voorbeelden

1. **Basis informatie over volume groepen**
   ```csh
   vgs
   ```

2. **Specifieke velden weergeven**
   ```csh
   vgs -o vg_name,lv_count,vg_size
   ```

3. **Uitvoer in menselijk leesbare eenheden**
   ```csh
   vgs -h
   ```

4. **Uitvoer met specifieke eenheden**
   ```csh
   vgs --units g
   ```

## Tips
- Gebruik de `-o` optie om alleen de informatie weer te geven die je nodig hebt, wat de uitvoer overzichtelijker maakt.
- Combineer `vgs` met andere LVM commando's zoals `lvdisplay` voor een completer beeld van je opslagconfiguratie.
- Controleer regelmatig de status van je volume groepen om ervoor te zorgen dat er voldoende ruimte beschikbaar is voor toekomstige uitbreidingen.