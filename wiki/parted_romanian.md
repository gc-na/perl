# [Linux] C Shell (csh) parted utilizare: gestionarea partițiilor de disc

## Overview
Comanda `parted` este un instrument utilizat pentru a gestiona partițiile de disc pe sistemele Linux. Aceasta permite utilizatorilor să creeze, să șteargă, să redimensionze și să modifice partițiile de pe unitățile de stocare.

## Usage
Sintaxa de bază a comenzii `parted` este următoarea:

```csh
parted [options] [arguments]
```

## Common Options
- `-l` sau `--list`: Listează toate dispozitivele de stocare și partițiile acestora.
- `mkpart`: Creează o nouă partiție.
- `rm`: Șterge o partiție existentă.
- `resizepart`: Redimensionează o partiție existentă.
- `print`: Afișează informații despre partițiile existente.

## Common Examples
1. **Listarea partițiilor existente:**
   ```csh
   parted -l
   ```

2. **Crearea unei noi partiții:**
   ```csh
   parted /dev/sda mkpart primary ext4 1MiB 100MiB
   ```

3. **Ștergerea unei partiții:**
   ```csh
   parted /dev/sda rm 1
   ```

4. **Redimensionarea unei partiții:**
   ```csh
   parted /dev/sda resizepart 1 200MiB
   ```

5. **Afișarea informațiilor despre partiții:**
   ```csh
   parted /dev/sda print
   ```

## Tips
- Asigurați-vă că aveți backup-uri ale datelor importante înainte de a modifica partițiile.
- Utilizați comanda `print` pentru a verifica structura actuală a partițiilor înainte de a efectua modificări.
- Rulați `parted` cu privilegii de administrator (de exemplu, folosind `sudo`) pentru a avea acces la toate funcțiile sale.