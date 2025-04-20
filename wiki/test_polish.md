# [Linux] C Shell (csh) test użycie: Sprawdzanie warunków

## Overview
Polecenie `test` w powłoce C Shell (csh) służy do oceny warunków i zwraca wartość prawda lub fałsz w zależności od spełnienia określonych kryteriów. Jest to przydatne narzędzie do podejmowania decyzji w skryptach powłoki.

## Usage
Podstawowa składnia polecenia `test` wygląda następująco:

```csh
test [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `test`:

- `-e [plik]`: Sprawdza, czy plik istnieje.
- `-d [katalog]`: Sprawdza, czy ścieżka jest katalogiem.
- `-f [plik]`: Sprawdza, czy ścieżka jest plikiem regularnym.
- `-z [łańcuch]`: Sprawdza, czy długość łańcucha jest równa zeru.
- `-n [łańcuch]`: Sprawdza, czy długość łańcucha jest większa od zera.
- `[argument1] -eq [argument2]`: Sprawdza, czy dwa argumenty są równe (dla liczb).

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `test`:

1. Sprawdzenie, czy plik istnieje:
   ```csh
   if ( `test -e myfile.txt` ) then
       echo "Plik istnieje."
   else
       echo "Plik nie istnieje."
   endif
   ```

2. Sprawdzenie, czy ścieżka jest katalogiem:
   ```csh
   if ( `test -d /home/user` ) then
       echo "To jest katalog."
   else
       echo "To nie jest katalog."
   endif
   ```

3. Sprawdzenie, czy zmienna jest pusta:
   ```csh
   set myvar = ""
   if ( `test -z "$myvar"` ) then
       echo "Zmienna jest pusta."
   endif
   ```

4. Porównanie dwóch liczb:
   ```csh
   set a = 5
   set b = 10
   if ( `test $a -eq $b` ) then
       echo "Liczby są równe."
   else
       echo "Liczby są różne."
   endif
   ```

## Tips
- Używaj polecenia `test` w połączeniu z instrukcją `if`, aby podejmować decyzje w skryptach.
- Pamiętaj o używaniu odpowiednich operatorów porównawczych dla typów danych, aby uniknąć błędów.
- Możesz używać nawiasów do grupowania warunków, co zwiększa czytelność skryptów.