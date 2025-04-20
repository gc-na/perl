# [Linux] C Shell (csh) script utilizare: Înregistrează sesiuni de terminal

## Overview
Comanda `script` este utilizată pentru a înregistra o sesiune de terminal într-un fișier. Aceasta permite utilizatorilor să salveze ieșirea tuturor comenzilor și rezultatelor într-un fișier text, facilitând revizuirea ulterioară a activităților efectuate în terminal.

## Usage
Sintaxa de bază a comenzii `script` este următoarea:

```csh
script [opțiuni] [argumente]
```

## Common Options
- `-a` : Adaugă ieșirea la un fișier existent în loc să îl suprascrie.
- `-f` : Scrie imediat ieșirea în fișier, fără a aștepta terminarea sesiunii.
- `-q` : Rulați comanda în mod tăcut, fără a afișa mesajul de început.
- `-t` : Înregistrează timpii de execuție pentru fiecare comandă.

## Common Examples
1. **Începerea unei sesiuni de înregistrare:**
   ```csh
   script sesiune.txt
   ```
   Aceasta va începe o sesiune de înregistrare și va salva ieșirea în `sesiune.txt`.

2. **Adăugarea ieșirii la un fișier existent:**
   ```csh
   script -a sesiune_adaugata.txt
   ```
   Aceasta va adăuga ieșirea la `sesiune_adaugata.txt` fără a șterge conținutul existent.

3. **Rularea în mod tăcut:**
   ```csh
   script -q sesiune_tacuta.txt
   ```
   Aceasta va începe o sesiune de înregistrare fără a afișa mesajul de început.

4. **Înregistrarea timpii de execuție:**
   ```csh
   script -t sesiune_timp.txt
   ```
   Aceasta va salva timpii de execuție împreună cu ieșirea în `sesiune_timp.txt`.

## Tips
- Asigurați-vă că verificați fișierul de ieșire după terminarea sesiunii pentru a vă asigura că toate comenzile dorite au fost înregistrate.
- Utilizați opțiunea `-f` dacă doriți să vizualizați imediat ieșirea în timp real, ceea ce poate fi util pentru sesiuni lungi.
- Nu uitați să opriți sesiunea de înregistrare tastând `exit` sau `Ctrl+D` pentru a salva corect fișierul.