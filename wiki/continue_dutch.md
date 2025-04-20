# [Linux] C Shell (csh) continue gebruik: Herstart een onderbroken loop

## Overzicht
De `continue` opdracht in C Shell (csh) wordt gebruikt om de huidige iteratie van een loop over te slaan en door te gaan naar de volgende iteratie. Dit is handig wanneer je bepaalde voorwaarden wilt controleren en, indien nodig, de rest van de loop wilt overslaan.

## Gebruik
De basis syntaxis van de `continue` opdracht is als volgt:

```csh
continue [n]
```

Hierbij is `n` een optioneel argument dat aangeeft hoeveel niveaus van geneste loops je wilt overslaan. Als `n` niet wordt opgegeven, wordt de huidige loop voortgezet.

## Veelvoorkomende opties
- `n`: Dit optionele argument geeft aan hoeveel niveaus van geneste loops je wilt overslaan. Bijvoorbeeld, `continue 2` zou de tweede geneste loop overslaan.

## Veelvoorkomende voorbeelden

### Voorbeeld 1: Basis gebruik van continue
In dit voorbeeld wordt een loop gemaakt die getallen van 1 tot 5 doorloopt, maar het getal 3 overslaat.

```csh
foreach i (1 2 3 4 5)
    if ($i == 3) then
        continue
    endif
    echo $i
end
```
**Output:**
```
1
2
4
5
```

### Voorbeeld 2: Geneste loops
Hier is een voorbeeld van het gebruik van `continue` in geneste loops. Dit voorbeeld print de getallen van 1 tot 3 voor de buitenste loop en 1 tot 3 voor de binnenste loop, maar slaat het getal 2 in de binnenste loop over.

```csh
foreach i (1 2 3)
    foreach j (1 2 3)
        if ($j == 2) then
            continue
        endif
        echo "$i $j"
    end
end
```
**Output:**
```
1 1
1 3
2 1
2 3
3 1
3 3
```

## Tips
- Gebruik `continue` om de leesbaarheid van je code te verbeteren door onnodige geneste if-statements te vermijden.
- Wees voorzichtig met het gebruik van `continue` in geneste loops, omdat het de flow van je programma kan beïnvloeden.
- Test je loops grondig om ervoor te zorgen dat ze zich gedragen zoals verwacht, vooral wanneer je met meerdere niveaus van geneste loops werkt.