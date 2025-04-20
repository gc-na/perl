# [Linux] C Shell (csh) dirname gebruik: Haal de directorynaam van een pad op

## Overzicht
De `dirname` opdracht in C Shell (csh) wordt gebruikt om de directorynaam van een opgegeven pad te extraheren. Dit is handig wanneer je alleen de map wilt weten waarin een bestand zich bevindt, zonder de bestandsnaam zelf.

## Gebruik
De basis syntaxis van de `dirname` opdracht is als volgt:

```csh
dirname [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-z`: Negeert lege argumenten.
- `--help`: Toont een helpbericht met informatie over het gebruik van de opdracht.
- `--version`: Geeft de versie-informatie van de `dirname` opdracht.

## Veelvoorkomende Voorbeelden

1. **Basisgebruik**: Verkrijg de directorynaam van een bestand.
   ```csh
   dirname /home/user/document.txt
   ```
   **Output**: `/home/user`

2. **Met een relatief pad**: Verkrijg de directorynaam van een relatief pad.
   ```csh
   dirname ./project/src/main.c
   ```
   **Output**: `./project/src`

3. **Meerdere paden**: Verkrijg de directorynamen van meerdere paden.
   ```csh
   dirname /var/log/syslog /etc/hosts
   ```
   **Output**:
   ```
   /var/log
   /etc
   ```

4. **Lege argumenten negeren**:
   ```csh
   dirname ""
   ```
   **Output**: (geen output, omdat het argument leeg is)

## Tips
- Gebruik `dirname` in scripts om dynamisch directorynamen te extraheren voor verdere verwerking.
- Combineer `dirname` met andere opdrachten zoals `basename` om zowel de directory als de bestandsnaam te verkrijgen.
- Wees voorzichtig met relatieve paden; zorg ervoor dat je in de juiste directory werkt om verwarring te voorkomen.