# [Linux] C Shell (csh) modprobe gebruik: Laad kernelmodules in

## Overzicht
Het `modprobe` commando wordt gebruikt om kernelmodules in Linux te laden en te verwijderen. Het zorgt ervoor dat de juiste afhankelijkheden worden beheerd, zodat de modules correct functioneren binnen de kernelomgeving.

## Gebruik
De basis syntaxis van het `modprobe` commando is als volgt:

```csh
modprobe [opties] [argumenten]
```

## Veelvoorkomende opties
- `-r` : Verwijdert een module.
- `--list` : Toont een lijst van beschikbare modules.
- `--show-depends` : Toont de afhankelijkheden van een specifieke module.

## Veelvoorkomende voorbeelden

### Een module laden
Om een module te laden, gebruik je het volgende commando:

```csh
modprobe naam_van_module
```

### Een module verwijderen
Om een module te verwijderen, gebruik je de `-r` optie:

```csh
modprobe -r naam_van_module
```

### Afhankelijkheden van een module bekijken
Om de afhankelijkheden van een module te bekijken, gebruik je:

```csh
modprobe --show-depends naam_van_module
```

### Lijst van beschikbare modules
Om een lijst van beschikbare modules te bekijken, gebruik je:

```csh
modprobe --list
```

## Tips
- Controleer altijd of je de juiste module laadt om conflicten te voorkomen.
- Gebruik de `--show-depends` optie om te begrijpen welke andere modules nodig zijn voordat je een module laadt.
- Wees voorzichtig met het verwijderen van modules, vooral als ze in gebruik zijn, om systeeminstabiliteit te voorkomen.