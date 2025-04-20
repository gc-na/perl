# [Linux] C Shell (csh) tr <Gebruik: Tekens omzetten>

## Overzicht
De `tr` (translate) opdracht in C Shell wordt gebruikt om tekens in tekstbestanden te vervangen of te verwijderen. Het is een handige tool voor tekstmanipulatie, vooral bij het verwerken van gegevens in scripts.

## Gebruik
De basis syntaxis van de `tr` opdracht is als volgt:

```csh
tr [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-d`: Verwijdert de opgegeven tekens.
- `-s`: Vervangt opeenvolgende herhalingen van een teken door één exemplaar.
- `-c`: Neemt de complementaire set van de opgegeven tekens.

## Veelvoorkomende Voorbeelden

1. **Vervangen van tekens**
   Vervang alle kleine letters door hoofdletters in een tekstbestand.
   ```csh
   cat bestand.txt | tr 'a-z' 'A-Z'
   ```

2. **Verwijderen van specifieke tekens**
   Verwijder alle cijfers uit een tekst.
   ```csh
   echo "Hallo123 Wereld456" | tr -d '0-9'
   ```

3. **Samenvatten van spaties**
   Vervang meerdere spaties door één enkele spatie.
   ```csh
   echo "Dit    is    een    test." | tr -s ' '
   ```

4. **Complementaire set gebruiken**
   Vervang alle niet-alfabetische tekens door een spatie.
   ```csh
   echo "Hallo! Dit is een test." | tr -c 'a-zA-Z' ' '
   ```

## Tips
- Gebruik `cat` in combinatie met `tr` om bestanden te verwerken zonder ze direct te wijzigen.
- Test je `tr` opdrachten met `echo` voordat je ze op bestanden toepast om onbedoelde wijzigingen te voorkomen.
- Combineer `tr` met andere commando's zoals `grep` of `awk` voor geavanceerdere tekstverwerking.