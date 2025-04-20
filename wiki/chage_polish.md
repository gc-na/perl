# [Linux] C Shell (csh) chage <Użycie: zarządzanie polityką haseł użytkowników>

## Overview
Polecenie `chage` służy do zarządzania polityką haseł użytkowników w systemie Linux. Umożliwia administratorom ustawienie różnych parametrów dotyczących wygasania haseł, takich jak maksymalny czas użytkowania hasła, czas ostrzeżenia przed wygaśnięciem oraz czas, po którym hasło musi zostać zmienione.

## Usage
Podstawowa składnia polecenia `chage` wygląda następująco:

```bash
chage [opcje] [argumenty]
```

## Common Options
- `-l` : Wyświetla informacje o polityce haseł dla określonego użytkownika.
- `-m` : Ustawia minimalny czas (w dniach) przed zmianą hasła.
- `-M` : Ustawia maksymalny czas (w dniach) użytkowania hasła.
- `-I` : Ustawia czas (w dniach) nieaktywności, po którym konto zostanie zablokowane.
- `-E` : Ustawia datę wygaśnięcia konta użytkownika.

## Common Examples
1. **Wyświetlenie polityki haseł dla użytkownika:**
   ```bash
   chage -l nazwa_użytkownika
   ```

2. **Ustawienie minimalnego czasu przed zmianą hasła na 7 dni:**
   ```bash
   chage -m 7 nazwa_użytkownika
   ```

3. **Ustawienie maksymalnego czasu użytkowania hasła na 90 dni:**
   ```bash
   chage -M 90 nazwa_użytkownika
   ```

4. **Ustawienie czasu nieaktywności na 30 dni:**
   ```bash
   chage -I 30 nazwa_użytkownika
   ```

5. **Ustawienie daty wygaśnięcia konta na 1 stycznia 2024:**
   ```bash
   chage -E 2024-01-01 nazwa_użytkownika
   ```

## Tips
- Zawsze sprawdzaj aktualną politykę haseł przed wprowadzeniem zmian, aby uniknąć nieporozumień.
- Używaj opcji `-l`, aby upewnić się, że zmiany zostały poprawnie zastosowane.
- Regularnie przeglądaj polityki haseł, aby dostosować je do wymagań bezpieczeństwa w organizacji.