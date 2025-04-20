# [Linux] C Shell (csh) stty użycie: Ustawianie i wyświetlanie opcji terminala

## Overview
Polecenie `stty` w powłoce C Shell (csh) służy do ustawiania i wyświetlania opcji terminala. Umożliwia użytkownikom konfigurowanie zachowania terminala, co może być przydatne w różnych scenariuszach, takich jak zmiana ustawień wejścia/wyjścia lub dostosowywanie sygnałów.

## Usage
Podstawowa składnia polecenia `stty` wygląda następująco:

```bash
stty [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `stty`:

- `-a` - Wyświetla wszystkie ustawienia terminala.
- `-g` - Zapisuje aktualne ustawienia terminala w formacie, który można później przywrócić.
- `erase` - Ustawia znak do usuwania (domyślnie Backspace).
- `kill` - Ustawia znak do usuwania linii (domyślnie Ctrl+U).
- `intr` - Ustawia znak do przerywania (domyślnie Ctrl+C).

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `stty`:

1. Wyświetlenie wszystkich ustawień terminala:

    ```bash
    stty -a
    ```

2. Ustawienie znaku usuwania na Backspace:

    ```bash
    stty erase ^H
    ```

3. Ustawienie znaku do usuwania linii na Ctrl+U:

    ```bash
    stty kill ^U
    ```

4. Zapisanie aktualnych ustawień terminala do pliku:

    ```bash
    stty -g > ustawienia_terminala.txt
    ```

5. Przywrócenie ustawień terminala z pliku:

    ```bash
    stty $(cat ustawienia_terminala.txt)
    ```

## Tips
- Zawsze sprawdzaj aktualne ustawienia terminala przed wprowadzeniem zmian, aby uniknąć niezamierzonych problemów.
- Używaj opcji `-a`, aby szybko zrozumieć, jakie ustawienia są aktualnie aktywne.
- Pamiętaj, że zmiany wprowadzone za pomocą `stty` mogą być tymczasowe i mogą zniknąć po zamknięciu terminala. Aby je zachować, rozważ dodanie polecenia do swojego pliku konfiguracyjnego powłoki.