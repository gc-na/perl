# [Linux] C Shell (csh) hostname gebruik: Toon de naam van de host

## Overzicht
De `hostname` opdracht in C Shell (csh) wordt gebruikt om de naam van de huidige host weer te geven of om deze te wijzigen. Dit is nuttig voor netwerkinstellingen en identificatie van het systeem binnen een netwerk.

## Gebruik
De basis syntaxis van de `hostname` opdracht is als volgt:

```csh
hostname [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-f` : Toon de volledig gekwalificeerde domeinnaam (FQDN).
- `-s` : Toon alleen de korte naam van de host.
- `-i` : Toon het IP-adres van de host.

## Veelvoorkomende Voorbeelden

1. **Toon de huidige hostnaam:**
   ```csh
   hostname
   ```

2. **Toon de volledig gekwalificeerde domeinnaam:**
   ```csh
   hostname -f
   ```

3. **Toon alleen de korte naam van de host:**
   ```csh
   hostname -s
   ```

4. **Toon het IP-adres van de host:**
   ```csh
   hostname -i
   ```

5. **Wijzig de hostnaam:**
   ```csh
   hostname nieuwe-hostnaam
   ```

## Tips
- Zorg ervoor dat je voldoende rechten hebt om de hostnaam te wijzigen, meestal zijn root-rechten vereist.
- Controleer altijd de huidige hostnaam voordat je wijzigingen aanbrengt, om verwarring te voorkomen.
- Gebruik de `hostname` opdracht in scripts om dynamisch de hostnaam te verkrijgen voor logging of netwerkconfiguraties.