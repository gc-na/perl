# [Linux] C Shell (csh) expr utilizare: Evaluarea expresiilor matematice și logice

## Overview
Comanda `expr` este utilizată în C Shell pentru evaluarea expresiilor matematice și logice. Aceasta poate efectua operații aritmetice, comparări și manipulări de șiruri de caractere.

## Usage
Sintaxa de bază a comenzii `expr` este următoarea:

```csh
expr [opțiuni] [argumente]
```

## Common Options
- `+` : Adunare.
- `-` : Scădere.
- `*` : Înmulțire (trebuie să fie escapată cu un backslash: `\*`).
- `/` : Împărțire.
- `%` : Modulo.
- `=` : Comparare pentru egalitate.
- `!=` : Comparare pentru inegalitate.
- `>` : Comparare pentru mai mare.
- `<` : Comparare pentru mai mic.

## Common Examples
1. **Adunare a două numere:**
   ```csh
   expr 5 + 3
   ```
   Rezultatul va fi `8`.

2. **Scădere a două numere:**
   ```csh
   expr 10 - 4
   ```
   Rezultatul va fi `6`.

3. **Înmulțire a două numere:**
   ```csh
   expr 7 \* 6
   ```
   Rezultatul va fi `42`.

4. **Împărțire a două numere:**
   ```csh
   expr 20 / 4
   ```
   Rezultatul va fi `5`.

5. **Comparare pentru egalitate:**
   ```csh
   expr 5 = 5
   ```
   Rezultatul va fi `1` (adevărat).

6. **Comparare pentru mai mare:**
   ```csh
   expr 10 \> 3
   ```
   Rezultatul va fi `1` (adevărat).

## Tips
- Asigurați-vă că utilizați un backslash (`\`) înainte de simbolul de înmulțire (`*`) pentru a evita interpretarea acestuia de către shell.
- `expr` returnează `0` pentru fals și `1` pentru adevărat în evaluările logice.
- Este util să folosiți `expr` în scripturi pentru a evalua condiții și a efectua calcule simple.