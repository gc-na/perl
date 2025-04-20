# [Linux] C Shell (csh) dirname utilizare: Extrage calea directorului dintr-un nume de fișier

## Overview
Comanda `dirname` este utilizată pentru a extrage calea directorului dintr-un nume de fișier. Aceasta returnează partea dintr-un path care reprezintă directorul, eliminând numele fișierului.

## Usage
Sintaxa de bază a comenzii `dirname` este următoarea:

```
dirname [opțiuni] [argumente]
```

## Common Options
- **-z**: Afișează rezultatul pe o linie nouă, fără a adăuga un caracter de sfârșit de linie.
- **--help**: Afișează un mesaj de ajutor cu opțiunile disponibile pentru comanda `dirname`.
- **--version**: Afișează informații despre versiunea comenzii.

## Common Examples
1. Extrage calea directorului dintr-un fișier:
    ```csh
    dirname /usr/local/bin/script.sh
    ```
    **Rezultatul:** `/usr/local/bin`

2. Extrage calea directorului dintr-un fișier fără extensie:
    ```csh
    dirname /home/user/document
    ```
    **Rezultatul:** `/home/user`

3. Utilizarea cu un fișier din directorul curent:
    ```csh
    dirname ./file.txt
    ```
    **Rezultatul:** `.`

4. Extrage calea directorului dintr-un fișier cu un path relativ:
    ```csh
    dirname ../images/photo.jpg
    ```
    **Rezultatul:** `.. /images`

## Tips
- Folosește `dirname` în combinație cu alte comenzi, cum ar fi `find`, pentru a procesa mai multe fișiere simultan.
- Verifică întotdeauna calea rezultată pentru a te asigura că este corectă, mai ales când lucrezi cu căi relative.
- Poți utiliza `dirname` în scripturi pentru a gestiona căile fișierelor într-un mod dinamic.