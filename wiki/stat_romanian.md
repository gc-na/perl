# [Linux] C Shell (csh) stat <Utilizare echivalentă>: obține informații despre fișiere

## Overview
Comanda `stat` este utilizată pentru a obține informații detaliate despre fișiere și directoare, inclusiv dimensiunea, permisiunile, data ultimei modificări și multe altele.

## Usage
Sintaxa de bază a comenzii `stat` este următoarea:

```csh
stat [opțiuni] [argumente]
```

## Common Options
- `-c` : Specifică un format personalizat pentru ieșire.
- `-f` : Afișează informații despre sistemul de fișiere.
- `--help` : Afișează ajutorul pentru utilizare.
- `--version` : Afișează versiunea comenzii.

## Common Examples
1. Obținerea informațiilor despre un fișier specific:
   ```csh
   stat nume_fisier.txt
   ```

2. Afișarea informațiilor într-un format personalizat:
   ```csh
   stat -c '%n: %s bytes' nume_fisier.txt
   ```

3. Obținerea informațiilor despre un director:
   ```csh
   stat /cale/catre/director
   ```

4. Afișarea informațiilor despre sistemul de fișiere:
   ```csh
   stat -f /cale/catre/director
   ```

## Tips
- Folosește opțiunea `-c` pentru a personaliza ieșirea și a obține informațiile exact așa cum ai nevoie.
- Verifică permisiunile fișierului pentru a te asigura că ai accesul necesar.
- Poți combina `stat` cu alte comenzi pentru a crea scripturi utile care să automatizeze sarcini repetitive.