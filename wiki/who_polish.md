# [Linux] C Shell (csh) who użycie: wyświetla zalogowanych użytkowników

## Overview
Polecenie `who` w C Shell (csh) służy do wyświetlania listy użytkowników aktualnie zalogowanych do systemu. Informacje te mogą być przydatne do monitorowania aktywności użytkowników oraz do zarządzania sesjami.

## Usage
Podstawowa składnia polecenia `who` jest następująca:

```
who [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `who`:

- `-b` - wyświetla czas ostatniego uruchomienia systemu.
- `-q` - pokazuje tylko zalogowanych użytkowników oraz ich liczbę.
- `-H` - wyświetla nagłówki kolumn w wynikach.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `who`:

1. Wyświetlenie wszystkich zalogowanych użytkowników:
   ```csh
   who
   ```

2. Wyświetlenie czasu ostatniego uruchomienia systemu:
   ```csh
   who -b
   ```

3. Wyświetlenie tylko liczby zalogowanych użytkowników:
   ```csh
   who -q
   ```

4. Wyświetlenie z nagłówkami kolumn:
   ```csh
   who -H
   ```

## Tips
- Używaj opcji `-q`, aby szybko sprawdzić, ilu użytkowników jest aktualnie zalogowanych, co może być przydatne w dużych systemach.
- Regularnie sprawdzaj, kto jest zalogowany, aby monitorować bezpieczeństwo i aktywność w systemie.
- Połącz polecenie `who` z innymi narzędziami, takimi jak `grep`, aby filtrować wyniki według konkretnego użytkownika.