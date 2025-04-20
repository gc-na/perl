# [Linux] C Shell (csh) uniq gebruik: Verwijder dubbele regels uit bestanden

## Overzicht
De `uniq`-opdracht in C Shell (csh) wordt gebruikt om dubbele regels uit een gesorteerd bestand te verwijderen. Het is een handige tool voor het opschonen van gegevens en het verkrijgen van unieke invoer.

## Gebruik
De basis syntaxis van de `uniq`-opdracht is als volgt:

```csh
uniq [opties] [argumenten]
```

## Veelvoorkomende opties
- `-c`: Tel het aantal keren dat elke regel voorkomt.
- `-d`: Geef alleen de regels weer die meer dan eens voorkomen.
- `-u`: Geef alleen de unieke regels weer die slechts één keer voorkomen.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `uniq`-opdracht:

1. **Verwijder dubbele regels uit een bestand:**
   ```csh
   uniq input.txt > output.txt
   ```

2. **Tel het aantal keren dat elke regel voorkomt:**
   ```csh
   uniq -c input.txt
   ```

3. **Toon alleen de dubbele regels:**
   ```csh
   uniq -d input.txt
   ```

4. **Toon alleen de unieke regels:**
   ```csh
   uniq -u input.txt
   ```

## Tips
- Zorg ervoor dat het bestand gesorteerd is voordat je `uniq` gebruikt, anders worden dubbele regels mogelijk niet correct herkend.
- Je kunt `uniq` combineren met andere commando's zoals `sort` om een efficiëntere gegevensverwerking te bereiken:
  ```csh
  sort input.txt | uniq > output.txt
  ```
- Gebruik de `-c` optie om snel een overzicht te krijgen van de frequentie van regels in je bestand.