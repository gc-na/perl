# [Linux] C Shell (csh) psql utilizare: interacțiune cu baza de date PostgreSQL

## Overview
Comanda `psql` este un client de linie de comandă pentru PostgreSQL, care permite utilizatorilor să interacționeze cu baza de date. Aceasta oferă o interfață pentru a rula comenzi SQL, a gestiona baze de date și a efectua diverse operațiuni administrative.

## Usage
Sintaxa de bază a comenzii `psql` este următoarea:

```bash
psql [opțiuni] [argumente]
```

## Common Options
- `-h`: Specifică gazda serverului PostgreSQL.
- `-p`: Specifică portul pe care serverul PostgreSQL ascultă.
- `-U`: Specifică utilizatorul care se conectează la baza de date.
- `-d`: Specifică numele bazei de date la care se conectează.
- `-c`: Execută o comandă SQL specificată și apoi iese.

## Common Examples
1. Conectare la o bază de date specifică:
   ```bash
   psql -U utilizator -d nume_baza_de_date
   ```

2. Executarea unei comenzi SQL direct din linia de comandă:
   ```bash
   psql -U utilizator -d nume_baza_de_date -c "SELECT * FROM tabela;"
   ```

3. Conectare la un server PostgreSQL pe o gazdă specifică:
   ```bash
   psql -h gazda -U utilizator -d nume_baza_de_date
   ```

4. Listarea tuturor bazelor de date disponibile:
   ```bash
   psql -U utilizator -l
   ```

## Tips
- Asigurați-vă că aveți permisiunile necesare pentru a accesa baza de date.
- Utilizați opțiunea `-W` pentru a solicita parola utilizatorului la conectare.
- Folosiți comanda `\?` în interiorul psql pentru a obține ajutor despre comenzile disponibile.