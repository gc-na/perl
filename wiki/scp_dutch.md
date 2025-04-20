# [Linux] C Shell (csh) scp gebruik: Bestanden veilig kopiëren tussen systemen

## Overzicht
De `scp` (secure copy) opdracht wordt gebruikt om bestanden veilig te kopiëren tussen lokale en externe systemen via SSH (Secure Shell). Het biedt een eenvoudige manier om gegevens over netwerken te verplaatsen met encryptie voor extra beveiliging.

## Gebruik
De basis syntaxis van de `scp` opdracht is als volgt:

```csh
scp [opties] [bron] [doel]
```

## Veelvoorkomende opties
- `-r`: Kopieert directories recursief.
- `-P [poort]`: Specificeert de poort voor de SSH-verbinding.
- `-i [sleutel]`: Gebruikt een specifieke privésleutel voor authenticatie.
- `-v`: Verhoogt de uitvoer voor debugging en toont gedetailleerde informatie over de overdracht.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `scp`:

1. **Kopieer een lokaal bestand naar een externe server:**
   ```csh
   scp /pad/naar/lokaal_bestand.txt gebruiker@server:/pad/naar/doel/
   ```

2. **Kopieer een bestand van een externe server naar de lokale machine:**
   ```csh
   scp gebruiker@server:/pad/naar/externe_bestand.txt /pad/naar/lokaal/
   ```

3. **Kopieer een hele directory naar een externe server:**
   ```csh
   scp -r /pad/naar/lokale_directory gebruiker@server:/pad/naar/doel/
   ```

4. **Kopieer een bestand naar een specifieke poort:**
   ```csh
   scp -P 2222 /pad/naar/lokaal_bestand.txt gebruiker@server:/pad/naar/doel/
   ```

## Tips
- Zorg ervoor dat SSH is geïnstalleerd en geconfigureerd op zowel de lokale als de externe machine.
- Gebruik de `-v` optie voor extra informatie als je problemen ondervindt bij het kopiëren van bestanden.
- Overweeg het gebruik van SSH-sleutels voor een veiligere en eenvoudigere authenticatie zonder wachtwoorden.