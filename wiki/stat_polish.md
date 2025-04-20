# [Linux] C Shell (csh) stat <Użycie: wyświetlanie informacji o plikach>

## Przegląd
Polecenie `stat` w C Shell (csh) służy do wyświetlania szczegółowych informacji o plikach i katalogach. Umożliwia użytkownikom uzyskanie danych takich jak rozmiar pliku, daty modyfikacji oraz uprawnienia.

## Użycie
Podstawowa składnia polecenia `stat` jest następująca:

```csh
stat [opcje] [argumenty]
```

## Częste opcje
- `-c` : Umożliwia formatowanie wyjścia według podanego wzoru.
- `-f` : Wyświetla informacje o systemie plików.
- `-L` : Śledzi dowiązania symboliczne i wyświetla informacje o pliku, do którego prowadzą.

## Przykłady
1. Aby wyświetlić podstawowe informacje o pliku:
   ```csh
   stat myfile.txt
   ```

2. Aby uzyskać szczegółowe informacje w formacie dostosowanym:
   ```csh
   stat -c '%n: %s bytes, modified %y' myfile.txt
   ```

3. Aby wyświetlić informacje o katalogu:
   ```csh
   stat /home/user/
   ```

4. Aby śledzić dowiązania symboliczne:
   ```csh
   stat -L symlink.txt
   ```

## Wskazówki
- Używaj opcji `-c` do dostosowywania wyjścia, co może być przydatne w skryptach.
- Sprawdzaj uprawnienia plików, aby upewnić się, że masz odpowiednie dostępy przed ich edytowaniem.
- Pamiętaj, że `stat` może być użyteczne w diagnostyce problemów z plikami i systemem plików.