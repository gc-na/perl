# [Linux] C Shell (csh) head utilizare: Afișează primele linii dintr-un fișier

## Overview
Comanda `head` este utilizată pentru a afișa primele linii ale unui fișier. Este utilă pentru a obține rapid o previzualizare a conținutului unui fișier, fără a-l deschide complet.

## Usage
Sintaxa de bază a comenzii `head` este următoarea:

```
head [opțiuni] [argumente]
```

## Common Options
- `-n [număr]`: Specifică numărul de linii de afișat (implicit este 10).
- `-c [număr]`: Afișează un număr specificat de octeți din fișier.
- `-q`: Nu afișează numele fișierului înainte de conținutul acestuia, atunci când se procesează mai multe fișiere.
- `-v`: Afișează numele fișierului înainte de conținutul acestuia, chiar și atunci când se procesează un singur fișier.

## Common Examples
1. Afișarea primelor 10 linii dintr-un fișier:
   ```csh
   head fisier.txt
   ```

2. Afișarea primelor 5 linii dintr-un fișier:
   ```csh
   head -n 5 fisier.txt
   ```

3. Afișarea primelor 20 de octeți dintr-un fișier:
   ```csh
   head -c 20 fisier.txt
   ```

4. Afișarea primelor 10 linii din mai multe fișiere:
   ```csh
   head fisier1.txt fisier2.txt
   ```

5. Afișarea primelor 5 linii dintr-un fișier fără a afișa numele acestuia:
   ```csh
   head -q -n 5 fisier.txt
   ```

## Tips
- Folosește `head` împreună cu `tail` pentru a vizualiza atât începutul, cât și sfârșitul unui fișier.
- Comanda `head` este foarte utilă în scripturi pentru a verifica rapid conținutul fișierelor de log.
- Poți combina `head` cu alte comenzi prin pipe (`|`) pentru a obține rezultate mai complexe.