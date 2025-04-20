# [Linux] C Shell (csh) foreach użycie: Iteracja przez elementy listy

## Overview
Polecenie `foreach` w C Shell (csh) służy do iteracji przez elementy listy. Umożliwia wykonywanie zestawu poleceń dla każdego elementu w podanej liście, co jest przydatne w automatyzacji zadań.

## Usage
Podstawowa składnia polecenia `foreach` wygląda następująco:

```csh
foreach variable (list)
    commands
end
```

## Common Options
Polecenie `foreach` nie ma wielu opcji, ale oto kilka, które mogą być przydatne:

- `variable`: Zmienna, która przyjmuje wartość każdego elementu listy w kolejnych iteracjach.
- `list`: Lista elementów, przez które chcemy iterować.
- `commands`: Zestaw poleceń, które mają być wykonane dla każdego elementu listy.

## Common Examples

### Przykład 1: Iteracja przez liczby
```csh
foreach i (1 2 3 4 5)
    echo "Liczba: $i"
end
```
Ten przykład wypisuje liczby od 1 do 5.

### Przykład 2: Iteracja przez pliki
```csh
foreach file (*.txt)
    echo "Znaleziony plik: $file"
end
```
W tym przykładzie polecenie wypisuje wszystkie pliki z rozszerzeniem `.txt` w bieżącym katalogu.

### Przykład 3: Wykonywanie polecenia na każdym pliku
```csh
foreach file (*.log)
    gzip $file
end
```
Tutaj każde wystąpienie pliku `.log` jest kompresowane za pomocą `gzip`.

## Tips
- Używaj `echo` do debugowania, aby zobaczyć, jakie wartości są przypisywane do zmiennej w każdej iteracji.
- Upewnij się, że lista nie jest pusta, aby uniknąć błędów podczas wykonywania poleceń.
- Możesz zagnieżdżać polecenia `foreach`, aby iterować przez złożone struktury danych.