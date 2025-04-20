# [Linux] C Shell (csh) mkdir Użycie: Tworzenie nowych katalogów

## Overview
Polecenie `mkdir` w C Shell (csh) służy do tworzenia nowych katalogów w systemie plików. Umożliwia użytkownikom organizowanie plików w struktury katalogów.

## Usage
Podstawowa składnia polecenia `mkdir` jest następująca:

```csh
mkdir [opcje] [argumenty]
```

## Common Options
- `-p`: Tworzy katalogi nadrzędne w razie potrzeby. Jeśli katalog nadrzędny nie istnieje, zostanie utworzony.
- `-m`: Umożliwia ustawienie uprawnień dla nowego katalogu w formacie oktalnym.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `mkdir`:

1. Tworzenie pojedynczego katalogu:
   ```csh
   mkdir nowy_katalog
   ```

2. Tworzenie wielu katalogów jednocześnie:
   ```csh
   mkdir katalog1 katalog2 katalog3
   ```

3. Tworzenie katalogu z uprawnieniami:
   ```csh
   mkdir -m 755 nowy_katalog
   ```

4. Tworzenie zagnieżdżonych katalogów:
   ```csh
   mkdir -p katalog/nadrzędny/podkatalog
   ```

## Tips
- Zawsze sprawdzaj, czy katalog, który chcesz utworzyć, już istnieje, aby uniknąć błędów.
- Używaj opcji `-p`, gdy tworzysz złożoną strukturę katalogów, aby uprościć proces.
- Pamiętaj o ustawieniu odpowiednich uprawnień, jeśli katalog ma być używany przez innych użytkowników.