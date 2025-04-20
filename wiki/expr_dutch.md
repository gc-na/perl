# [Linux] C Shell (csh) expr gebruik: Voer berekeningen en stringoperaties uit

## Overzicht
Het `expr` commando in C Shell (csh) wordt gebruikt voor het uitvoeren van eenvoudige berekeningen en stringoperaties. Het kan worden gebruikt om wiskundige expressies te evalueren, strings te vergelijken en substrings te extraheren.

## Gebruik
De basis syntaxis van het `expr` commando is als volgt:

```csh
expr [opties] [argumenten]
```

## Veelvoorkomende Opties
- `+` : Optelling van twee getallen.
- `-` : Aftrekking van twee getallen.
- `*` : Vermenigvuldiging van twee getallen (gebruik `\*` om het te ontsnappen).
- `/` : Deling van twee getallen.
- `%` : Modulus (rest) van twee getallen.
- `=` : Vergelijking van twee strings of getallen.
- `:` : Verkrijg een substring van een string.

## Veelvoorkomende Voorbeelden

### Voorbeeld 1: Optelling
```csh
expr 5 + 3
```
Dit geeft `8` als resultaat.

### Voorbeeld 2: Aftrekking
```csh
expr 10 - 4
```
Dit geeft `6` als resultaat.

### Voorbeeld 3: Vermenigvuldiging
```csh
expr 7 \* 6
```
Dit geeft `42` als resultaat.

### Voorbeeld 4: Deling
```csh
expr 20 / 4
```
Dit geeft `5` als resultaat.

### Voorbeeld 5: Stringvergelijking
```csh
expr "hello" = "hello"
```
Dit geeft `1` (waar) als resultaat.

### Voorbeeld 6: Substring
```csh
expr substr "abcdef" 2 3
```
Dit geeft `bcd` als resultaat.

## Tips
- Gebruik altijd een backslash (`\`) voor het vermenigvuldigingssymbool (`*`) om verwarring met shell-wildcards te voorkomen.
- Zorg ervoor dat je spaties gebruikt tussen de operatoren en de getallen of strings, anders kan `expr` niet correct functioneren.
- `expr` retourneert `0` voor false en `1` voor true bij vergelijkingen, wat handig kan zijn in scripts.