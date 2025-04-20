# [Linux] C Shell (csh) uniq Uso equivalente: Rimuove le righe duplicate

## Overview
Il comando `uniq` in C Shell (csh) è utilizzato per rimuovere le righe duplicate da un file o da un input standard. Funziona meglio quando le righe duplicate sono adiacenti, quindi è comune utilizzarlo in combinazione con il comando `sort`.

## Usage
La sintassi di base del comando `uniq` è la seguente:

```csh
uniq [options] [arguments]
```

## Common Options
- `-c`: Conta il numero di occorrenze di ogni riga.
- `-d`: Mostra solo le righe duplicate.
- `-u`: Mostra solo le righe uniche.
- `-i`: Ignora la differenza tra maiuscole e minuscole.

## Common Examples

1. Rimuovere righe duplicate da un file:
   ```csh
   uniq file.txt
   ```

2. Ordinare un file e poi rimuovere le righe duplicate:
   ```csh
   sort file.txt | uniq
   ```

3. Contare le righe duplicate:
   ```csh
   uniq -c file.txt
   ```

4. Mostrare solo le righe duplicate:
   ```csh
   uniq -d file.txt
   ```

5. Ignorare la differenza tra maiuscole e minuscole:
   ```csh
   uniq -i file.txt
   ```

## Tips
- Assicurati di ordinare il file prima di utilizzare `uniq` se desideri rimuovere tutte le righe duplicate.
- Usa l'opzione `-c` per avere un'idea di quante volte appare ogni riga nel file.
- Ricorda che `uniq` funziona solo su righe adiacenti, quindi l'ordinamento è spesso un passaggio necessario.