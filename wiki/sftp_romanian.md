# [Linux] C Shell (csh) sftp utilizare: Transfer de fișiere securizat

## Overview
Comanda `sftp` (SSH File Transfer Protocol) este utilizată pentru a transfera fișiere între un client și un server printr-o conexiune securizată. Aceasta permite utilizatorilor să se conecteze la un server SSH și să efectueze operațiuni de transfer de fișiere, cum ar fi încărcarea și descărcarea fișierelor.

## Usage
Sintaxa de bază a comenzii `sftp` este următoarea:

```bash
sftp [opțiuni] [utilizator@host]
```

## Common Options
- `-b <file>`: Specifică un fișier de comenzi batch care conține comenzi SFTP.
- `-C`: Activează compresia pentru transferurile de fișiere.
- `-i <file>`: Specifică un fișier de cheie privată pentru autentificare.
- `-P <port>`: Specifică portul pe care se conectează SFTP (implicit este 22).
- `-v`: Activează modul verbose, oferind informații suplimentare despre conexiune.

## Common Examples
### Conectare la un server SFTP
```bash
sftp utilizator@exemplu.com
```

### Descărcarea unui fișier de pe server
```bash
get numefisier.txt
```

### Încărcarea unui fișier pe server
```bash
put numefisier.txt
```

### Descărcarea unui director întreg
```bash
get -r numedirector
```

### Încărcarea unui director întreg
```bash
put -r numedirector
```

### Listarea fișierelor de pe server
```bash
ls
```

## Tips
- Asigurați-vă că aveți permisiunile necesare pentru a accesa fișierele pe server.
- Utilizați opțiunea `-v` pentru a depista problemele de conectare.
- Folosiți comanda `exit` pentru a ieși din sesiunea SFTP în mod corespunzător.