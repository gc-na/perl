# [Linux] C Shell (csh) cmp <Porównaj pliki: porównuje dwa pliki binarnie>

## Overview
Polecenie `cmp` służy do porównywania dwóch plików, aby sprawdzić, czy są one identyczne. Jeśli pliki różnią się, `cmp` wskazuje pierwszą różnicę, co jest przydatne w analizie plików binarnych lub tekstowych.

## Usage
Podstawowa składnia polecenia `cmp` jest następująca:

```csh
cmp [opcje] [argumenty]
```

## Common Options
- `-l`: Wyświetla numery bajtów, w których występują różnice.
- `-s`: Nie wyświetla żadnych informacji, tylko zwraca kod wyjścia, który wskazuje, czy pliki są różne.
- `-i <n>`: Pomija pierwsze `n` bajtów w obu plikach przed porównaniem.
- `-b`: Wyświetla różnice w formacie binarnym.

## Common Examples
- Porównanie dwóch plików tekstowych:

```csh
cmp plik1.txt plik2.txt
```

- Porównanie dwóch plików binarnych z wyświetleniem różnic w formacie binarnym:

```csh
cmp -b plik1.bin plik2.bin
```

- Użycie opcji `-s` do sprawdzenia, czy pliki są identyczne, bez wyświetlania różnic:

```csh
cmp -s plik1.txt plik2.txt
```

- Porównanie plików, pomijając pierwsze 10 bajtów:

```csh
cmp -i 10 plik1.txt plik2.txt
```

- Wyświetlenie numerów bajtów, w których występują różnice:

```csh
cmp -l plik1.txt plik2.txt
```

## Tips
- Używaj opcji `-s`, gdy chcesz szybko sprawdzić, czy pliki są identyczne, bez zbędnych informacji.
- Przy porównywaniu dużych plików binarnych, opcja `-b` może być bardzo pomocna w identyfikacji różnic.
- Pamiętaj, że `cmp` porównuje pliki bajt po bajcie, więc nawet najmniejsza różnica zostanie wykryta.