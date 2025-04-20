# [Linux] C Shell (csh) schrijf: [verzend berichten naar andere gebruikers]

## Overzicht
De `write`-opdracht in C Shell (csh) stelt gebruikers in staat om directe berichten te verzenden naar andere ingelogde gebruikers op hetzelfde systeem. Dit is handig voor communicatie tussen gebruikers zonder gebruik te maken van e-mail of andere communicatiemiddelen.

## Gebruik
De basis syntaxis van de `write`-opdracht is als volgt:

```
write [opties] [gebruiker] [tty]
```

Hierbij is `[gebruiker]` de naam van de gebruiker naar wie je een bericht wilt sturen, en `[tty]` is het terminalapparaat (optioneel).

## Veelvoorkomende opties
- `-n`: Stuur geen melding naar de ontvanger dat er een bericht is verzonden.
- `-h`: Geef een korte helptekst weer over het gebruik van de opdracht.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `write`-opdracht:

1. Stuur een bericht naar een gebruiker genaamd "jan":
   ```csh
   write jan
   Hallo Jan, hoe gaat het met je?
   ```

2. Stuur een bericht naar een specifieke terminal van een gebruiker:
   ```csh
   write jan pts/1
   Vergeet niet de vergadering om 3 uur!
   ```

3. Stuur een bericht zonder een melding naar de ontvanger:
   ```csh
   write -n jan
   Ik ben bezig met de rapporten.
   ```

## Tips
- Zorg ervoor dat de ontvanger ingelogd is en dat hun terminal beschikbaar is om berichten te ontvangen.
- Gebruik `mesg` om te controleren of je berichten kunt ontvangen. Typ `mesg` in de terminal om de status te bekijken.
- Wees kort en duidelijk in je berichten om verwarring te voorkomen.