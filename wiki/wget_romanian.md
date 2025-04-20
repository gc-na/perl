# [Linux] C Shell (csh) wget utilizare: Descărcarea fișierelor de pe internet

## Overview
Comanda `wget` este un instrument puternic folosit pentru a descărca fișiere de pe internet. Aceasta suportă diverse protocoale, inclusiv HTTP, HTTPS și FTP, și este utilă pentru descărcarea fișierelor mari sau a site-urilor întregi.

## Usage
Sintaxa de bază a comenzii `wget` este următoarea:

```bash
wget [opțiuni] [argumente]
```

## Common Options
Iată câteva opțiuni comune pentru `wget`:

- `-O [fișier]`: Salvează fișierul descărcat cu un nume specificat.
- `-c`: Continuă descărcarea unui fișier incomplet.
- `-r`: Descarcă recursiv toate fișierele dintr-un director.
- `-p`: Descarcă toate resursele necesare pentru a vizualiza o pagină HTML (imagini, CSS etc.).
- `--limit-rate=[viteză]`: Limitează viteza de descărcare.

## Common Examples
Iată câteva exemple practice de utilizare a comenzii `wget`:

1. **Descărcarea unui fișier simplu:**
   ```bash
   wget http://example.com/fișier.txt
   ```

2. **Descărcarea unui fișier și salvarea cu un nume specific:**
   ```bash
   wget -O nou_fișier.txt http://example.com/fișier.txt
   ```

3. **Continuarea descărcării unui fișier incomplet:**
   ```bash
   wget -c http://example.com/fișier_mare.zip
   ```

4. **Descărcarea recursivă a unui site:**
   ```bash
   wget -r http://example.com/
   ```

5. **Descărcarea unei pagini web și a resurselor sale:**
   ```bash
   wget -p http://example.com/pagina.html
   ```

## Tips
- Asigurați-vă că aveți permisiunea de a descărca conținutul de pe site-uri, pentru a respecta drepturile de autor.
- Utilizați opțiunea `--limit-rate` pentru a evita suprasolicitarea lățimii de bandă.
- Verificați opțiunile de autentificare dacă descărcați fișiere de pe servere protejate.