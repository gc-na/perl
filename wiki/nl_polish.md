# [Linux] C Shell (csh) nl użycie: numerowanie linii w plikach tekstowych

## Overview
Polecenie `nl` w C Shell (csh) służy do numerowania linii w plikach tekstowych. Umożliwia dodanie numerów do każdej linii, co jest przydatne w analizie lub edytowaniu plików.

## Usage
Podstawowa składnia polecenia `nl` jest następująca:

```csh
nl [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `nl`:

- `-b` - Określa, które linie mają być numerowane (np. `-b a` numeruje wszystkie linie).
- `-f` - Umożliwia pominięcie numerowania dla określonych sekcji.
- `-n` - Określa format numeracji (np. `-n ln` dla numeracji z zerami wiodącymi).
- `-w` - Ustala szerokość numerów (np. `-w 3` dla szerokości 3).

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `nl`:

1. Numerowanie wszystkich linii w pliku:
   ```csh
   nl plik.txt
   ```

2. Numerowanie tylko niepustych linii:
   ```csh
   nl -b t plik.txt
   ```

3. Ustawienie szerokości numerów na 5:
   ```csh
   nl -w 5 plik.txt
   ```

4. Numerowanie linii z zerami wiodącymi:
   ```csh
   nl -n ln plik.txt
   ```

## Tips
- Używaj opcji `-b` do precyzyjnego kontrolowania, które linie mają być numerowane, aby uniknąć niepotrzebnego numerowania.
- Eksperymentuj z różnymi opcjami formatowania, aby dostosować wyjście do swoich potrzeb.
- Możesz przekierować wynik do nowego pliku, używając `>`:
  ```csh
  nl plik.txt > numerowany_plik.txt
  ```