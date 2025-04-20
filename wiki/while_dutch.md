# [Linux] C Shell (csh) while gebruiken: Voer een commando uit zolang een voorwaarde waar is

## Overzicht
De `while`-opdracht in C Shell (csh) wordt gebruikt om een bepaalde reeks commando's herhaaldelijk uit te voeren zolang een opgegeven voorwaarde waar is. Dit is nuttig voor het automatiseren van taken die afhankelijk zijn van dynamische voorwaarden.

## Gebruik
De basis syntaxis van de `while`-opdracht is als volgt:

```csh
while (voorwaarde)
    commando's
end
```

## Veelvoorkomende opties
- **voorwaarde**: Dit is de expressie die geëvalueerd wordt. Zolang deze waar is, worden de commando's binnen de `while`-lus uitgevoerd.
  
## Veelvoorkomende voorbeelden

### Voorbeeld 1: Eenvoudige tel-lus
Dit voorbeeld toont hoe je een teller kunt gebruiken om een commando herhaaldelijk uit te voeren.

```csh
set i = 1
while ($i <= 5)
    echo "Huidige waarde van i: $i"
    @ i++
end
```

### Voorbeeld 2: Bestanden lezen
Hier is een voorbeeld waarbij we door een lijst van bestanden itereren en deze afdrukken.

```csh
set files = (bestand1.txt bestand2.txt bestand3.txt)
set i = 1
while ($i <= $#files)
    echo "Verwerken: $files[$i]"
    @ i++
end
```

### Voorbeeld 3: Wacht op een bestand
Dit voorbeeld wacht totdat een specifiek bestand beschikbaar is.

```csh
set bestand = "output.txt"
while (! -e $bestand)
    echo "Wachten op $bestand..."
    sleep 1
end
echo "$bestand is nu beschikbaar."
```

## Tips
- Zorg ervoor dat je de juiste syntaxis gebruikt, vooral met haakjes en spaties.
- Gebruik `sleep` in een `while`-lus om systeembronnen te sparen als je wacht op een bepaalde voorwaarde.
- Test je voorwaarden grondig om oneindige lussen te voorkomen, wat kan leiden tot systeemvertragingen.