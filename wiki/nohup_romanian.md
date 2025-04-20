# [Linux] C Shell (csh) nohup utilizare: Permite rularea proceselor în fundal

## Overview
Comanda `nohup` (no hang up) este utilizată pentru a rula comenzi sau procese în fundal, astfel încât acestea să continue să funcționeze chiar și după ce utilizatorul se deconectează de la sesiunea terminalului. Aceasta este utilă în special pentru sarcini de lungă durată care nu trebuie întrerupte.

## Usage
Sintaxa de bază a comenzii `nohup` este următoarea:

```csh
nohup [options] [arguments]
```

## Common Options
- `&` - Rulează procesul în fundal.
- `-o [file]` - Specifică un fișier de ieșire pentru mesajele generate de proces.
- `-h` - Afișează ajutorul pentru utilizarea comenzii.

## Common Examples
1. Rularea unui script în fundal:
   ```csh
   nohup ./script.sh &
   ```

2. Rularea unei comenzi cu ieșirea redirecționată:
   ```csh
   nohup ls -l > output.txt &
   ```

3. Rularea unui proces care nu se oprește la deconectare:
   ```csh
   nohup python my_script.py &
   ```

## Tips
- Asigurați-vă că redirecționați ieșirea standard și erorile către un fișier, pentru a putea verifica rezultatele mai târziu.
- Utilizați `jobs` pentru a verifica procesele care rulează în fundal.
- Combinați `nohup` cu `disown` pentru a elimina procesul din lista de sarcini active, astfel încât să nu mai fie asociat cu sesiunea curentă.