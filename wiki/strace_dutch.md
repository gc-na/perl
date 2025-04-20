# [Linux] C Shell (csh) strace gebruik: systeemaanroep trace

## Overzicht
De `strace`-opdracht is een krachtig hulpmiddel dat wordt gebruikt om systeemaanroepen en signalen van een proces te traceren. Het biedt inzicht in hoe een programma met het besturingssysteem communiceert, wat nuttig kan zijn voor foutopsporing en prestatie-analyse.

## Gebruik
De basis syntaxis van de `strace`-opdracht is als volgt:

```csh
strace [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-c`: Geeft een samenvatting van systeemaanroepen en hun statistieken.
- `-e trace=<type>`: Traceert alleen specifieke systeemaanroepen, zoals `file`, `network`, etc.
- `-p <pid>`: Voegt zich bij een bestaand proces met het opgegeven proces-ID.
- `-o <bestand>`: Schrijft de uitvoer naar het opgegeven bestand in plaats van naar de standaarduitvoer.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `strace`:

1. **Basisgebruik van strace**:
   ```csh
   strace ls
   ```
   Dit commando traceert de systeemaanroepen die door het `ls`-commando worden gedaan.

2. **Traceer specifieke systeemaanroepen**:
   ```csh
   strace -e trace=open,close ls
   ```
   Dit commando traceert alleen de `open` en `close` systeemaanroepen die door `ls` worden uitgevoerd.

3. **Statistieken van systeemaanroepen weergeven**:
   ```csh
   strace -c ls
   ```
   Dit geeft een samenvatting van de systeemaanroepen die door `ls` zijn uitgevoerd, inclusief het aantal en de tijd die aan elke aanroep is besteed.

4. **Voeg je bij een bestaand proces**:
   ```csh
   strace -p 1234
   ```
   Dit voegt zich bij het proces met PID 1234 en begint met het traceren van de systeemaanroepen.

5. **Schrijf uitvoer naar een bestand**:
   ```csh
   strace -o output.txt ls
   ```
   Dit schrijft de uitvoer van de `strace`-opdracht naar `output.txt` in plaats van naar de terminal.

## Tips
- Gebruik `strace` met de `-c` optie voor een snelle statistische samenvatting van systeemaanroepen, vooral handig bij het analyseren van prestatieproblemen.
- Wees voorzichtig bij het traceren van processen met veel systeemaanroepen, omdat de uitvoer snel overweldigend kan worden.
- Combineer `strace` met andere tools zoals `grep` om specifieke systeemaanroepen of foutmeldingen te filteren.