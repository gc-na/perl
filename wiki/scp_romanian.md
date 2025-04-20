# [Sistem de operare] C Shell (csh) scp utilizare: Transferă fișiere între sisteme

## Overview
Comanda `scp` (secure copy) este utilizată pentru a copia fișiere sau directoare între sisteme printr-o conexiune securizată SSH. Aceasta permite transferul de date în mod sigur, protejând informațiile împotriva interceptării.

## Usage
Sintaxa de bază a comenzii `scp` este următoarea:
```bash
scp [opțiuni] [sursă] [destinație]
```

## Common Options
- `-r`: Copiază recursiv directoare.
- `-P`: Specifică portul SSH (în cazul în care nu este portul standard 22).
- `-i`: Utilizează un fișier de cheie specific pentru autentificare.
- `-v`: Activează modul verbose, oferind informații detaliate despre transfer.

## Common Examples
1. **Copiază un fișier de pe un sistem local pe un server remote:**
   ```bash
   scp /cale/catre/fisier.txt utilizator@server:/cale/destinatie/
   ```

2. **Copiază un fișier de pe un server remote pe sistemul local:**
   ```bash
   scp utilizator@server:/cale/catre/fisier.txt /cale/destinatie/
   ```

3. **Copiază un director întreg de pe un sistem local pe un server remote:**
   ```bash
   scp -r /cale/catre/director utilizator@server:/cale/destinatie/
   ```

4. **Copiază un fișier utilizând un port SSH diferit:**
   ```bash
   scp -P 2222 /cale/catre/fisier.txt utilizator@server:/cale/destinatie/
   ```

## Tips
- Asigurați-vă că aveți permisiunile necesare pentru a accesa fișierele și directoarele pe care doriți să le copiați.
- Utilizați opțiunea `-v` pentru a depana problemele de conectivitate sau de transfer.
- Dacă transferați fișiere mari, luați în considerare utilizarea opțiunii `-C` pentru a activa compresia, ceea ce poate accelera transferul.