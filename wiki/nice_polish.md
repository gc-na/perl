# [Linux] C Shell (csh) nice użycie: Ustawianie priorytetu procesów

## Overview
Polecenie `nice` w C Shell (csh) służy do uruchamiania procesów z określonym priorytetem. Umożliwia to użytkownikom kontrolowanie, jak wiele zasobów systemowych dany proces może wykorzystać w porównaniu do innych procesów działających w systemie.

## Usage
Podstawowa składnia polecenia `nice` jest następująca:

```
nice [opcje] [argumenty]
```

## Common Options
- `-n [wartość]`: Ustawia wartość priorytetu. Wartość może być dodatnia (zmniejsza priorytet) lub ujemna (zwiększa priorytet).
- `-h`: Wyświetla pomoc dotycząca użycia polecenia.

## Common Examples
1. Uruchomienie programu `my_script.sh` z domyślnym priorytetem:
   ```csh
   nice ./my_script.sh
   ```

2. Uruchomienie programu `my_script.sh` z priorytetem -5:
   ```csh
   nice -n -5 ./my_script.sh
   ```

3. Uruchomienie programu `my_script.sh` z priorytetem 10:
   ```csh
   nice -n 10 ./my_script.sh
   ```

4. Sprawdzenie aktualnego priorytetu procesu:
   ```csh
   ps -o pid,ni,cmd
   ```

## Tips
- Używaj `nice` do uruchamiania procesów, które nie wymagają dużej mocy obliczeniowej, aby nie zakłócać pracy innych użytkowników.
- Zawsze sprawdzaj aktualny priorytet procesów, aby upewnić się, że nie obniżasz wydajności systemu.
- Pamiętaj, że tylko użytkownicy z odpowiednimi uprawnieniami mogą zwiększać priorytet procesów (ustawiać wartość ujemną).