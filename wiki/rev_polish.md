# [Linux] C Shell (csh) rev: odwracanie tekstu

## Overview
Polecenie `rev` służy do odwracania kolejności znaków w każdej linii pliku lub tekstu. Jest to przydatne narzędzie, gdy potrzebujemy szybko zobaczyć, jak wygląda tekst w odwrotnej formie.

## Usage
Podstawowa składnia polecenia `rev` jest następująca:

```csh
rev [opcje] [argumenty]
```

## Common Options
- `-o, --output=FILE` - Zapisuje wynik do wskazanego pliku zamiast wyświetlać go na standardowym wyjściu.
- `-h, --help` - Wyświetla pomoc dotyczącą użycia polecenia.
- `-V, --version` - Wyświetla wersję polecenia.

## Common Examples
1. Odwrócenie tekstu w pliku:
   ```csh
   rev plik.txt
   ```

2. Odwrócenie tekstu wprowadzoną z klawiatury:
   ```csh
   echo "Przykładowy tekst" | rev
   ```

3. Zapisanie odwróconego tekstu do nowego pliku:
   ```csh
   rev plik.txt -o odwrócony_plik.txt
   ```

4. Odwrócenie tekstu z wielu linii:
   ```csh
   cat wiele_linii.txt | rev
   ```

## Tips
- Używaj opcji `-o`, aby łatwo zapisać wynik do pliku, co jest przydatne, gdy pracujesz z dużymi zbiorami danych.
- Możesz łączyć `rev` z innymi poleceniami, takimi jak `grep` lub `sort`, aby uzyskać bardziej złożone operacje na tekście.
- Pamiętaj, że `rev` działa na poziomie linii, więc każda linia w pliku będzie odwrócona niezależnie.