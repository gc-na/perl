# [Linux] C Shell (csh) sha512sum gebruik: Controleer de integriteit van bestanden

## Overzicht
De `sha512sum` opdracht wordt gebruikt om de SHA-512 hashwaarde van bestanden te berekenen. Dit is nuttig voor het verifiëren van de integriteit van bestanden en het detecteren van wijzigingen.

## Gebruik
De basis syntaxis van de `sha512sum` opdracht is als volgt:

```csh
sha512sum [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-b`: Behandelt de invoer als binaire bestanden.
- `-c`: Controleert de hashwaarden van bestanden op basis van een opgegeven controlebestand.
- `-h`: Toont een helpbericht met informatie over de opties.

## Veelvoorkomende Voorbeelden

1. **Bereken de SHA-512 hash van een bestand:**
   ```csh
   sha512sum voorbeeld.txt
   ```

2. **Sla de hashwaarde op in een bestand:**
   ```csh
   sha512sum voorbeeld.txt > hash.txt
   ```

3. **Controleer de hashwaarden van bestanden met een controlebestand:**
   ```csh
   sha512sum -c hash.txt
   ```

4. **Bereken de hash van meerdere bestanden:**
   ```csh
   sha512sum bestand1.txt bestand2.txt
   ```

## Tips
- Gebruik de optie `-c` om snel te controleren of bestanden zijn gewijzigd door hun hashwaarden te vergelijken met eerder opgeslagen waarden.
- Het is een goede gewoonte om hashwaarden op te slaan na het downloaden van bestanden om later de integriteit te kunnen verifiëren.
- Voor binaire bestanden is het raadzaam om de `-b` optie te gebruiken om correcte resultaten te garanderen.