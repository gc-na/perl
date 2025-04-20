# [Linux] C Shell (csh) mysql utilizare: Interacțiune cu baza de date MySQL

## Overview
Comanda `mysql` este un client de linie de comandă utilizat pentru a interacționa cu serverul de baze de date MySQL. Aceasta permite utilizatorilor să execute interogări SQL, să gestioneze baze de date și să efectueze diverse operațiuni asupra datelor stocate.

## Usage
Sintaxa de bază a comenzii `mysql` este următoarea:

```bash
mysql [opțiuni] [argumente]
```

## Common Options
Iată câteva opțiuni comune pentru comanda `mysql`:

- `-u [utilizator]`: Specifică numele utilizatorului pentru autentificare.
- `-p`: Solicită parola utilizatorului.
- `-h [host]`: Specifică gazda serverului MySQL (implicit este localhost).
- `-D [bază_de_date]`: Selectează baza de date implicită la conectare.
- `--execute=[comandă]`: Execută o comandă SQL specificată.

## Common Examples
Iată câteva exemple practice de utilizare a comenzii `mysql`:

1. Conectarea la serverul MySQL cu un utilizator specific:
   ```bash
   mysql -u root -p
   ```

2. Conectarea la un server MySQL pe un host specific:
   ```bash
   mysql -h 192.168.1.100 -u utilizator -p
   ```

3. Executarea unei comenzi SQL direct din linia de comandă:
   ```bash
   mysql -u utilizator -p -e "SHOW DATABASES;"
   ```

4. Selectarea unei baze de date și executarea unei interogări:
   ```bash
   mysql -u utilizator -p -D nume_baza_de_date -e "SELECT * FROM tabela;"
   ```

## Tips
- Asigurați-vă că aveți permisiuni corespunzătoare pentru a accesa baza de date.
- Utilizați opțiunea `-D` pentru a evita scrierea comenzii `USE` de fiecare dată când doriți să lucrați cu o bază de date specifică.
- Păstrați parolele în siguranță și evitați să le introduceți direct în linia de comandă pentru a preveni expunerea acestora.