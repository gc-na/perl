# [Linux] C Shell (csh) sftp użycie: Przesyłanie plików przez SSH

## Overview
Polecenie `sftp` (Secure File Transfer Protocol) służy do bezpiecznego przesyłania plików między komputerami za pomocą protokołu SSH. Umożliwia zarówno przesyłanie plików w górę, jak i w dół, a także zarządzanie plikami na zdalnym serwerze.

## Usage
Podstawowa składnia polecenia `sftp` jest następująca:

```bash
sftp [opcje] [użytkownik@host]
```

## Common Options
- `-P port` - Określa port, na którym nasłuchuje serwer SFTP.
- `-i plik_klucza` - Używa podanego pliku klucza do autoryzacji.
- `-o opcja` - Umożliwia przekazanie dodatkowych opcji do SSH.

## Common Examples
Przykłady użycia polecenia `sftp`:

1. Połączenie z serwerem SFTP:
   ```bash
   sftp user@hostname
   ```

2. Przesyłanie pliku z lokalnego systemu na serwer:
   ```bash
   put lokalny_plik.txt
   ```

3. Pobieranie pliku z serwera na lokalny system:
   ```bash
   get zdalny_plik.txt
   ```

4. Przesyłanie katalogu:
   ```bash
   put -r lokalny_katalog
   ```

5. Wyświetlanie zawartości zdalnego katalogu:
   ```bash
   ls
   ```

## Tips
- Używaj kluczy SSH do autoryzacji, aby zwiększyć bezpieczeństwo i uprościć logowanie.
- Regularnie aktualizuj swoje oprogramowanie SSH, aby korzystać z najnowszych poprawek bezpieczeństwa.
- Zawsze sprawdzaj, czy połączenie jest bezpieczne, zwracając uwagę na komunikaty o błędach lub ostrzeżenia.