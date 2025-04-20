# [Linux] C Shell (csh) hostname utilizare: Afișează sau setează numele gazdei

## Overview
Comanda `hostname` în C Shell (csh) este utilizată pentru a afișa sau a seta numele gazdei sistemului. Numele gazdei este identificatorul unic al unui sistem într-o rețea, fiind esențial pentru comunicarea între computere.

## Usage
Sintaxa de bază a comenzii `hostname` este următoarea:

```
hostname [opțiuni] [argumente]
```

## Common Options
- `-s`: Afișează doar numele scurt al gazdei.
- `-f`: Afișează numele complet al gazdei.
- `-i`: Afișează adresa IP a gazdei.
- `-d`: Afișează domeniul gazdei.

## Common Examples
1. **Afișarea numelui gazdei curente:**
   ```csh
   hostname
   ```

2. **Afișarea numelui scurt al gazdei:**
   ```csh
   hostname -s
   ```

3. **Afișarea numelui complet al gazdei:**
   ```csh
   hostname -f
   ```

4. **Afișarea adresei IP a gazdei:**
   ```csh
   hostname -i
   ```

5. **Setarea unui nou nume pentru gazdă:**
   ```csh
   hostname noul_nume
   ```

## Tips
- Asigurați-vă că aveți permisiuni de administrator atunci când setați un nou nume de gazdă.
- Verificați configurația fișierului `/etc/hosts` pentru a evita conflictele de nume.
- Utilizați comanda `hostname` fără opțiuni pentru a verifica rapid numele gazdei curente în scripturi sau sesiuni de terminal.