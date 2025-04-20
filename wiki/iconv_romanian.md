# [Linux] C Shell (csh) iconv utilizare: Conversia între codificări de caractere

## Overview
Comanda `iconv` este utilizată pentru a converti fișiere sau fluxuri de date între diferite codificări de caractere. Aceasta este utilă atunci când trebuie să lucrați cu texte în diverse limbi sau formate care necesită codificări specifice.

## Usage
Sintaxa de bază a comenzii `iconv` este următoarea:

```csh
iconv [opțiuni] [argumente]
```

## Common Options
- `-f, --from-code=CODE`: Specifică codificarea de caractere sursă.
- `-t, --to-code=CODE`: Specifică codificarea de caractere țintă.
- `-o, --output=FILE`: Salvează rezultatul într-un fișier specificat.
- `-c`: Ignoră caracterele invalide în timpul conversiei.

## Common Examples
1. **Conversia unui fișier din UTF-8 în ISO-8859-1**:
   ```csh
   iconv -f UTF-8 -t ISO-8859-1 input.txt -o output.txt
   ```

2. **Conversia unui fișier din Windows-1252 în UTF-8**:
   ```csh
   iconv -f WINDOWS-1252 -t UTF-8 input.txt -o output.txt
   ```

3. **Conversia unui text dintr-un flux standard**:
   ```csh
   echo "Text în UTF-8" | iconv -f UTF-8 -t ISO-8859-1
   ```

4. **Conversia unui fișier și ignorarea caracterelor invalide**:
   ```csh
   iconv -f UTF-8 -t ISO-8859-1 -c input.txt -o output.txt
   ```

## Tips
- Asigurați-vă că specificați corect codificările de caractere pentru a evita pierderea de date.
- Utilizați opțiunea `-o` pentru a salva rezultatul într-un fișier, în loc să suprascrieți fișierul original.
- Verificați întotdeauna rezultatul conversiei pentru a vă asigura că nu au apărut erori.