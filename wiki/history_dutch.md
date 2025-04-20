# [Linux] C Shell (csh) geschiedenis gebruik: Beheer je opdrachtgeschiedenis

## Overzicht
De `history`-opdracht in de C Shell (csh) toont een lijst van eerder uitgevoerde opdrachten. Dit is handig voor gebruikers die snel eerdere commando's willen terugvinden of herhalen zonder ze opnieuw te typen.

## Gebruik
De basis syntaxis van de `history`-opdracht is als volgt:

```csh
history [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-c`: Wis de huidige geschiedenis.
- `n`: Geef de laatste n opdrachten weer.
- `-h`: Toon een korte helptekst over het gebruik van de geschiedenisopdracht.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `history`-opdracht:

1. **Toon de volledige geschiedenis**:
   ```csh
   history
   ```

2. **Toon de laatste 10 opdrachten**:
   ```csh
   history 10
   ```

3. **Wis de geschiedenis**:
   ```csh
   history -c
   ```

4. **Herhaal een specifieke opdracht**:
   ```csh
   !123
   ```
   (waarbij `123` het nummer van de opdracht in de geschiedenis is).

## Tips
- Gebruik de `history`-opdracht regelmatig om je workflow te versnellen door eerder gebruikte commando's snel te herhalen.
- Combineer de `history`-opdracht met andere shell-functies, zoals pijpen en omleiden, voor geavanceerdere taken.
- Vergeet niet je geschiedenis regelmatig op te schonen om onnodige commando's te verwijderen en de lijst overzichtelijk te houden.