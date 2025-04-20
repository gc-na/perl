# [Linux] C Shell (csh) mtr utilizare: instrument de diagnosticare a rețelei

## Overview
Comanda `mtr` (My Traceroute) combină funcționalitatea comenzii `ping` și `traceroute`, oferind o modalitate eficientă de a diagnostica problemele de rețea. Aceasta permite utilizatorilor să monitorizeze rutele de rețea și să verifice latența și pierderile de pachete între gazda locală și o destinație specificată.

## Usage
Sintaxa de bază a comenzii `mtr` este următoarea:

```bash
mtr [options] [arguments]
```

## Common Options
- `-r`: Rulare în modul raport, care va genera un raport și se va închide.
- `-c <număr>`: Specifică numărul de probe de trimis.
- `-i <secunde>`: Setează intervalul de timp între probe.
- `-p`: Afișează porturile utilizate pentru fiecare hop.
- `-n`: Nu efectuează rezolvarea DNS, afișând doar adresele IP.

## Common Examples
1. **Rularea mtr pentru o destinație specifică:**
   ```bash
   mtr google.com
   ```

2. **Generarea unui raport cu 10 probe:**
   ```bash
   mtr -r -c 10 google.com
   ```

3. **Rularea mtr fără rezolvarea DNS:**
   ```bash
   mtr -n google.com
   ```

4. **Setarea unui interval de 2 secunde între probe:**
   ```bash
   mtr -i 2 google.com
   ```

5. **Afișarea porturilor utilizate:**
   ```bash
   mtr -p google.com
   ```

## Tips
- Utilizați opțiunea `-r` pentru a obține un raport concis, util pentru diagnosticare rapidă.
- Rulați `mtr` cu opțiunea `-n` pentru a evita întârzierile cauzate de rezolvarea DNS, mai ales în rețelele lente.
- Monitorizați periodic o destinație pentru a observa variațiile în latență și pierderile de pachete, ceea ce poate ajuta la identificarea problemelor de rețea.