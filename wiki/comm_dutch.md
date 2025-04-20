# [Linux] C Shell (csh) comm commando: Vergelijk twee gesorteerde bestanden

## Overzicht
Het `comm` commando wordt gebruikt om de overeenkomsten en verschillen tussen twee gesorteerde bestanden te vergelijken. Het geeft de inhoud van de bestanden weer in drie kolommen: unieke regels van het eerste bestand, unieke regels van het tweede bestand en gemeenschappelijke regels.

## Gebruik
De basis syntaxis van het `comm` commando is als volgt:

```
comm [opties] [bestanden]
```

## Veelvoorkomende Opties
- `-1`: Onderdruk de eerste kolom (unieke regels van het eerste bestand).
- `-2`: Onderdruk de tweede kolom (unieke regels van het tweede bestand).
- `-3`: Onderdruk de derde kolom (gemeenschappelijke regels).
- `-i`: Negeer hoofdlettergebruik bij de vergelijking.

## Veelvoorkomende Voorbeelden

1. **Basisvergelijking van twee bestanden:**
   ```csh
   comm bestand1.txt bestand2.txt
   ```

2. **Alleen gemeenschappelijke regels weergeven:**
   ```csh
   comm -3 bestand1.txt bestand2.txt
   ```

3. **Unieke regels van het eerste bestand weergeven:**
   ```csh
   comm -2 bestand1.txt bestand2.txt
   ```

4. **Vergelijking met hoofdlettergevoeligheid genegeerd:**
   ```csh
   comm -i bestand1.txt bestand2.txt
   ```

## Tips
- Zorg ervoor dat de bestanden gesorteerd zijn voordat je `comm` gebruikt, anders kan de output onvoorspelbaar zijn.
- Gebruik de opties om alleen de informatie te krijgen die je nodig hebt, dit maakt de output overzichtelijker.
- Combineer `comm` met andere commando's zoals `sort` om automatisch gesorteerde invoer te genereren.