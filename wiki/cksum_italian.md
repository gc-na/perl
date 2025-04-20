# [Linux] C Shell (csh) cksum: Calcola il checksum di un file

## Overview
Il comando `cksum` in C Shell (csh) calcola e visualizza il checksum di un file, insieme alla sua dimensione in byte. Questo è utile per verificare l'integrità dei dati e per confrontare file.

## Usage
La sintassi di base del comando `cksum` è la seguente:

```csh
cksum [options] [arguments]
```

## Common Options
- `-a` : Specifica l'algoritmo di checksum da utilizzare.
- `-b` : Stampa il checksum in formato binario.
- `-h` : Mostra un messaggio di aiuto con le opzioni disponibili.

## Common Examples
Ecco alcuni esempi pratici di utilizzo del comando `cksum`:

1. Calcolare il checksum di un file:
   ```csh
   cksum file.txt
   ```

2. Calcolare il checksum di più file:
   ```csh
   cksum file1.txt file2.txt
   ```

3. Utilizzare l'opzione `-a` per specificare un algoritmo di checksum:
   ```csh
   cksum -a md5 file.txt
   ```

4. Stampare il checksum in formato binario:
   ```csh
   cksum -b file.txt
   ```

## Tips
- Assicurati di avere i permessi necessari per leggere i file di cui vuoi calcolare il checksum.
- Utilizza `cksum` in combinazione con altri comandi come `diff` per confrontare file e verificare le differenze.
- Salva l'output di `cksum` in un file per un confronto futuro, ad esempio:
  ```csh
  cksum file.txt > checksum.txt
  ```