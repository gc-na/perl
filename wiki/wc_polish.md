# [Linux] C Shell (csh) wc użycie: Zliczanie linii, słów i znaków w plikach

## Overview
Polecenie `wc` (word count) służy do zliczania linii, słów i znaków w plikach tekstowych. Jest to przydatne narzędzie do analizy zawartości plików oraz do szybkiego uzyskiwania informacji o ich wielkości.

## Usage
Podstawowa składnia polecenia `wc` jest następująca:

```csh
wc [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `wc`:

- `-l`: Zlicza tylko linie.
- `-w`: Zlicza tylko słowa.
- `-c`: Zlicza tylko znaki.
- `-m`: Zlicza znaki (w tym znaki multibyte).
- `-L`: Zwraca długość najdłuższej linii.

## Common Examples
Poniżej znajdują się praktyczne przykłady użycia polecenia `wc`:

1. Zliczanie linii, słów i znaków w pliku `plik.txt`:
   ```csh
   wc plik.txt
   ```

2. Zliczanie tylko linii w pliku `plik.txt`:
   ```csh
   wc -l plik.txt
   ```

3. Zliczanie tylko słów w pliku `plik.txt`:
   ```csh
   wc -w plik.txt
   ```

4. Zliczanie tylko znaków w pliku `plik.txt`:
   ```csh
   wc -c plik.txt
   ```

5. Zliczanie długości najdłuższej linii w pliku `plik.txt`:
   ```csh
   wc -L plik.txt
   ```

## Tips
- Używaj opcji `-l` w połączeniu z innymi poleceniami, aby szybko sprawdzić liczbę linii w wynikach, np. `grep`:
  ```csh
  grep "szukany_tekst" plik.txt | wc -l
  ```
- Możesz zliczać wiele plików jednocześnie, podając je jako argumenty:
  ```csh
  wc plik1.txt plik2.txt
  ```
- Aby uzyskać bardziej czytelny wynik, możesz użyć opcji `-h`, aby wyświetlić wyniki w formacie przyjaznym dla użytkownika (dostępne w niektórych systemach Unix).