# [Linux] C Shell (csh) df Użycie: Sprawdzanie dostępnej przestrzeni dyskowej

## Overview
Polecenie `df` (disk free) w systemie C Shell (csh) służy do wyświetlania informacji o dostępnej i używanej przestrzeni dyskowej na zamontowanych systemach plików. Dzięki temu użytkownicy mogą szybko ocenić, ile miejsca pozostało na dysku.

## Usage
Podstawowa składnia polecenia `df` jest następująca:

```csh
df [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `df`:

- `-h` - Wyświetla rozmiary w formacie czytelnym dla ludzi (np. KB, MB, GB).
- `-T` - Wyświetla typy systemów plików.
- `-a` - Wyświetla wszystkie systemy plików, w tym te, które mają 0 bajtów.
- `-i` - Wyświetla informacje o inode'ach zamiast o przestrzeni dyskowej.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `df`:

1. Wyświetlenie dostępnej przestrzeni dyskowej w formacie czytelnym dla ludzi:
   ```csh
   df -h
   ```

2. Wyświetlenie typów systemów plików:
   ```csh
   df -T
   ```

3. Wyświetlenie informacji o wszystkich systemach plików, w tym tych z zerową przestrzenią:
   ```csh
   df -a
   ```

4. Wyświetlenie informacji o inode'ach:
   ```csh
   df -i
   ```

## Tips
- Regularnie sprawdzaj dostępność przestrzeni dyskowej, aby uniknąć problemów z brakiem miejsca na dysku.
- Użyj opcji `-h` w codziennym użytkowaniu, aby łatwiej interpretować wyniki.
- Możesz łączyć różne opcje, na przykład `df -hT`, aby uzyskać więcej informacji w przystępnej formie.