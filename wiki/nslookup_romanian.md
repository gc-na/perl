# [Sistem de operare] C Shell (csh) nslookup utilizare: [verificare DNS]

## Overview
Comanda `nslookup` este utilizată pentru a interoga serverele DNS pentru a obține informații despre numele de domenii și adresele IP asociate. Aceasta este o unealtă esențială pentru diagnosticarea problemelor de rețea și pentru verificarea configurărilor DNS.

## Usage
Sintaxa de bază a comenzii `nslookup` este următoarea:

```
nslookup [opțiuni] [argumente]
```

## Common Options
- `-type=tip`: Specifică tipul de înregistrare DNS pe care doriți să-l căutați (de exemplu, A, MX, CNAME).
- `-timeout=n`: Setează timpul de așteptare pentru răspunsul serverului DNS (în secunde).
- `-retry=n`: Setează numărul de încercări pentru a obține un răspuns de la serverul DNS.

## Common Examples
1. **Căutarea unei adrese IP pentru un nume de domeniu:**
   ```csh
   nslookup www.example.com
   ```

2. **Căutarea unei înregistrări MX pentru un domeniu:**
   ```csh
   nslookup -type=MX example.com
   ```

3. **Specificarea unui server DNS pentru interogare:**
   ```csh
   nslookup www.example.com 8.8.8.8
   ```

4. **Obținerea informațiilor despre un nume de domeniu cu un timp de așteptare specificat:**
   ```csh
   nslookup -timeout=5 www.example.com
   ```

## Tips
- Folosiți opțiunea `-type` pentru a obține informații specifice despre diferite tipuri de înregistrări DNS.
- Verificați întotdeauna dacă serverul DNS pe care îl utilizați este disponibil și funcționează corect.
- Utilizați `nslookup` în combinație cu alte comenzi de rețea pentru a diagnostica problemele de conectivitate.