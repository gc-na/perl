# [Linux] C Shell (csh) ls gebruik: Lijst bestanden en mappen

## Overzicht
De `ls`-opdracht in C Shell (csh) wordt gebruikt om de inhoud van een directory weer te geven. Het toont bestanden en submappen, waardoor gebruikers snel kunnen zien welke bestanden beschikbaar zijn in een bepaalde map.

## Gebruik
De basis syntaxis van de `ls`-opdracht is als volgt:

```
ls [opties] [argumenten]
```

## Veelvoorkomende Opties
Hier zijn enkele veelvoorkomende opties die je kunt gebruiken met de `ls`-opdracht:

- `-l`: Toont een gedetailleerde lijst van bestanden met informatie zoals permissies, eigenaar, grootte en datum.
- `-a`: Toont alle bestanden, inclusief verborgen bestanden (die beginnen met een punt).
- `-h`: Toont bestandsgroottes in een leesbaar formaat (bijv. KB, MB).
- `-R`: Toont de inhoud van submappen recursief.
- `-t`: Sorteert bestanden op tijd van laatste wijziging.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `ls`-opdracht:

1. **Basis gebruik:**
   ```csh
   ls
   ```

2. **Lijst met gedetailleerde informatie:**
   ```csh
   ls -l
   ```

3. **Inclusief verborgen bestanden:**
   ```csh
   ls -a
   ```

4. **Lijst met leesbare bestandsgroottes:**
   ```csh
   ls -lh
   ```

5. **Recursief door submappen:**
   ```csh
   ls -R
   ```

6. **Bestanden gesorteerd op tijd:**
   ```csh
   ls -lt
   ```

## Tips
- Gebruik `ls -la` om een volledig overzicht van alle bestanden, inclusief verborgen bestanden, te krijgen.
- Combineer opties voor meer gedetailleerde informatie, bijvoorbeeld `ls -lhR` voor een leesbare, recursieve lijst.
- Maak gebruik van alias in je `.cshrc` bestand om vaak gebruikte opties te vereenvoudigen, zoals `alias ll 'ls -l'`.