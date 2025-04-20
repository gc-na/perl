# [Linux] C Shell (csh) fdisk utilizare: Gestionarea partițiilor de disc

## Overview
Comanda `fdisk` este utilizată pentru a gestiona partițiile de disc pe sistemele de operare bazate pe Unix. Aceasta permite utilizatorilor să creeze, să șteargă și să modifice partițiile de pe un disc dur.

## Usage
Sintaxa de bază a comenzii `fdisk` este următoarea:

```
fdisk [opțiuni] [argumente]
```

## Common Options
- `-l`: Listează toate partițiile disponibile pe disc.
- `-u`: Folosește unități de sectoare pentru dimensiunile partițiilor.
- `-n`: Creează o nouă partiție.
- `-d`: Șterge o partiție existentă.
- `-s`: Afișează dimensiunea unei partiții specificate.

## Common Examples
1. **Listarea partițiilor existente:**
   ```bash
   fdisk -l
   ```

2. **Crearea unei noi partiții:**
   ```bash
   fdisk /dev/sda
   ```
   Apoi, urmați instrucțiunile pentru a crea o nouă partiție.

3. **Ștergerea unei partiții:**
   ```bash
   fdisk /dev/sda
   ```
   Apoi, selectați opțiunea de ștergere și specificați numărul partiției.

4. **Afișarea dimensiunii unei partiții:**
   ```bash
   fdisk -s /dev/sda1
   ```

## Tips
- Asigurați-vă că aveți un backup al datelor importante înainte de a modifica partițiile.
- Utilizați `fdisk` cu prudență, deoarece modificările pot duce la pierderea datelor.
- Consultați documentația oficială sau utilizați `man fdisk` pentru informații detaliate despre opțiuni și utilizare.