# [Linux] C Shell (csh) nohup gebruik: Voorkom dat een proces wordt beëindigd bij uitloggen

## Overzicht
De `nohup` (no hang up) opdracht in C Shell wordt gebruikt om een proces te starten dat niet wordt beëindigd wanneer de gebruiker uitlogt of de terminal sluit. Dit is bijzonder nuttig voor lange-running processen die je wilt laten doorgaan, zelfs als je niet meer bent ingelogd.

## Gebruik
De basis syntaxis van de `nohup` opdracht is als volgt:

```csh
nohup [opties] [argumenten]
```

## Veelvoorkomende Opties
- `&` : Voegt het proces toe aan de achtergrond, zodat je de terminal kunt blijven gebruiken.
- `-o [bestand]` : Standaard uitvoer wordt naar het opgegeven bestand geschreven.
- `-e [bestand]` : Standaard foutuitvoer wordt naar het opgegeven bestand geschreven.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `nohup`:

1. Een eenvoudig proces uitvoeren in de achtergrond:
   ```csh
   nohup myscript.sh &
   ```

2. De uitvoer van een script naar een bestand sturen:
   ```csh
   nohup myscript.sh > output.log &
   ```

3. Zowel de uitvoer als de foutuitvoer naar aparte bestanden sturen:
   ```csh
   nohup myscript.sh > output.log 2> error.log &
   ```

4. Een Python-script uitvoeren dat lange tijd kan duren:
   ```csh
   nohup python long_running_script.py &
   ```

## Tips
- Gebruik `jobs` om te controleren welke achtergrondprocessen actief zijn.
- Vergeet niet om de uitvoerbestanden regelmatig te controleren om te zien hoe je processen vorderen.
- Combineer `nohup` met `screen` of `tmux` voor nog meer controle over je processen, vooral als je meerdere sessies wilt beheren.