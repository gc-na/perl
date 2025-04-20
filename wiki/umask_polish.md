# [Linux] C Shell (csh) umask użycie: Ustawianie domyślnych uprawnień plików

## Overview
Polecenie `umask` w powłoce C Shell (csh) służy do ustawiania domyślnych uprawnień dla nowych plików i katalogów. Umask określa, które uprawnienia będą usuwane z domyślnych uprawnień, co pozwala na kontrolowanie dostępu do tworzonych zasobów.

## Usage
Podstawowa składnia polecenia `umask` jest następująca:

```csh
umask [opcje] [argumenty]
```

## Common Options
- `-S` - Wyświetla umask w formacie symbolicznym.
- `-p` - Wyświetla aktualną wartość umask bez jej zmiany.

## Common Examples
1. **Sprawdzenie aktualnej wartości umask:**
   ```csh
   umask
   ```

2. **Ustawienie umask na 022 (czyli usunięcie uprawnień do zapisu dla grupy i innych):**
   ```csh
   umask 022
   ```

3. **Ustawienie umask na 007 (czyli usunięcie uprawnień do odczytu i zapisu dla innych):**
   ```csh
   umask 007
   ```

4. **Wyświetlenie umask w formacie symbolicznym:**
   ```csh
   umask -S
   ```

5. **Wyświetlenie aktualnej wartości umask bez jej zmiany:**
   ```csh
   umask -p
   ```

## Tips
- Ustawienie umask na 027 jest często dobrym wyborem dla bezpieczeństwa, ponieważ ogranicza dostęp do plików dla innych użytkowników.
- Pamiętaj, że umask jest stosowany tylko do nowych plików i katalogów, więc nie wpłynie na już istniejące zasoby.
- Możesz dodać polecenie umask do swojego pliku konfiguracyjnego powłoki (np. `.cshrc`), aby automatycznie ustawiać preferowane uprawnienia przy każdym uruchomieniu powłoki.