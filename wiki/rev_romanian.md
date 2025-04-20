# [Linux] C Shell (csh) rev: Inversează caracterele din fiecare linie

## Overview
Comanda `rev` este utilizată pentru a inversa caracterele din fiecare linie a unui fișier sau dintr-un input standard. Aceasta este utilă în diverse scenarii, cum ar fi procesarea textului sau simpla distracție.

## Usage
Sintaxa de bază a comenzii `rev` este următoarea:

```
rev [opțiuni] [argumente]
```

## Common Options
- `-o <file>`: Scrie rezultatul inversat într-un fișier specificat.
- `-h`, `--help`: Afișează un mesaj de ajutor cu informații despre utilizarea comenzii.

## Common Examples
1. **Inversarea unui text dintr-un fișier:**
   ```bash
   rev fisier.txt
   ```
   Aceasta va inversa fiecare linie din `fisier.txt` și va afișa rezultatul în terminal.

2. **Inversarea unui text introdus manual:**
   ```bash
   echo "Salut, lume!" | rev
   ```
   Rezultatul va fi `!emul ,tulas`.

3. **Scrierea rezultatului într-un fișier:**
   ```bash
   rev -o rezultat.txt fisier.txt
   ```
   Aceasta va inversa conținutul din `fisier.txt` și va salva rezultatul în `rezultat.txt`.

## Tips
- Folosește `rev` împreună cu alte comenzi prin pipe pentru a crea fluxuri de procesare a textului mai complexe.
- Verifică întotdeauna conținutul fișierului de ieșire pentru a te asigura că inversarea s-a realizat corect.