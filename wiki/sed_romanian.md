# [Linux] C Shell (csh) sed utilizare: Modificarea textului în fluxuri de date

## Overview
Comanda `sed` (Stream Editor) este un editor de fluxuri de date care permite modificarea textului din fișiere sau din fluxuri de date. Aceasta este folosită frecvent pentru a efectua substituții, ștergeri sau inserții de text.

## Usage
Sintaxa de bază a comenzii `sed` este următoarea:

```bash
sed [opțiuni] [argumente]
```

## Common Options
- `-e`: Permite specificarea mai multor comenzi `sed`.
- `-i`: Modifică fișierul direct, fără a crea un fișier temporar.
- `-n`: Suprimă ieșirea implicită, permițându-vă să controlați ce se afișează.
- `s`: Comanda de substituție, folosită pentru a înlocui textul.

## Common Examples
1. **Substituția unui cuvânt într-un fișier:**
   ```bash
   sed 's/vechi/nou/g' fisier.txt
   ```
   Acest exemplu înlocuiește toate aparițiile cuvântului "vechi" cu "nou" în `fisier.txt`.

2. **Modificarea fișierului direct:**
   ```bash
   sed -i 's/vechi/actualizat/g' fisier.txt
   ```
   Aceasta va modifica fișierul `fisier.txt` direct, înlocuind "vechi" cu "actualizat".

3. **Afișarea doar a liniilor care conțin un anumit cuvânt:**
   ```bash
   sed -n '/cuvânt/p' fisier.txt
   ```
   Aici, comanda va afișa doar liniile din `fisier.txt` care conțin "cuvânt".

4. **Ștergerea liniilor goale dintr-un fișier:**
   ```bash
   sed '/^$/d' fisier.txt
   ```
   Acest exemplu elimină toate liniile goale din `fisier.txt`.

## Tips
- Folosiți opțiunea `-i` cu precauție, deoarece modificările sunt permanente.
- Testați comenzile `sed` cu opțiunea `-n` pentru a verifica rezultatul înainte de a aplica modificări.
- Familiarizați-vă cu expresiile regulate, deoarece `sed` le utilizează pentru a identifica și manipula textul.