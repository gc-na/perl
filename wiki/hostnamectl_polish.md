# [Linux] C Shell (csh) hostnamectl Użycie: zarządzanie nazwą hosta i informacjami o systemie

## Overview
Polecenie `hostnamectl` służy do zarządzania nazwą hosta oraz wyświetlania informacji o systemie operacyjnym. Umożliwia użytkownikom łatwe modyfikowanie nazwy hosta oraz uzyskiwanie szczegółowych informacji o systemie.

## Usage
Podstawowa składnia polecenia `hostnamectl` jest następująca:

```
hostnamectl [opcje] [argumenty]
```

## Common Options
- `set-hostname`: Umożliwia ustawienie nowej nazwy hosta.
- `status`: Wyświetla aktualny status systemu, w tym nazwę hosta.
- `set-icon-name`: Umożliwia ustawienie ikony systemu.
- `set-chassis`: Umożliwia określenie typu obudowy systemu (np. desktop, laptop).

## Common Examples
1. **Wyświetlenie aktualnej nazwy hosta:**
   ```csh
   hostnamectl status
   ```

2. **Ustawienie nowej nazwy hosta:**
   ```csh
   hostnamectl set-hostname nowa-nazwa-host
   ```

3. **Ustawienie ikony systemu:**
   ```csh
   hostnamectl set-icon-name ikona-systemu
   ```

4. **Określenie typu obudowy:**
   ```csh
   hostnamectl set-chassis laptop
   ```

## Tips
- Upewnij się, że masz odpowiednie uprawnienia (np. administratora), aby zmieniać nazwę hosta.
- Po zmianie nazwy hosta, może być konieczne ponowne uruchomienie systemu, aby zmiany zaczęły obowiązywać.
- Regularnie sprawdzaj status systemu, aby upewnić się, że wszystkie ustawienia są poprawne.