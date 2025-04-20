# [Linux] C Shell (csh) md5sum utilizare: Calcularea și verificarea sumelor de control MD5

## Overview
Comanda `md5sum` este utilizată pentru a calcula și verifica suma de control MD5 a fișierelor. Aceasta este utilă pentru a asigura integritatea datelor, permițând utilizatorilor să compare sumele de control pentru a verifica dacă fișierele au fost modificate.

## Usage
Sintaxa de bază a comenzii `md5sum` este:

```
md5sum [opțiuni] [argumente]
```

## Common Options
- `-b`: Citește fișiere binare.
- `-c`: Verifică sumele de control dintr-un fișier.
- `-t`: Calculează suma de control pentru intrările standard.
- `--help`: Afișează ajutorul pentru utilizare.
- `--version`: Afișează informații despre versiune.

## Common Examples
1. **Calcularea sumei de control pentru un fișier:**
   ```bash
   md5sum fisier.txt
   ```

2. **Salvarea sumei de control într-un fișier:**
   ```bash
   md5sum fisier.txt > suma.md5
   ```

3. **Verificarea sumei de control dintr-un fișier:**
   ```bash
   md5sum -c suma.md5
   ```

4. **Calcularea sumei de control pentru un fișier binar:**
   ```bash
   md5sum -b fisier.bin
   ```

## Tips
- Asigurați-vă că verificați sumele de control după descărcarea fișierelor importante pentru a confirma integritatea acestora.
- Utilizați opțiunea `-c` pentru a verifica rapid mai multe fișiere cu o singură comandă.
- Păstrați fișierele de sumă de control într-un loc sigur pentru a putea verifica fișierele în viitor.