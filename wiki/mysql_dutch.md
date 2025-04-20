# [Linux] C Shell (csh) mysql gebruik: Beheer van MySQL-databases

## Overzicht
De `mysql`-opdracht is een commandoregelprogramma dat wordt gebruikt om verbinding te maken met een MySQL-database. Het stelt gebruikers in staat om SQL-commando's uit te voeren, databases te beheren en gegevens te manipuleren.

## Gebruik
De basis syntaxis van de `mysql`-opdracht is als volgt:

```bash
mysql [options] [arguments]
```

## Veelvoorkomende opties
- `-u [username]`: Specificeert de gebruikersnaam voor de databaseverbinding.
- `-p`: Vraagt om een wachtwoord voor de opgegeven gebruiker.
- `-h [hostname]`: Geeft de hostnaam van de MySQL-server op.
- `-D [database]`: Verbindt direct met de opgegeven database.
- `--execute [query]`: Voert een specifieke SQL-query uit.

## Veelvoorkomende voorbeelden

### Verbinden met een lokale MySQL-database
```bash
mysql -u root -p
```

### Verbinden met een specifieke database
```bash
mysql -u root -p -D mijn_database
```

### Een SQL-query uitvoeren vanuit de opdrachtregel
```bash
mysql -u root -p --execute "SELECT * FROM gebruikers;"
```

### Een SQL-script uitvoeren
```bash
mysql -u root -p mijn_database < script.sql
```

## Tips
- Zorg ervoor dat je altijd de juiste gebruikersrechten hebt voor de database waarmee je verbinding maakt.
- Gebruik de optie `-h` om verbinding te maken met een externe MySQL-server.
- Maak gebruik van SQL-scripts voor complexe queries om de leesbaarheid en herbruikbaarheid te verbeteren.