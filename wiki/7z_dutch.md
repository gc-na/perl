# [Nederlandse] C Shell (csh) 7z Gebruik: Bestanden comprimeren en decomprimeren

## Overzicht
De `7z`-opdracht is een krachtige tool voor het comprimeren en decomprimeren van bestanden en mappen. Het ondersteunt verschillende archiefformaten en biedt een hoge compressieverhouding.

## Gebruik
De basis syntaxis van de `7z`-opdracht is als volgt:

```
7z [opties] [argumenten]
```

## Veelvoorkomende Opties
- `a`: Voeg bestanden toe aan een archief.
- `x`: Extraheer bestanden uit een archief.
- `l`: Lijst de inhoud van een archief.
- `d`: Verwijder bestanden uit een archief.
- `t`: Test de integriteit van een archief.

## Veelvoorkomende Voorbeelden
- **Bestanden comprimeren in een archief:**
  ```bash
  7z a archief.7z bestand1.txt bestand2.txt
  ```

- **Bestanden uit een archief extraheren:**
  ```bash
  7z x archief.7z
  ```

- **Inhoud van een archief weergeven:**
  ```bash
  7z l archief.7z
  ```

- **Bestanden uit een archief verwijderen:**
  ```bash
  7z d archief.7z bestand1.txt
  ```

- **Integriteit van een archief testen:**
  ```bash
  7z t archief.7z
  ```

## Tips
- Zorg ervoor dat je de juiste opties gebruikt om de gewenste actie uit te voeren.
- Gebruik de `l`-optie om de inhoud van een archief te controleren voordat je bestanden extraheert.
- Het is handig om archieven te comprimeren in een map om de organisatie te verbeteren.