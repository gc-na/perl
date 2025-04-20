# [Linux] Użytkownicy C Shell (csh): wyświetlanie aktywnych użytkowników

## Overview
Polecenie `users` w C Shell (csh) służy do wyświetlania nazw użytkowników, którzy są aktualnie zalogowani na systemie. Jest to przydatne narzędzie do szybkiego sprawdzenia, kto korzysta z systemu w danym momencie.

## Usage
Podstawowa składnia polecenia `users` jest następująca:

```csh
users [options] [arguments]
```

## Common Options
- `-n` : Wyświetla tylko unikalne nazwy użytkowników.
- `-r` : Wyświetla tylko użytkowników, którzy są aktualnie aktywni.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `users`:

1. Wyświetlenie wszystkich aktualnie zalogowanych użytkowników:
   ```csh
   users
   ```

2. Wyświetlenie unikalnych nazw użytkowników:
   ```csh
   users -n
   ```

3. Wyświetlenie tylko aktywnych użytkowników:
   ```csh
   users -r
   ```

## Tips
- Używaj opcji `-n`, aby uniknąć powtarzających się nazw użytkowników, co jest szczególnie przydatne w systemach z wieloma sesjami.
- Regularnie sprawdzaj zalogowanych użytkowników, aby monitorować aktywność w systemie, zwłaszcza na serwerach wielodostępnych.