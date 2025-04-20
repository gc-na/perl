# [Linux] C Shell (csh) last commando: Toont inloggeschiedenis

## Overzicht
Het `last` commando in C Shell (csh) toont een lijst van gebruikers die zich hebben aangemeld op het systeem, samen met de tijd en datum van hun inlog- en uitlogmomenten. Dit is nuttig voor het controleren van systeemactiviteit en het identificeren van ongebruikelijke inlogpogingen.

## Gebruik
De basis syntaxis van het `last` commando is als volgt:

```
last [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-n`: Beperk het aantal weergegeven inlogrecords tot `n`.
- `-R`: Schakel de weergave van de hostname uit.
- `-f`: Geef een specifieke wtmp-bestand op in plaats van het standaard wtmp-bestand.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van het `last` commando:

1. **Toon de laatste inlogrecords:**
   ```csh
   last
   ```

2. **Beperk de weergave tot de laatste 10 inlogrecords:**
   ```csh
   last -n 10
   ```

3. **Toon inlogrecords zonder hostnamen:**
   ```csh
   last -R
   ```

4. **Toon inlogrecords uit een specifiek wtmp-bestand:**
   ```csh
   last -f /var/log/wtmp.1
   ```

## Tips
- Gebruik `last -n` om snel een overzicht te krijgen van recente inlogactiviteit zonder te veel informatie te tonen.
- Controleer regelmatig de inloggeschiedenis om verdachte activiteiten te identificeren.
- Combineer `last` met andere commando's zoals `grep` om specifieke gebruikers of tijdstippen te filteren.