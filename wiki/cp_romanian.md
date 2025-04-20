# [Linux] C Shell (csh) cp utilizare: Copierea fișierelor și directoarelor

## Overview
Comanda `cp` este utilizată în C Shell (csh) pentru a copia fișiere și directoare. Aceasta permite utilizatorilor să creeze copii ale fișierelor existente, facilitând gestionarea datelor.

## Usage
Sintaxa de bază a comenzii `cp` este următoarea:

```csh
cp [opțiuni] [argumente]
```

## Common Options
- `-i`: Solicita confirmarea înainte de a suprascrie fișierele existente.
- `-r`: Copiază directoare recursiv, inclusiv toate fișierele și subdirectoarele.
- `-u`: Copiază fișierele doar dacă sursa este mai nouă decât destinația sau dacă destinația nu există.
- `-v`: Afișează informații detaliate despre fișierele copiate.

## Common Examples
1. **Copierea unui fișier:**
   ```csh
   cp fisier.txt copia_fisier.txt
   ```
   Aceasta va crea o copie a `fisier.txt` numită `copia_fisier.txt`.

2. **Copierea unui director recursiv:**
   ```csh
   cp -r director_original/ director_copie/
   ```
   Aceasta va copia întregul conținut al `director_original` în `director_copie`.

3. **Copierea cu confirmare:**
   ```csh
   cp -i fisier.txt copia_fisier.txt
   ```
   Aceasta va solicita confirmarea înainte de a suprascrie `copia_fisier.txt`, dacă acesta există.

4. **Copierea fișierelor doar dacă sursa este mai nouă:**
   ```csh
   cp -u fisier_nou.txt fisier_vechi.txt
   ```
   Aceasta va copia `fisier_nou.txt` în `fisier_vechi.txt` doar dacă `fisier_nou.txt` este mai recent.

## Tips
- Folosiți opțiunea `-v` pentru a urmări progresul copiei, mai ales când copiați multe fișiere.
- Verificați întotdeauna destinația pentru a evita suprascrierea accidentală a fișierelor importante.
- Când copiați directoare, asigurați-vă că folosiți opțiunea `-r` pentru a include toate subdirectoarele și fișierele.