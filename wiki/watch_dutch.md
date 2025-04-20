# [Linux] C Shell (csh) watch gebruik: Voortdurend een commando uitvoeren

## Overzicht
De `watch`-opdracht in C Shell (csh) wordt gebruikt om een bepaald commando op regelmatige tijdstippen uit te voeren en de uitvoer in de terminal bij te werken. Dit is handig voor het monitoren van veranderingen in de uitvoer van een commando, zoals systeemprestaties of bestandssystemen.

## Gebruik
De basis syntaxis van de `watch`-opdracht is als volgt:

```csh
watch [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-n <seconden>`: Bepaalt de intervaltijd in seconden tussen de uitvoeringen van het commando.
- `-d`: Markeer de verschillen tussen de huidige en de vorige uitvoer.
- `-t`: Schakel de titelbalk van de terminal uit.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `watch`-opdracht:

1. **Monitoren van systeembelasting elke 2 seconden**:
   ```csh
   watch -n 2 uptime
   ```

2. **De inhoud van een directory elke 5 seconden bekijken**:
   ```csh
   watch -n 5 ls -l /pad/naar/directory
   ```

3. **Controleer het gebruik van schijfruimte met verschillen gemarkeerd**:
   ```csh
   watch -d df -h
   ```

4. **Een proces volgen zonder titelbalk**:
   ```csh
   watch -t ps aux | grep naam_van_proces
   ```

## Tips
- Gebruik de `-d` optie om snel veranderingen te identificeren in de uitvoer, vooral nuttig bij het monitoren van dynamische gegevens.
- Pas de intervaltijd aan met `-n` om de belasting op het systeem te minimaliseren, vooral bij intensieve commando's.
- Combineer `watch` met andere commando's zoals `grep` of `awk` voor gerichte monitoring van specifieke informatie.