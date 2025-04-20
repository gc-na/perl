# [Linux] C Shell (csh) gebruikerscommando: Toont actieve gebruikers

## Overzicht
Het `users` commando in de C Shell (csh) toont een lijst van de gebruikers die momenteel zijn ingelogd op het systeem. Dit is handig voor systeembeheerders en gebruikers die willen weten wie er actief is op de machine.

## Gebruik
De basis syntaxis van het `users` commando is als volgt:

```
users [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-n` : Toont het aantal unieke gebruikers in plaats van hun namen.
- `-r` : Toont alleen de gebruikers die op een terminal zijn ingelogd.

## Veelvoorkomende Voorbeelden

1. **Toon ingelogde gebruikers:**
   ```csh
   users
   ```

2. **Toon het aantal unieke ingelogde gebruikers:**
   ```csh
   users -n
   ```

3. **Toon alleen gebruikers die op een terminal zijn ingelogd:**
   ```csh
   users -r
   ```

## Tips
- Gebruik het `users` commando in combinatie met andere commando's zoals `who` of `w` voor meer gedetailleerde informatie over de ingelogde gebruikers.
- Het `users` commando geeft geen tijdstempels of andere details; voor meer informatie over gebruikerssessies, gebruik `who` of `w`.