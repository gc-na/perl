# [Linux] C Shell (csh) lvm gebruik: Beheer van logische volumes

## Overzicht
De `lvm` (Logical Volume Manager) opdracht wordt gebruikt voor het beheren van logische volumes in Linux-systemen. Het stelt gebruikers in staat om opslagcapaciteit dynamisch te beheren, volumes te creëren, te verwijderen en aan te passen zonder dat het systeem opnieuw opgestart hoeft te worden.

## Gebruik
De basis syntaxis van de `lvm` opdracht is als volgt:

```
lvm [opties] [argumenten]
```

## Veelvoorkomende Opties
- `create`: Maak een nieuw logisch volume aan.
- `remove`: Verwijder een bestaand logisch volume.
- `extend`: Vergroot een logisch volume.
- `reduce`: Verklein een logisch volume.
- `list`: Toon een lijst van logische volumes.

## Veelvoorkomende Voorbeelden

### 1. Een nieuw logisch volume aanmaken
```bash
lvm create -n mijn_volume -L 10G mijn_volume_group
```

### 2. Een logisch volume verwijderen
```bash
lvm remove mijn_volume
```

### 3. Een logisch volume vergroten
```bash
lvm extend -L +5G mijn_volume
```

### 4. Een logisch volume verkleinen
```bash
lvm reduce -L -5G mijn_volume
```

### 5. Een lijst van logische volumes weergeven
```bash
lvm list
```

## Tips
- Zorg ervoor dat je altijd een back-up maakt van belangrijke gegevens voordat je wijzigingen aanbrengt aan logische volumes.
- Controleer de beschikbare ruimte in je volume group met de `vgdisplay` opdracht voordat je volumes aanmaakt of vergroot.
- Gebruik de `--dry-run` optie bij het uitvoeren van destructieve opdrachten om te zien wat er zou gebeuren zonder daadwerkelijk wijzigingen aan te brengen.