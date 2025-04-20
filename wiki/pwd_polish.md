# [Linux] C Shell (csh) pwd użycie: Wyświetla bieżący katalog roboczy

## Overview
Polecenie `pwd` (print working directory) w C Shell (csh) służy do wyświetlania pełnej ścieżki do bieżącego katalogu roboczego. Jest to przydatne, gdy chcesz szybko sprawdzić, w którym katalogu aktualnie się znajdujesz.

## Usage
Podstawowa składnia polecenia `pwd` jest następująca:

```
pwd [opcje]
```

## Common Options
- `-L` - Wyświetla ścieżkę do katalogu roboczego, używając symbolicznych linków.
- `-P` - Wyświetla rzeczywistą ścieżkę do katalogu roboczego, ignorując symboliczne linki.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `pwd`:

1. Wyświetlenie bieżącego katalogu roboczego:
   ```csh
   pwd
   ```

2. Wyświetlenie rzeczywistej ścieżki do katalogu roboczego (ignorując linki symboliczne):
   ```csh
   pwd -P
   ```

3. Wyświetlenie ścieżki do katalogu roboczego z użyciem linków symbolicznych:
   ```csh
   pwd -L
   ```

## Tips
- Używaj `pwd` przed wykonywaniem poleceń zmiany katalogu, aby upewnić się, że wiesz, gdzie się znajdujesz.
- Warto łączyć `pwd` z innymi poleceniami, aby uzyskać pełny kontekst operacji w skryptach powłoki.