# [Linux] C Shell (csh) fdisk użycie: zarządzanie partycjami dysku

## Overview
Polecenie `fdisk` służy do zarządzania partycjami dysku w systemach operacyjnych opartych na Uniksie. Umożliwia tworzenie, usuwanie i modyfikowanie partycji, co jest niezbędne do efektywnego zarządzania przestrzenią dyskową.

## Usage
Podstawowa składnia polecenia `fdisk` jest następująca:

```
fdisk [opcje] [argumenty]
```

## Common Options
- `-l` - Wyświetla listę dostępnych dysków i ich partycji.
- `-u` - Używa jednostek cylindrów do wyświetlania informacji o partycjach.
- `-n` - Tworzy nową partycję.
- `-d` - Usuwa istniejącą partycję.
- `-p` - Wyświetla tabelę partycji.

## Common Examples
1. **Wyświetlenie listy partycji**:
   ```bash
   fdisk -l
   ```

2. **Tworzenie nowej partycji**:
   ```bash
   fdisk /dev/sda
   ```
   Następnie w interaktywnym menu wybierz opcję `n`, aby dodać nową partycję.

3. **Usuwanie partycji**:
   ```bash
   fdisk /dev/sda
   ```
   W interaktywnym menu wybierz opcję `d`, aby usunąć partycję.

4. **Wyświetlenie tabeli partycji**:
   ```bash
   fdisk -p /dev/sda
   ```

## Tips
- Zawsze wykonuj kopię zapasową danych przed modyfikowaniem partycji.
- Używaj opcji `-l` przed wprowadzeniem zmian, aby upewnić się, że znasz aktualny stan partycji.
- Pracuj z `fdisk` jako użytkownik z uprawnieniami administratora, aby uniknąć problemów z dostępem.