# [Linux] C Shell (csh) ulimit użycie: Ustawianie limitów zasobów procesów

## Overview
Polecenie `ulimit` w C Shell (csh) służy do ustawiania lub wyświetlania limitów zasobów dla procesów uruchamianych w danej sesji powłoki. Dzięki temu użytkownicy mogą kontrolować, ile zasobów systemowych mogą wykorzystywać ich procesy, co jest szczególnie przydatne w zarządzaniu wydajnością i bezpieczeństwem systemu.

## Usage
Podstawowa składnia polecenia `ulimit` jest następująca:

```csh
ulimit [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `ulimit`:

- `-a` – Wyświetla wszystkie aktualne limity zasobów.
- `-c [rozmiar]` – Ustawia limit rozmiaru pliku zrzutu pamięci (core dump).
- `-d [rozmiar]` – Ustawia limit rozmiaru pamięci danych.
- `-f [rozmiar]` – Ustawia limit rozmiaru plików, które mogą być tworzone przez proces.
- `-l [rozmiar]` – Ustawia limit rozmiaru pamięci, która może być zablokowana w pamięci fizycznej.
- `-s [rozmiar]` – Ustawia limit rozmiaru stosu dla procesów.

## Common Examples
Poniżej przedstawiono kilka praktycznych przykładów użycia polecenia `ulimit`:

1. Wyświetlenie wszystkich limitów zasobów:
   ```csh
   ulimit -a
   ```

2. Ustawienie limitu rozmiaru pliku zrzutu pamięci na 100 MB:
   ```csh
   ulimit -c 100000
   ```

3. Ustawienie limitu rozmiaru pamięci danych na 512 MB:
   ```csh
   ulimit -d 524288
   ```

4. Ustawienie limitu rozmiaru plików na 1 GB:
   ```csh
   ulimit -f 1048576
   ```

5. Ustawienie limitu rozmiaru stosu na 8 MB:
   ```csh
   ulimit -s 8192
   ```

## Tips
- Zawsze sprawdzaj aktualne limity zasobów przed uruchomieniem zasobożernych procesów, aby uniknąć nieoczekiwanych błędów.
- Ustawianie limitów zasobów może pomóc w zapobieganiu przeciążeniu systemu przez zbyt wiele jednoczesnych procesów.
- Pamiętaj, że zmiany w limitach zasobów są tymczasowe i dotyczą tylko bieżącej sesji powłoki. Aby wprowadzić trwałe zmiany, należy dodać odpowiednie polecenia do pliku konfiguracyjnego powłoki.