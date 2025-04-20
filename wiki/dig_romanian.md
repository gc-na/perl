# [Sistem de operare] C Shell (csh) dig utilizare: [interogare DNS]

## Overview
Comanda `dig` (Domain Information Groper) este un instrument utilizat pentru a interoga serverele DNS (Domain Name System). Aceasta permite utilizatorilor să obțină informații despre adresele IP, înregistrările DNS și alte detalii legate de domenii.

## Usage
Sintaxa de bază a comenzii `dig` este următoarea:

```
dig [opțiuni] [argumente]
```

## Common Options
- `@server` - Specifică serverul DNS pe care doriți să-l interogați.
- `-t type` - Definește tipul de înregistrare DNS pe care doriți să-l căutați (de exemplu, A, MX, TXT).
- `+short` - Afișează rezultatul într-un format scurt, ușor de citit.
- `+trace` - Urmărește calea interogării DNS de la rădăcină până la serverul autoritar.

## Common Examples
1. **Interogarea unei adrese IP pentru un domeniu:**
   ```bash
   dig example.com
   ```

2. **Obținerea înregistrărilor MX pentru un domeniu:**
   ```bash
   dig -t MX example.com
   ```

3. **Interogarea unui server DNS specific:**
   ```bash
   dig @8.8.8.8 example.com
   ```

4. **Afișarea rezultatelor într-un format scurt:**
   ```bash
   dig +short example.com
   ```

5. **Urmărirea căii interogării DNS:**
   ```bash
   dig +trace example.com
   ```

## Tips
- Utilizați opțiunea `+short` pentru a obține rezultate mai concise, mai ales când căutați adrese IP.
- Dacă aveți probleme cu rezolvarea DNS, încercați să interogați un server DNS public, cum ar fi Google DNS (`8.8.8.8`).
- Folosiți `dig` împreună cu alte comenzi de rețea pentru a diagnostica problemele de conectivitate.