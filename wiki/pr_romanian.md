# [Linux] C Shell (csh) pr: Afișează fișierele text în format paginat

## Overview
Comanda `pr` este utilizată pentru a formata fișierele text, împărțindu-le în pagini și adăugând antete, astfel încât să fie mai ușor de citit. Aceasta este utilă în special pentru a pregăti documente pentru imprimare.

## Usage
Sintaxa de bază a comenzii `pr` este următoarea:

```
pr [options] [arguments]
```

## Common Options
- `-h` : Specifică un antet personalizat pentru fiecare pagină.
- `-l` : Setează numărul de linii pe pagină.
- `-w` : Definește lățimea paginii în caractere.
- `-t` : Elimină antetele și numerele de pagină.

## Common Examples
1. **Formatarea unui fișier text simplu:**
   ```csh
   pr fisier.txt
   ```

2. **Setarea unui antet personalizat:**
   ```csh
   pr -h "Antet Personalizat" fisier.txt
   ```

3. **Modificarea numărului de linii pe pagină:**
   ```csh
   pr -l 40 fisier.txt
   ```

4. **Eliminarea antetelor și numerelor de pagină:**
   ```csh
   pr -t fisier.txt
   ```

5. **Formatarea mai multor fișiere simultan:**
   ```csh
   pr fisier1.txt fisier2.txt
   ```

## Tips
- Folosește opțiunea `-w` pentru a ajusta lățimea paginii în funcție de formatul imprimantei tale.
- Verifică întotdeauna cum arată documentul formatat înainte de a-l imprima, pentru a evita risipa de hârtie.
- Combină `pr` cu alte comenzi, cum ar fi `cat`, pentru a vizualiza rapid conținutul mai multor fișiere.