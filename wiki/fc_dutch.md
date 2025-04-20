# [Linux] C Shell (csh) fc gebruik: Geschiedenis van commando's bewerken

## Overzicht
Het `fc`-commando in C Shell (csh) wordt gebruikt om de geschiedenis van eerder ingevoerde commando's te bewerken en opnieuw uit te voeren. Het stelt gebruikers in staat om hun commando's te bekijken, te wijzigen en opnieuw uit te voeren zonder ze opnieuw te typen.

## Gebruik
De basis syntaxis van het `fc`-commando is als volgt:

```csh
fc [opties] [argumenten]
```

## Veelvoorkomende opties
- `-l`: Lijst de geschiedenis van commando's.
- `-r`: Beweeg de lijst van commando's in omgekeerde volgorde.
- `-n`: Toon de commando's zonder nummering.
- `-e`: Specificeer een editor om de commando's te bewerken.

## Veelvoorkomende voorbeelden

1. **Lijst de laatste 10 commando's:**
   ```csh
   fc -l -10
   ```

2. **Bewerk het laatste commando met de standaard editor:**
   ```csh
   fc
   ```

3. **Bewerk een specifiek commando uit de geschiedenis (bijvoorbeeld nummer 5):**
   ```csh
   fc 5
   ```

4. **Lijst de geschiedenis in omgekeerde volgorde:**
   ```csh
   fc -r -l
   ```

5. **Bewerk de laatste commando's met een specifieke editor (bijv. vi):**
   ```csh
   fc -e vi
   ```

## Tips
- Gebruik `fc` regelmatig om typfouten in eerdere commando's snel te corrigeren.
- Combineer `fc` met andere shell-commando's om efficiënter te werken.
- Vergeet niet dat de geschiedenis beperkt is; oudere commando's kunnen niet altijd worden teruggevonden, afhankelijk van de configuratie van de shell.