# [Linux] C Shell (csh) id gebruik: toon gebruikers- en groepsinformatie

## Overzicht
De `id`-opdracht in C Shell (csh) wordt gebruikt om informatie over de huidige gebruiker en hun groepen weer te geven. Het toont de gebruikers-ID (UID), de primaire groeps-ID (GID) en de groepen waartoe de gebruiker behoort.

## Gebruik
De basis syntaxis van de `id`-opdracht is als volgt:

```csh
id [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-u`: Toont alleen de gebruikers-ID.
- `-g`: Toont alleen de primaire groeps-ID.
- `-G`: Toont alle groeps-ID's waartoe de gebruiker behoort.
- `-n`: Toont de naam in plaats van het nummer voor UID en GID.

## Veelvoorkomende Voorbeelden

1. Toon de volledige gebruikers- en groepsinformatie:
   ```csh
   id
   ```

2. Toon alleen de gebruikers-ID:
   ```csh
   id -u
   ```

3. Toon alleen de primaire groeps-ID:
   ```csh
   id -g
   ```

4. Toon alle groeps-ID's waartoe de gebruiker behoort:
   ```csh
   id -G
   ```

5. Toon de naam van de gebruiker in plaats van het nummer:
   ```csh
   id -n -u
   ```

## Tips
- Gebruik `id` zonder opties om snel een overzicht van je gebruikers- en groepsinformatie te krijgen.
- Combineer opties om specifieke informatie te verkrijgen, zoals het tonen van alleen de groepsnamen met `id -n -G`.
- Deze opdracht is handig voor systeembeheerders om de rechten en lidmaatschappen van gebruikers te controleren.