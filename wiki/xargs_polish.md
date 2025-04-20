# [Linux] C Shell (csh) xargs użycie: Przekazywanie argumentów do poleceń

## Overview
Polecenie `xargs` w powłoce C Shell (csh) służy do przekształcania wejścia standardowego w argumenty dla innych poleceń. Umożliwia to efektywne przetwarzanie dużych zbiorów danych, które mogą być przekazywane do poleceń w systemie.

## Usage
Podstawowa składnia polecenia `xargs` jest następująca:

```csh
xargs [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla `xargs`:

- `-n N` - Przekazuje maksymalnie N argumentów do polecenia.
- `-d DELIM` - Używa określonego znaku jako delimitera dla argumentów.
- `-p` - Pyta użytkownika przed wykonaniem każdego polecenia.
- `-0` - Oczekuje, że wejście będzie zakończone znakiem null, co jest przydatne w przypadku plików z białymi znakami.

## Common Examples
Oto kilka praktycznych przykładów użycia `xargs`:

1. **Usuwanie plików**:
   Aby usunąć pliki, których nazwy są przekazywane przez `find`:
   ```csh
   find . -name '*.tmp' | xargs rm
   ```

2. **Zliczanie linii w plikach**:
   Zliczanie linii w plikach tekstowych:
   ```csh
   ls *.txt | xargs wc -l
   ```

3. **Kopiowanie plików**:
   Kopiowanie plików do innego katalogu:
   ```csh
   find . -name '*.jpg' | xargs -I {} cp {} /path/to/destination/
   ```

4. **Przekazywanie argumentów z delimitatorem**:
   Użycie niestandardowego delimitera:
   ```csh
   echo "file1.txt,file2.txt,file3.txt" | xargs -d ',' cp -t /path/to/destination/
   ```

## Tips
- Używaj opcji `-n` dla lepszej kontroli nad liczbą argumentów przekazywanych do polecenia, co może być przydatne w przypadku poleceń, które mają ograniczenia na liczbę argumentów.
- Zawsze sprawdzaj, co zostanie wykonane, używając opcji `-p`, aby uniknąć niezamierzonych działań.
- W przypadku plików z białymi znakami lub nowymi liniami, rozważ użycie opcji `-0` w połączeniu z `find` z opcją `-print0`, aby poprawnie przetwarzać nazwy plików.