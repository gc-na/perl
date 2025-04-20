# [Linux] C Shell (csh) trap gebruik: Beheer signalen en exit-acties

## Overzicht
De `trap`-opdracht in C Shell (csh) wordt gebruikt om signalen en exit-acties te beheren. Het stelt gebruikers in staat om specifieke commando's uit te voeren wanneer een bepaald signaal wordt ontvangen of wanneer een script wordt beëindigd.

## Gebruik
De basis syntaxis van de `trap`-opdracht is als volgt:

```csh
trap [actie] [signaal]
```

Hierbij is `[actie]` het commando dat moet worden uitgevoerd en `[signaal]` het signaal dat de actie triggert.

## Veelvoorkomende opties
- `SIGINT`: Dit signaal wordt verzonden wanneer de gebruiker Ctrl+C indrukt. Het kan worden gebruikt om een script veilig te beëindigen.
- `SIGTERM`: Dit signaal wordt verzonden om een proces te beëindigen. Het kan worden opgevangen om schoonmaakacties uit te voeren voordat het script stopt.
- `EXIT`: Dit signaal wordt verzonden wanneer een script eindigt. Het kan worden gebruikt om opruimacties uit te voeren.

## Veelvoorkomende voorbeelden

### Voorbeeld 1: Opvangen van SIGINT
Dit voorbeeld toont hoe je een script kunt laten stoppen met een boodschap wanneer Ctrl+C wordt ingedrukt.

```csh
trap 'echo "Script onderbroken"; exit' SIGINT
while true
do
    echo "Voer iets in (druk Ctrl+C om te stoppen)"
    sleep 1
end
```

### Voorbeeld 2: Opruimen bij beëindigen
Hier is een voorbeeld dat een opruimactie uitvoert wanneer het script wordt beëindigd.

```csh
trap 'echo "Opruimen..."; rm -f temp.txt' EXIT
echo "Script aan het draaien..."
touch temp.txt
sleep 5
```

### Voorbeeld 3: Opvangen van SIGTERM
Dit voorbeeld laat zien hoe je een actie kunt uitvoeren wanneer het script een SIGTERM-signaal ontvangt.

```csh
trap 'echo "Ontvangen SIGTERM, beëindigen..."' SIGTERM
while true
do
    echo "Script draait... (druk Ctrl+Z om op te schorten)"
    sleep 2
end
```

## Tips
- Gebruik `trap` om ervoor te zorgen dat je scripts netjes worden afgesloten, vooral als ze tijdelijke bestanden aanmaken.
- Test je `trap`-instellingen grondig om er zeker van te zijn dat ze de gewenste acties uitvoeren bij het ontvangen van signalen.
- Houd rekening met de volgorde van signalen; sommige signalen kunnen andere signalen overschrijven of negeren.