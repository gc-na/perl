# [Linux] C Shell (csh) exec gebruik: Voer een commando uit in de huidige shell

## Overzicht
Het `exec` commando in C Shell (csh) vervangt de huidige shell door een nieuw programma. Dit betekent dat, zodra het nieuwe programma is gestart, de oorspronkelijke shell niet meer beschikbaar is. Het is nuttig voor het uitvoeren van een programma zonder een nieuwe shell te openen.

## Gebruik
De basis syntaxis van het `exec` commando is als volgt:

```
exec [opties] [argumenten]
```

## Veelvoorkomende Opties
- **-l**: Start het programma als een login-shell.
- **-c**: Voer een commando uit dat wordt opgegeven als een string.

## Veelvoorkomende Voorbeelden

### Voorbeeld 1: Een programma uitvoeren
Voer een programma zoals `ls` uit met `exec`:

```csh
exec ls -l
```

### Voorbeeld 2: Een shell vervangen
Vervang de huidige shell door een nieuwe instance van `bash`:

```csh
exec bash
```

### Voorbeeld 3: Een commando uitvoeren met argumenten
Voer een script uit met argumenten:

```csh
exec ./myscript.sh arg1 arg2
```

### Voorbeeld 4: Een login-shell starten
Start een nieuwe login-shell met `exec`:

```csh
exec -l bash
```

## Tips
- Gebruik `exec` wanneer je niet terug wilt keren naar de oorspronkelijke shell na het uitvoeren van een programma.
- Wees voorzichtig met het gebruik van `exec`, omdat het de huidige shell vervangt en je geen toegang meer hebt tot eerdere shell-commando's.
- Test nieuwe commando's in een aparte terminal voordat je ze met `exec` uitvoert om onbedoelde gevolgen te voorkomen.