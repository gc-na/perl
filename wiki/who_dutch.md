# [Unix] C Shell (csh) who gebruik: Toon ingelogde gebruikers

## Overzicht
De `who`-opdracht in C Shell (csh) toont een lijst van gebruikers die momenteel zijn ingelogd op het systeem. Het geeft informatie zoals de gebruikersnaam, terminal, inlogtijd en soms het IP-adres van de gebruiker.

## Gebruik
De basis syntaxis van de `who`-opdracht is als volgt:

```
who [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-a`: Toont alle beschikbare informatie, inclusief inlog- en uitlogtijden.
- `-b`: Geeft de tijd van de laatste systeemopstart weer.
- `-q`: Toont alleen de gebruikersnamen en het aantal ingelogde gebruikers.
- `-H`: Toont de kolomnamen boven de uitvoer.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `who`-opdracht:

1. Toon alle ingelogde gebruikers:
    ```csh
    who
    ```

2. Toon alle beschikbare informatie over ingelogde gebruikers:
    ```csh
    who -a
    ```

3. Toon de tijd van de laatste systeemopstart:
    ```csh
    who -b
    ```

4. Toon alleen de gebruikersnamen en het aantal ingelogde gebruikers:
    ```csh
    who -q
    ```

5. Toon de kolomnamen boven de uitvoer:
    ```csh
    who -H
    ```

## Tips
- Gebruik `who -a` voor een uitgebreid overzicht van ingelogde gebruikers en systeeminformatie.
- Combineer `who` met andere opdrachten zoals `grep` om specifieke gebruikers te filteren.
- Controleer regelmatig wie er is ingelogd, vooral op gedeelde systemen, voor beveiligingsdoeleinden.