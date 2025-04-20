# [Linux] C Shell (csh) sha256sum gebruik: Controleer de integriteit van bestanden

## Overzicht
De `sha256sum` opdracht wordt gebruikt om de SHA-256 hashwaarde van bestanden te berekenen. Dit is nuttig voor het verifiëren van de integriteit van bestanden, bijvoorbeeld na het downloaden of overdragen van bestanden.

## Gebruik
De basis syntaxis van de `sha256sum` opdracht is als volgt:

```
sha256sum [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-b`: Behandel de invoer als binaire bestanden.
- `-c`: Controleer de hashwaarden van bestanden die zijn opgeslagen in een bestand.
- `-h`: Toon een helpbericht met informatie over het gebruik van de opdracht.
- `--quiet`: Vermijd het tonen van de hashwaarden bij het controleren.

## Veelvoorkomende Voorbeelden

1. **Bereken de SHA-256 hash van een bestand:**
   ```csh
   sha256sum bestand.txt
   ```

2. **Sla de hashwaarde op in een bestand:**
   ```csh
   sha256sum bestand.txt > hash.txt
   ```

3. **Controleer de hashwaarden van bestanden met een hashbestand:**
   ```csh
   sha256sum -c hash.txt
   ```

4. **Bereken de hash van meerdere bestanden:**
   ```csh
   sha256sum bestand1.txt bestand2.txt
   ```

## Tips
- Zorg ervoor dat je de hashwaarden opslaat na het berekenen, zodat je deze later kunt gebruiken voor verificatie.
- Gebruik de `-c` optie om eenvoudig te controleren of bestanden zijn gewijzigd door hun hashwaarden te vergelijken met een eerder opgeslagen bestand.
- Het is een goede gewoonte om hashwaarden te controleren na het downloaden van belangrijke bestanden, vooral van onbekende bronnen.