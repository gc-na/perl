# [Linux] C Shell (csh) strace utilizare: Urmărirea apelurilor de sistem

## Overview
Comanda `strace` este un instrument puternic utilizat pentru a urmări apelurile de sistem și semnalele primite de un proces. Aceasta permite utilizatorilor să observe interacțiunile dintre un program și nucleul sistemului de operare, fiind extrem de utilă pentru depanare și analiză.

## Usage
Sintaxa de bază a comenzii `strace` este:

```csh
strace [options] [arguments]
```

## Common Options
- `-c`: Afișează statistici despre apelurile de sistem efectuate.
- `-e trace=<set>`: Specifică un set de apeluri de sistem de urmărit.
- `-o <file>`: Redirecționează ieșirea într-un fișier specificat.
- `-p <pid>`: Urmărește un proces existent specificat prin PID.
- `-f`: Urmărește procesele fiu create prin apeluri de sistem.

## Common Examples
1. **Urmărirea unui program simplu**:
   ```csh
   strace ls
   ```
   Aceasta va afișa toate apelurile de sistem efectuate de comanda `ls`.

2. **Redirecționarea ieșirii într-un fișier**:
   ```csh
   strace -o output.txt ls
   ```
   Ieșirea va fi salvată în fișierul `output.txt`.

3. **Urmărirea unui proces existent**:
   ```csh
   strace -p 1234
   ```
   Aceasta va urmări procesul cu PID 1234.

4. **Afișarea statisticilor apelurilor de sistem**:
   ```csh
   strace -c ls
   ```
   Aceasta va oferi un rezumat al apelurilor de sistem efectuate de `ls`.

5. **Urmărirea unui set specific de apeluri de sistem**:
   ```csh
   strace -e trace=open,close ls
   ```
   Aceasta va urmări doar apelurile `open` și `close` efectuate de `ls`.

## Tips
- Utilizați opțiunea `-c` pentru a obține un rezumat rapid al apelurilor de sistem, ceea ce poate ajuta la identificarea problemelor de performanță.
- Redirecționarea ieșirii într-un fișier poate fi utilă pentru analize ulterioare, mai ales când urmăriți aplicații complexe.
- Fiți atenți la permisiunile necesare; unele procese pot necesita privilegii de administrator pentru a fi urmărite.