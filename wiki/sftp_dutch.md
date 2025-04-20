# [Linux] C Shell (csh) sftp gebruik: Bestanden overdragen via een beveiligde verbinding

## Overzicht
De `sftp` (Secure File Transfer Protocol) opdracht wordt gebruikt om bestanden veilig te verzenden en ontvangen over een netwerk. Het biedt een veilige manier om bestanden te verplaatsen tussen een lokale en een externe computer, gebruikmakend van SSH (Secure Shell) voor encryptie.

## Gebruik
De basis syntaxis van de `sftp` opdracht is als volgt:

```csh
sftp [opties] [gebruikersnaam@host]
```

## Veelvoorkomende Opties
- `-b batchfile`: Voer opdrachten uit vanuit een batchbestand.
- `-C`: Schakel compressie in voor snellere overdracht.
- `-o option`: Specificeer een extra optie voor de SSH-verbinding.
- `-P port`: Geef een alternatieve poort op voor de verbinding.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `sftp` opdracht:

1. Verbinden met een externe server:
   ```csh
   sftp gebruiker@voorbeeld.com
   ```

2. Een bestand uploaden naar de server:
   ```csh
   put lokaal_bestand.txt
   ```

3. Een bestand downloaden van de server:
   ```csh
   get server_bestand.txt
   ```

4. Een hele map downloaden:
   ```csh
   get -r mapnaam
   ```

5. Een bestand verwijderen van de server:
   ```csh
   rm server_bestand.txt
   ```

## Tips
- Gebruik de `-C` optie om de overdrachtssnelheid te verbeteren, vooral bij grote bestanden.
- Zorg ervoor dat je de juiste machtigingen hebt op de server om bestanden te uploaden of te verwijderen.
- Maak gebruik van batchbestanden om meerdere opdrachten in één keer uit te voeren, wat tijd kan besparen bij repetitieve taken.