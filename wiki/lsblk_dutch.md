# [Linux] C Shell (csh) lsblk gebruik: Toont blokapparaten en hun eigenschappen

## Overzicht
De `lsblk` opdracht in C Shell (csh) wordt gebruikt om informatie weer te geven over blokapparaten op een systeem. Dit omvat harde schijven, SSD's en andere opslagmedia, samen met hun partities en eigenschappen.

## Gebruik
De basis syntaxis van de `lsblk` opdracht is als volgt:

```csh
lsblk [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-a` : Toont ook lege apparaten.
- `-f` : Toont informatie over bestandssystemen.
- `-l` : Toont de uitvoer in een lijstvorm.
- `-o` : Specificeert welke kolommen moeten worden weergegeven.
- `-p` : Toont de volledige padnamen van de apparaten.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `lsblk`:

1. **Basisinformatie over blokapparaten weergeven:**
   ```csh
   lsblk
   ```

2. **Informatie over bestandssystemen tonen:**
   ```csh
   lsblk -f
   ```

3. **Weergave in lijstvorm:**
   ```csh
   lsblk -l
   ```

4. **Specifieke kolommen weergeven (bijv. naam, grootte en type):**
   ```csh
   lsblk -o NAME,SIZE,TYPE
   ```

5. **Lege apparaten ook tonen:**
   ```csh
   lsblk -a
   ```

## Tips
- Gebruik de `-f` optie om snel te controleren welk bestandssysteem op elk apparaat is geïnstalleerd.
- Combineer opties voor meer gedetailleerde uitvoer, zoals `lsblk -fa`.
- Controleer regelmatig de status van je opslagapparaten, vooral voor systeemonderhoud en troubleshooting.