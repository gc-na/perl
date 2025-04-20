# [Linux] C Shell (csh) bzip2 Utilizare: Compresia fișierelor

## Overview
Comanda `bzip2` este utilizată pentru a comprima fișiere, reducându-le dimensiunea pentru a economisi spațiu de stocare. Aceasta folosește algoritmi avansați de compresie, oferind un raport de compresie mai bun decât alte metode, cum ar fi `gzip`.

## Usage
Sintaxa de bază a comenzii `bzip2` este următoarea:

```csh
bzip2 [options] [arguments]
```

## Common Options
- `-d`, `--decompress`: Decomprimați un fișier comprimat.
- `-k`, `--keep`: Păstrează fișierul original după comprimare.
- `-f`, `--force`: Forțează comprimarea, suprascriind fișierele existente.
- `-v`, `--verbose`: Afișează informații detaliate despre procesul de compresie.
- `-z`, `--compress`: Comprimă fișierul (aceasta este opțiunea implicită).

## Common Examples
1. **Comprimarea unui fișier:**
   ```csh
   bzip2 fisier.txt
   ```
   Acest lucru va crea un fișier comprimat numit `fisier.txt.bz2`.

2. **Decomprimarea unui fișier:**
   ```csh
   bzip2 -d fisier.txt.bz2
   ```
   Aceasta va restaura fișierul original `fisier.txt`.

3. **Comprimarea și păstrarea fișierului original:**
   ```csh
   bzip2 -k fisier.txt
   ```
   Fișierul `fisier.txt` va fi comprimat, dar va rămâne și versiunea originală.

4. **Afișarea detaliilor în timpul comprimării:**
   ```csh
   bzip2 -v fisier.txt
   ```
   Aceasta va afișa informații despre progresul comprimării.

## Tips
- Folosiți opțiunea `-k` dacă doriți să păstrați fișierul original după comprimare.
- Verificați dimensiunea fișierului comprimat pentru a evalua eficiența compresiei.
- Fiți atenți la utilizarea opțiunii `-f`, deoarece aceasta poate suprascrie fișierele existente fără avertisment.