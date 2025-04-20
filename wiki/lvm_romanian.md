# [Linux] C Shell (csh) lvm utilizare: Gestionarea volumelor logice

## Overview
Comanda `lvm` (Logical Volume Manager) este utilizată pentru a gestiona volumele logice în sistemele Linux. Aceasta permite utilizatorilor să creeze, să redimensioneze și să elimine volume logice, facilitând astfel gestionarea spațiului de stocare.

## Usage
Sintaxa de bază a comenzii `lvm` este următoarea:

```
lvm [options] [arguments]
```

## Common Options
- `create`: Creează un nou volum logic.
- `remove`: Elimină un volum logic existent.
- `extend`: Extinde un volum logic existent.
- `reduce`: Reduce dimensiunea unui volum logic.
- `list`: Afișează informații despre volumele logice existente.

## Common Examples
1. **Crearea unui volum logic:**
   ```bash
   lvm create -n nume_volum -L 10G grup_volum
   ```

2. **Eliminarea unui volum logic:**
   ```bash
   lvm remove nume_volum
   ```

3. **Extinderea unui volum logic:**
   ```bash
   lvm extend -L +5G nume_volum
   ```

4. **Reducerea unui volum logic:**
   ```bash
   lvm reduce -L -5G nume_volum
   ```

5. **Listarea volumelor logice:**
   ```bash
   lvm list
   ```

## Tips
- Asigurați-vă că ați făcut backup datelor importante înainte de a efectua modificări cu `lvm`, în special când reduceți dimensiunea volumelor.
- Utilizați comanda `lvm list` frecvent pentru a verifica starea volumelor logice existente.
- Familiarizați-vă cu opțiunile disponibile prin rularea comenzii `man lvm` pentru a înțelege mai bine funcționalitățile sale.