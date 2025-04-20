# [Linux] C Shell (csh) stat gebruik: Toont bestandseigenschappen

## Overzicht
De `stat` opdracht in C Shell (csh) wordt gebruikt om gedetailleerde informatie over bestanden en directories weer te geven. Het biedt gegevens zoals bestandsgrootte, aanmaakdatum, wijzigingsdatum en bestandspermissies.

## Gebruik
De basis syntaxis van de `stat` opdracht is als volgt:

```csh
stat [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-c` : Specificeer een aangepaste outputformat.
- `-f` : Toon alleen de informatie voor het opgegeven bestand.
- `-L` : Volg symbolische links om informatie over het doelbestand te tonen.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `stat` opdracht:

1. **Basis informatie over een bestand weergeven:**
   ```csh
   stat mijnbestand.txt
   ```

2. **Specifieke informatie opvragen met aangepaste output:**
   ```csh
   stat -c '%n: %s bytes, %y' mijnbestand.txt
   ```

3. **Informatie over een directory tonen:**
   ```csh
   stat mijnmap/
   ```

4. **Informatie over een symbolische link volgen:**
   ```csh
   stat -L mijnlink
   ```

## Tips
- Gebruik de `-c` optie om de output aan te passen aan jouw behoeften, wat handig kan zijn voor scripting.
- Controleer altijd de bestandspermissies met de `stat` opdracht om ervoor te zorgen dat je de juiste toegang hebt.
- Combineer `stat` met andere commando's zoals `grep` om specifieke informatie te filteren.