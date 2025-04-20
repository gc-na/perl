# [Linux] C Shell (csh) stty gebruik: Instellen van terminaleigenschappen

## Overview
Het `stty`-commando wordt gebruikt om de terminalinstellingen te configureren en te beheren. Hiermee kun je verschillende eigenschappen van de terminal aanpassen, zoals het instellen van speciale toetsen, het wijzigen van de invoer- en uitvoermodi, en het beheren van de flow control.

## Usage
De basis syntaxis van het `stty`-commando is als volgt:

```csh
stty [opties] [argumenten]
```

## Common Options
Hier zijn enkele veelvoorkomende opties voor `stty`:

- `-a`: Toont alle huidige terminalinstellingen.
- `-g`: Geeft de huidige instellingen weer in een formaat dat kan worden opgeslagen en later kan worden hersteld.
- `erase`: Stelt het teken in dat gebruikt wordt om een teken te wissen.
- `kill`: Stelt het teken in dat gebruikt wordt om een regel te wissen.
- `intr`: Stelt het teken in dat gebruikt wordt om een onderbreking te genereren.

## Common Examples
Hier zijn enkele praktische voorbeelden van het gebruik van `stty`:

1. **Toon alle terminalinstellingen**:
   ```csh
   stty -a
   ```

2. **Stel het wis-teken in op Backspace**:
   ```csh
   stty erase ^H
   ```

3. **Stel het onderbrekings-teken in op Ctrl+C**:
   ```csh
   stty intr ^C
   ```

4. **Herstel de terminalinstellingen naar een eerder opgeslagen configuratie**:
   ```csh
   stty $(stty -g)
   ```

## Tips
- Gebruik `stty -a` om een overzicht te krijgen van alle huidige instellingen voordat je wijzigingen aanbrengt.
- Wees voorzichtig met het instellen van speciale toetsen, omdat dit de normale werking van de terminal kan beïnvloeden.
- Sla je terminalinstellingen op met `stty -g` voordat je wijzigingen aanbrengt, zodat je ze later kunt herstellen indien nodig.