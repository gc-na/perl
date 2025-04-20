# [Linux] C Shell (csh) psql gebruik: Interactie met PostgreSQL databases

## Overzicht
De `psql` opdracht is een krachtige commandoregelinterface voor het werken met PostgreSQL databases. Het stelt gebruikers in staat om SQL-commando's uit te voeren, database-informatie op te vragen en databasebeheer uit te voeren.

## Gebruik
De basis syntaxis van de `psql` opdracht is als volgt:

```csh
psql [opties] [argumenten]
```

## Veelvoorkomende opties
- `-h`: Specificeert de hostnaam van de database server.
- `-p`: Geeft de poort aan waarop de database server luistert.
- `-U`: Bepaalt de gebruikersnaam die gebruikt moet worden voor de verbinding.
- `-d`: Geeft de naam van de database aan waarmee verbinding moet worden gemaakt.
- `-f`: Voert een SQL-bestand uit.

## Veelvoorkomende voorbeelden

1. Verbinden met een lokale database:
   ```csh
   psql -U gebruikersnaam -d databasenaam
   ```

2. Verbinden met een specifieke host en poort:
   ```csh
   psql -h localhost -p 5432 -U gebruikersnaam -d databasenaam
   ```

3. Uitvoeren van een SQL-bestand:
   ```csh
   psql -U gebruikersnaam -d databasenaam -f pad/naar/bestand.sql
   ```

4. Een eenvoudige SQL-query uitvoeren:
   ```csh
   psql -U gebruikersnaam -d databasenaam -c "SELECT * FROM tabelnaam;"
   ```

## Tips
- Zorg ervoor dat je de juiste gebruikersrechten hebt voor de database waarmee je verbinding maakt.
- Gebruik de `\?` commando binnen `psql` voor een lijst met beschikbare commando's en opties.
- Maak gebruik van het `\q` commando om `psql` netjes af te sluiten.