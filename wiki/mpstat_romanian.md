# [Linux] C Shell (csh) mpstat utilizare: Monitorizarea statisticilor CPU

## Overview
Comanda `mpstat` este utilizată pentru a afișa statistici despre utilizarea CPU-ului pe un sistem. Aceasta oferă informații despre procesele de lucru și utilizarea resurselor, ajutând utilizatorii să analizeze performanța sistemului.

## Usage
Sintaxa de bază a comenzii `mpstat` este următoarea:

```csh
mpstat [options] [arguments]
```

## Common Options
- `-P ALL`: Afișează statistici pentru toate procesoarele.
- `-u`: Afișează utilizarea CPU-ului.
- `-r`: Afișează statistici despre utilizarea memoriei.
- `-h`: Afișează ajutorul pentru utilizarea comenzii.

## Common Examples
1. Afișarea statisticilor CPU pentru toate procesoarele:
   ```csh
   mpstat -P ALL
   ```

2. Afișarea utilizării CPU-ului:
   ```csh
   mpstat -u
   ```

3. Afișarea statisticilor de memorie:
   ```csh
   mpstat -r
   ```

4. Afișarea statisticilor CPU la fiecare 5 secunde:
   ```csh
   mpstat 5
   ```

## Tips
- Utilizați opțiunea `-P ALL` pentru a obține o imagine de ansamblu completă a utilizării CPU-ului pe toate procesoarele.
- Rulați `mpstat` cu un interval de timp (de exemplu, `mpstat 5`) pentru a monitoriza utilizarea CPU-ului în timp real.
- Verificați periodic statisticile pentru a identifica eventualele probleme de performanță ale sistemului.