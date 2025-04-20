# [Systemy Unixowe] C Shell (csh) 7z użycie: Kompresja i dekompresja plików

## Przegląd
Polecenie `7z` jest częścią programu 7-Zip, który służy do kompresji i dekompresji plików. Obsługuje wiele formatów archiwów, w tym 7z, ZIP, RAR i inne, co czyni go wszechstronnym narzędziem do zarządzania plikami.

## Użycie
Podstawowa składnia polecenia `7z` jest następująca:

```
7z [opcje] [argumenty]
```

## Częste opcje
- `a` - dodaje pliki do archiwum.
- `x` - wypakowuje pliki z archiwum.
- `t` - testuje archiwum.
- `l` - wyświetla zawartość archiwum.
- `d` - usuwa pliki z archiwum.

## Częste przykłady
1. **Tworzenie archiwum 7z:**
   ```csh
   7z a archiwum.7z plik1.txt plik2.txt
   ```

2. **Wypakowywanie archiwum 7z:**
   ```csh
   7z x archiwum.7z
   ```

3. **Testowanie archiwum:**
   ```csh
   7z t archiwum.7z
   ```

4. **Wyświetlanie zawartości archiwum:**
   ```csh
   7z l archiwum.7z
   ```

5. **Usuwanie pliku z archiwum:**
   ```csh
   7z d archiwum.7z plik1.txt
   ```

## Wskazówki
- Zawsze sprawdzaj integralność archiwum za pomocą opcji `t` przed jego użyciem.
- Używaj opcji `-p` do zabezpieczenia archiwum hasłem, aby chronić swoje dane.
- Regularnie aktualizuj 7-Zip, aby korzystać z najnowszych funkcji i poprawek bezpieczeństwa.