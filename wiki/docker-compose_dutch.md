# [Linux] C Shell (csh) docker-compose gebruik: Beheer van multi-container Docker-applicaties

## Overzicht
Het `docker-compose` commando is een hulpmiddel dat het mogelijk maakt om multi-container Docker-applicaties te definiëren en te beheren. Met een enkele configuratiebestand (meestal `docker-compose.yml`) kun je de services, netwerken en volumes van je applicatie specificeren en beheren.

## Gebruik
De basis syntaxis van het `docker-compose` commando is als volgt:

```bash
docker-compose [opties] [argumenten]
```

## Veelvoorkomende Opties
- `up`: Start de gedefinieerde services.
- `down`: Stop en verwijder de containers, netwerken en volumes die door `up` zijn gemaakt.
- `build`: Bouw de services zoals gedefinieerd in het `docker-compose.yml` bestand.
- `logs`: Toon de logboeken van de services.
- `ps`: Lijst de actieve containers die door docker-compose zijn gestart.

## Veelvoorkomende Voorbeelden

### Starten van de applicatie
Om de applicatie te starten zoals gedefinieerd in `docker-compose.yml`, gebruik je:

```bash
docker-compose up
```

### Stoppen van de applicatie
Om de applicatie te stoppen en de containers te verwijderen, gebruik je:

```bash
docker-compose down
```

### Bouw de services
Als je wijzigingen hebt aangebracht in de Dockerfile of de configuratie, kun je de services opnieuw bouwen met:

```bash
docker-compose build
```

### Bekijk de logs
Om de logboeken van de actieve services te bekijken, gebruik je:

```bash
docker-compose logs
```

### Lijst actieve containers
Om een lijst van actieve containers te zien die door docker-compose zijn gestart, gebruik je:

```bash
docker-compose ps
```

## Tips
- Zorg ervoor dat je altijd een geldig `docker-compose.yml` bestand hebt in de huidige directory voordat je `docker-compose` commando's uitvoert.
- Gebruik de optie `-d` met `up` om de containers in de achtergrond te draaien: 

```bash
docker-compose up -d
```

- Controleer regelmatig de logboeken om problemen vroegtijdig te identificeren en op te lossen.
- Maak gebruik van versiebeheer voor je `docker-compose.yml` bestand om wijzigingen bij te houden en samen te werken met anderen.