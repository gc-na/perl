# [Linux] C Shell (csh) tail utilizare: Afișează ultimele linii ale unui fișier

## Overview
Comanda `tail` este utilizată pentru a afișa ultimele linii ale unui fișier. Este foarte utilă pentru monitorizarea fișierelor de jurnal sau pentru a verifica rapid conținutul final al unui fișier text.

## Usage
Sintaxa de bază a comenzii `tail` este următoarea:

```csh
tail [opțiuni] [argumente]
```

## Common Options
- `-n [număr]`: Afișează ultimele `număr` de linii din fișier.
- `-f`: Urmărește un fișier în timp real, afișând noi linii pe măsură ce sunt adăugate.
- `-c [număr]`: Afișează ultimele `număr` de octeți din fișier.

## Common Examples
1. Afișează ultimele 10 linii dintr-un fișier:
   ```csh
   tail nume_fisier.txt
   ```

2. Afișează ultimele 20 de linii dintr-un fișier:
   ```csh
   tail -n 20 nume_fisier.txt
   ```

3. Urmărește un fișier de jurnal în timp real:
   ```csh
   tail -f jurnal.log
   ```

4. Afișează ultimele 50 de octeți dintr-un fișier:
   ```csh
   tail -c 50 nume_fisier.txt
   ```

## Tips
- Folosește opțiunea `-f` pentru a monitoriza fișierele de jurnal, astfel încât să poți vedea imediat ce se întâmplă.
- Combină `tail` cu comanda `grep` pentru a căuta anumite șiruri de caractere în ultimele linii ale unui fișier:
  ```csh
  tail -f jurnal.log | grep "eroare"
  ```
- Dacă lucrezi cu fișiere mari, specifică un număr mai mic de linii pentru a evita o ieșire prea lungă.