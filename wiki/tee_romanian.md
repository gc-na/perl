# [Linux] C Shell (csh) tee utilizare: Scrierea datelor în fișiere și pe ecran

## Overview
Comanda `tee` în C Shell (csh) este utilizată pentru a citi date de la standard input și a le scrie simultan atât pe standard output (de obicei, ecranul), cât și într-un sau mai multe fișiere. Aceasta permite utilizatorilor să vizualizeze datele în timp ce le salvează.

## Usage
Sintaxa de bază a comenzii `tee` este următoarea:

```csh
tee [opțiuni] [argumente]
```

## Common Options
- `-a`: Adaugă datele la sfârșitul fișierului existent, în loc să suprascrie.
- `-i`: Ignoră semnalul de întrerupere (SIGINT) și continuă să scrie datele.

## Common Examples
1. **Scrierea output-ului într-un fișier:**
   ```csh
   echo "Salut, lume!" | tee fisier.txt
   ```
   Aceasta va scrie "Salut, lume!" atât pe ecran, cât și în `fisier.txt`.

2. **Adăugarea output-ului la un fișier existent:**
   ```csh
   echo "Alt text" | tee -a fisier.txt
   ```
   Aceasta va adăuga "Alt text" la sfârșitul fișierului `fisier.txt`.

3. **Scrierea output-ului în mai multe fișiere:**
   ```csh
   echo "Date importante" | tee fisier1.txt fisier2.txt
   ```
   Aceasta va scrie "Date importante" în ambele fișiere `fisier1.txt` și `fisier2.txt`.

## Tips
- Utilizați opțiunea `-a` pentru a evita pierderea datelor existente în fișiere.
- Combinați `tee` cu alte comenzi folosind pipe (`|`) pentru a crea fluxuri de date complexe.
- Verificați permisiunile fișierului pentru a vă asigura că aveți drepturi de scriere înainte de a utiliza `tee`.