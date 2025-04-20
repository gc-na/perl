# [Sistem de operare] C Shell (csh) rsync utilizare: Sincronizarea fișierelor

## Overview
Comanda `rsync` este utilizată pentru a sincroniza fișiere și directoare între două locații, fie pe aceeași mașină, fie pe mașini diferite, prin rețea. Aceasta este eficientă și rapidă, deoarece transferă doar modificările efectuate, nu întregul fișier.

## Usage
Sintaxa de bază a comenzii `rsync` este următoarea:

```bash
rsync [opțiuni] [sursă] [destinație]
```

## Common Options
- `-a`: Activează modul arhivă, care păstrează permisiunile, timestamp-urile, și recursivitatea.
- `-v`: Afișează informații detaliate despre procesul de transfer.
- `-z`: Comprimă datele în timpul transferului pentru a reduce lățimea de bandă utilizată.
- `-r`: Sincronizează recursiv directoare.
- `--delete`: Șterge fișierele din destinație care nu mai există în sursă.

## Common Examples
1. Sincronizarea unui director local:
   ```bash
   rsync -av /cale/catre/sursa/ /cale/catre/destinatie/
   ```

2. Sincronizarea fișierelor între două mașini prin SSH:
   ```bash
   rsync -avz -e ssh /cale/catre/sursa/ utilizator@ip_destinatie:/cale/catre/destinatie/
   ```

3. Sincronizarea și ștergerea fișierelor care nu mai există în sursă:
   ```bash
   rsync -av --delete /cale/catre/sursa/ /cale/catre/destinatie/
   ```

## Tips
- Folosiți opțiunea `-n` (sau `--dry-run`) pentru a simula transferul și a verifica ce fișiere vor fi afectate înainte de a efectua efectiv sincronizarea.
- Asigurați-vă că aveți permisiunile necesare pentru a accesa fișierele sursă și destinație.
- Utilizați `rsync` în scripturi automate pentru backup-uri regulate, având grijă să verificați periodic logurile pentru erori.