# [Linux] C Shell (csh) usermod <Użycie: zarządzanie użytkownikami>

## Przegląd
Polecenie `usermod` w systemie C Shell (csh) służy do modyfikacji istniejących kont użytkowników. Umożliwia administratorom systemu aktualizację różnych atrybutów użytkowników, takich jak grupa, hasło czy katalog domowy.

## Użycie
Podstawowa składnia polecenia `usermod` jest następująca:

```csh
usermod [opcje] [argumenty]
```

## Częste opcje
- `-a`: Dodaje użytkownika do nowej grupy bez usuwania go z innych grup.
- `-G`: Umożliwia określenie grup, do których użytkownik ma być dodany.
- `-d`: Zmienia katalog domowy użytkownika.
- `-l`: Zmienia nazwę użytkownika.
- `-p`: Umożliwia ustawienie nowego hasła dla użytkownika.

## Częste przykłady
1. **Dodanie użytkownika do grupy**:
   ```csh
   usermod -a -G developers janek
   ```

2. **Zmiana katalogu domowego użytkownika**:
   ```csh
   usermod -d /home/janek janek
   ```

3. **Zmiana nazwy użytkownika**:
   ```csh
   usermod -l nowa_nazwa janek
   ```

4. **Ustawienie nowego hasła dla użytkownika**:
   ```csh
   usermod -p nowe_haslo janek
   ```

## Wskazówki
- Zawsze wykonuj kopię zapasową danych użytkownika przed wprowadzeniem zmian.
- Używaj opcji `-a` przy dodawaniu użytkowników do grup, aby uniknąć usunięcia ich z istniejących grup.
- Sprawdzaj poprawność wprowadzonych zmian, korzystając z polecenia `id [nazwa_użytkownika]`, aby upewnić się, że użytkownik ma odpowiednie uprawnienia.