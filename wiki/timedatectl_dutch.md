# [Linux] C Shell (csh) timedatectl gebruik: Beheer tijd en datum instellingen

## Overzicht
De `timedatectl` opdracht wordt gebruikt om de systeemdatum en -tijd te beheren, evenals om tijdzones in te stellen en de synchronisatie met tijdservers te controleren. Dit is een handig hulpmiddel voor systeembeheerders en gebruikers die nauwkeurige tijdinstellingen nodig hebben.

## Gebruik
De basis syntaxis van de `timedatectl` opdracht is als volgt:

```bash
timedatectl [opties] [argumenten]
```

## Veelvoorkomende opties
- `set-time`: Hiermee stel je de systeemdatum en -tijd in.
- `set-timezone`: Hiermee stel je de tijdzone in.
- `status`: Toont de huidige datum, tijd en tijdzone-instellingen.
- `list-timezones`: Lijst alle beschikbare tijdzones.
- `set-ntp`: Schakelt NTP (Network Time Protocol) synchronisatie in of uit.

## Veelvoorkomende voorbeelden

### Huidige tijd en datum weergeven
Om de huidige datum en tijd weer te geven, gebruik je de volgende opdracht:

```bash
timedatectl status
```

### Tijdzone instellen
Om de tijdzone in te stellen op 'Europe/Amsterdam', gebruik je:

```bash
timedatectl set-timezone Europe/Amsterdam
```

### Systeemdatum en -tijd instellen
Om de systeemdatum en -tijd in te stellen op 1 januari 2024, 12:00, gebruik je:

```bash
timedatectl set-time '2024-01-01 12:00:00'
```

### NTP synchronisatie inschakelen
Om NTP-synchronisatie in te schakelen, gebruik je:

```bash
timedatectl set-ntp true
```

### Tijdzones weergeven
Om een lijst van beschikbare tijdzones weer te geven, gebruik je:

```bash
timedatectl list-timezones
```

## Tips
- Zorg ervoor dat je de juiste tijdzone instelt om verwarring met tijdsafspraken te voorkomen.
- Controleer regelmatig de tijdinstellingen, vooral op servers die afhankelijk zijn van nauwkeurige tijd.
- Gebruik NTP voor automatische tijdsynchronisatie om handmatige aanpassingen te minimaliseren.