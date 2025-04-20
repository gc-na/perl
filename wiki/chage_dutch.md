# [Linux] C Shell (csh) chage gebruik: Beheer van gebruikerswachtwoordverval

## Overzicht
De `chage`-opdracht wordt gebruikt om de vervaldatum van gebruikerswachtwoorden in een Linux-systeem te beheren. Hiermee kun je instellen wanneer een gebruiker zijn wachtwoord moet wijzigen en andere gerelateerde instellingen.

## Gebruik
De basis syntaxis van de `chage`-opdracht is als volgt:

```csh
chage [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-l, --list`: Toon de huidige wachtwoordinstellingen voor een gebruiker.
- `-m, --mindays`: Stel het minimum aantal dagen in tussen wachtwoordwijzigingen.
- `-M, --maxdays`: Stel het maximum aantal dagen in dat een wachtwoord geldig is.
- `-I, --inactive`: Stel het aantal dagen in dat een account inactief blijft na het vervallen van het wachtwoord.
- `-E, --expire`: Stel een vervaldatum in voor het account.

## Veelvoorkomende Voorbeelden
- **Toon de wachtwoordinstellingen voor een gebruiker:**
  ```csh
  chage -l gebruikersnaam
  ```

- **Stel het minimum aantal dagen in tussen wachtwoordwijzigingen op 7 dagen:**
  ```csh
  chage -m 7 gebruikersnaam
  ```

- **Stel het maximum aantal dagen in dat een wachtwoord geldig is op 90 dagen:**
  ```csh
  chage -M 90 gebruikersnaam
  ```

- **Stel het aantal inactieve dagen in op 14 dagen na het vervallen van het wachtwoord:**
  ```csh
  chage -I 14 gebruikersnaam
  ```

- **Stel een vervaldatum in voor het account op 2024-12-31:**
  ```csh
  chage -E 2024-12-31 gebruikersnaam
  ```

## Tips
- Zorg ervoor dat je voldoende rechten hebt om de `chage`-opdracht uit te voeren, meestal moet je root of een sudo-gebruiker zijn.
- Controleer regelmatig de wachtwoordinstellingen van gebruikers om de beveiliging van je systeem te waarborgen.
- Gebruik de `-l` optie om een overzicht te krijgen van de huidige instellingen voordat je wijzigingen aanbrengt.