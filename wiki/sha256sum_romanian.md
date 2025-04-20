# [Linux] C Shell (csh) sha256sum utilizare: Calculează suma de control SHA-256

## Overview
Comanda `sha256sum` este utilizată pentru a calcula și verifica suma de control SHA-256 a fișierelor. Aceasta este utilă pentru a asigura integritatea datelor, permițând utilizatorilor să compare sumele de control pentru a verifica dacă fișierele au fost modificate.

## Usage
Sintaxa de bază a comenzii `sha256sum` este următoarea:

```shell
sha256sum [opțiuni] [argumente]
```

## Common Options
- `-b`: Citește fișierele în mod binar.
- `-c`: Verifică sumele de control dintr-un fișier.
- `-o`: Specifică un fișier de ieșire pentru rezultatele sumei de control.
- `--help`: Afișează ajutorul pentru utilizare.

## Common Examples
1. Calcularea sumei de control pentru un fișier:
   ```shell
   sha256sum fisier.txt
   ```

2. Salvarea sumei de control într-un fișier:
   ```shell
   sha256sum fisier.txt > suma.txt
   ```

3. Verificarea sumei de control dintr-un fișier:
   ```shell
   sha256sum -c suma.txt
   ```

4. Calcularea sumei de control pentru un fișier în mod binar:
   ```shell
   sha256sum -b fisier.bin
   ```

## Tips
- Asigurați-vă că verificați sumele de control după descărcarea fișierelor importante pentru a confirma integritatea acestora.
- Utilizați opțiunea `-o` pentru a redirecționa ieșirea într-un fișier, astfel încât să păstrați un istoric al sumelor de control.
- Folosiți `--help` pentru a explora toate opțiunile disponibile și a înțelege mai bine funcționalitățile comenzii.