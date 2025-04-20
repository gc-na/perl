# [Linux] C Shell (csh) dig gebruik: DNS-query's uitvoeren

## Overzicht
Het `dig`-commando, wat staat voor "Domain Information Groper", is een krachtig hulpmiddel voor het uitvoeren van DNS-query's. Het wordt vaak gebruikt om informatie over domeinnamen op te vragen, zoals IP-adressen, mailservers en andere DNS-records.

## Gebruik
De basis syntaxis van het `dig`-commando is als volgt:

```csh
dig [opties] [argumenten]
```

## Veelvoorkomende opties
- `@server`: Specificeert een andere DNS-server om de query naar te sturen.
- `-t type`: Bepaalt het type record dat je wilt opvragen (bijv. A, MX, TXT).
- `+short`: Geeft een verkorte output weer, wat handig is voor snelle informatie.
- `+trace`: Volgt de resolutie van de DNS-query stap voor stap.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `dig`:

1. **Basis A-record opvragen:**
   ```csh
   dig example.com
   ```

2. **Specifiek A-record opvragen:**
   ```csh
   dig -t A example.com
   ```

3. **MX-records opvragen:**
   ```csh
   dig -t MX example.com
   ```

4. **Query naar een specifieke DNS-server sturen:**
   ```csh
   dig @8.8.8.8 example.com
   ```

5. **Verkorte output van een A-record:**
   ```csh
   dig +short example.com
   ```

6. **Trace van de DNS-resolutie:**
   ```csh
   dig +trace example.com
   ```

## Tips
- Gebruik de `+short` optie voor een snellere en eenvoudigere output, vooral als je alleen het IP-adres nodig hebt.
- Probeer verschillende recordtypes (zoals MX, TXT) om meer informatie over een domein te verkrijgen.
- Als je problemen hebt met DNS-resolutie, gebruik dan de `+trace` optie om te zien waar het probleem zich voordoet.