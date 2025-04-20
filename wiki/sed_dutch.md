# [Linux] C Shell (csh) sed Gebruik: tekstverwerking en -manipulatie

## Overzicht
De `sed` (stream editor) command is een krachtige tool voor tekstverwerking in de C Shell. Het stelt gebruikers in staat om tekstbestanden te bewerken, te filteren en te transformeren op basis van specifieke patronen.

## Gebruik
De basis syntaxis van de `sed` command is als volgt:

```bash
sed [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-e`: Voegt een expressie toe aan de bewerkingen die uitgevoerd moeten worden.
- `-f`: Specificeert een bestand met sed-script dat uitgevoerd moet worden.
- `-i`: Wijzigt bestanden in plaats van de uitvoer naar de standaarduitvoer te sturen.
- `-n`: Schakelt de standaard uitvoer uit, zodat alleen expliciet aangegeven regels worden weergegeven.

## Veelvoorkomende Voorbeelden

1. **Een specifieke regel vervangen:**
   Vervang "oud" door "nieuw" in een bestand.
   ```bash
   sed 's/oud/nieuw/' bestand.txt
   ```

2. **Alle voorkomens van een woord vervangen:**
   Vervang alle voorkomens van "fout" door "correct".
   ```bash
   sed 's/fout/correct/g' bestand.txt
   ```

3. **Regels verwijderen die een bepaald patroon bevatten:**
   Verwijder alle regels die "verwijder" bevatten.
   ```bash
   sed '/verwijder/d' bestand.txt
   ```

4. **Regels nummeren:**
   Nummer alle regels in een bestand.
   ```bash
   sed = bestand.txt | sed 'N;s/\n/ /'
   ```

5. **In-place bewerking met back-up:**
   Vervang "oud" door "nieuw" en maak een back-up van het originele bestand.
   ```bash
   sed -i.bak 's/oud/nieuw/g' bestand.txt
   ```

## Tips
- Gebruik de `-n` optie samen met `p` om alleen specifieke regels weer te geven die aan een patroon voldoen.
- Test je `sed` commando's met een kopie van je bestand om onbedoelde wijzigingen te voorkomen.
- Maak gebruik van reguliere expressies voor complexere zoek- en vervangoperaties.