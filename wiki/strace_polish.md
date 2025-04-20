# [Linux] C Shell (csh) strace użycie: Śledzenie wywołań systemowych

## Przegląd
Polecenie `strace` jest narzędziem do śledzenia wywołań systemowych i sygnałów, które są generowane przez procesy w systemie operacyjnym. Umożliwia to programistom i administratorom systemów zrozumienie, jak programy komunikują się z jądrem systemu oraz diagnozowanie problemów.

## Użycie
Podstawowa składnia polecenia `strace` jest następująca:

```csh
strace [opcje] [argumenty]
```

## Częste opcje
- `-c`: Podsumowuje statystyki wywołań systemowych.
- `-e`: Umożliwia filtrowanie wywołań systemowych według określonych kryteriów.
- `-o <plik>`: Zapisuje wyjście śledzenia do wskazanego pliku.
- `-p <pid>`: Śledzi już działający proces o podanym identyfikatorze PID.

## Przykłady
1. Śledzenie wywołań systemowych dla nowego procesu:
   ```csh
   strace ls
   ```

2. Zapisanie wyjścia do pliku:
   ```csh
   strace -o wyjscie.txt ls
   ```

3. Śledzenie konkretnego procesu:
   ```csh
   strace -p 1234
   ```

4. Podsumowanie statystyk wywołań:
   ```csh
   strace -c ls
   ```

5. Filtrowanie wywołań systemowych:
   ```csh
   strace -e trace=open,close ls
   ```

## Wskazówki
- Używaj opcji `-o`, aby zapisać wyniki do pliku, co ułatwia analizę.
- Filtrowanie wywołań za pomocą `-e` może pomóc w skupieniu się na interesujących cię aspektach działania programu.
- Pamiętaj, że `strace` może spowolnić działanie śledzonego procesu, więc używaj go ostrożnie w środowiskach produkcyjnych.