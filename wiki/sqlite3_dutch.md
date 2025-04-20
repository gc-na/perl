# [Linux] C Shell (csh) sqlite3 gebruik: Beheer van SQLite-databases

## Overzicht
De `sqlite3`-opdracht is een krachtige tool voor het beheren en bewerken van SQLite-databases. Met deze opdracht kun je databases aanmaken, gegevens invoegen, bewerken, opvragen en verwijderen, evenals verschillende database-instellingen en -structuren beheren.

## Gebruik
De basis syntaxis van de `sqlite3`-opdracht is als volgt:

```csh
sqlite3 [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-init FILE`: Voer de SQL-commando's in het opgegeven bestand uit bij het opstarten van sqlite3.
- `-batch`: Voer de opdracht uit in batchmodus, waarbij geen interactieve prompts worden weergegeven.
- `-header`: Toon de kolomkoppen bij het weergeven van resultaten.
- `-version`: Toon de versie van sqlite3.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `sqlite3`-opdracht:

1. **Een nieuwe database aanmaken:**
   ```csh
   sqlite3 mijn_database.db
   ```

2. **Een tabel aanmaken:**
   ```csh
   sqlite3 mijn_database.db "CREATE TABLE gebruikers (id INTEGER PRIMARY KEY, naam TEXT);"
   ```

3. **Gegevens invoegen in een tabel:**
   ```csh
   sqlite3 mijn_database.db "INSERT INTO gebruikers (naam) VALUES ('Jan');"
   ```

4. **Gegevens opvragen uit een tabel:**
   ```csh
   sqlite3 mijn_database.db "SELECT * FROM gebruikers;"
   ```

5. **Een database exporteren naar een tekstbestand:**
   ```csh
   sqlite3 mijn_database.db ".output gebruikers.txt" ".dump" ".output stdout"
   ```

## Tips
- Gebruik de `-header` optie om de resultaten beter leesbaar te maken.
- Maak regelmatig back-ups van je databasebestanden om gegevensverlies te voorkomen.
- Experimenteer met de interactieve modus door simpelweg `sqlite3 mijn_database.db` in te voeren en SQL-commando's direct in te voeren.