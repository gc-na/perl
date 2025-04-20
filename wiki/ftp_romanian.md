# [Linux] C Shell (csh) ftp utilizare: Transfer de fișiere între computere

## Overview
Comanda `ftp` este utilizată pentru a transfera fișiere între computere prin intermediul protocolului File Transfer Protocol (FTP). Aceasta permite utilizatorilor să se conecteze la un server FTP, să navigheze prin directoare și să încarce sau să descarce fișiere.

## Usage
Sintaxa de bază a comenzii `ftp` este următoarea:

```csh
ftp [options] [arguments]
```

## Common Options
- `-i`: Dezactivează modul interactiv, permițând transferul de fișiere fără confirmare.
- `-n`: Previne conectarea automată la un server la deschiderea sesiunii.
- `-v`: Activează modul detaliat, afișând informații suplimentare despre transferurile de fișiere.

## Common Examples
1. **Conectare la un server FTP:**
   ```csh
   ftp ftp.example.com
   ```

2. **Descărcarea unui fișier:**
   ```csh
   get numefisier.txt
   ```

3. **Încărcarea unui fișier:**
   ```csh
   put numefisier.txt
   ```

4. **Listarea fișierelor din directorul curent al serverului:**
   ```csh
   ls
   ```

5. **Ieșirea din sesiunea FTP:**
   ```csh
   bye
   ```

## Tips
- Asigurați-vă că aveți permisiunile necesare pentru a accesa fișierele pe serverul FTP.
- Utilizați opțiunea `-i` pentru a evita confirmările repetate atunci când transferați mai multe fișiere.
- Verificați întotdeauna conexiunea la internet înainte de a începe transferurile de fișiere pentru a evita întreruperile.