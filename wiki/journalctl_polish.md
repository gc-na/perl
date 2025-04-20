# [Linux] C Shell (csh) journalctl użycie: Przeglądanie dzienników systemowych

## Przegląd
Polecenie `journalctl` jest używane do przeglądania dzienników systemowych w systemach opartych na systemd. Umożliwia użytkownikom dostęp do logów, które są zbierane przez systemd-journald, co pozwala na monitorowanie i diagnozowanie problemów w systemie.

## Użycie
Podstawowa składnia polecenia `journalctl` wygląda następująco:

```
journalctl [opcje] [argumenty]
```

## Częste opcje
- `-b` lub `--boot`: Wyświetla logi z bieżącej sesji rozruchowej.
- `-f` lub `--follow`: Śledzi na żywo nowe wpisy w dzienniku.
- `-p` lub `--priority`: Filtruje logi według priorytetu (np. `-p err` wyświetli tylko błędy).
- `--since` i `--until`: Umożliwiają określenie zakresu czasowego dla logów.
- `-u` lub `--unit`: Filtruje logi według jednostki systemd (np. `-u ssh.service`).

## Przykłady
1. Wyświetlenie wszystkich logów:
   ```bash
   journalctl
   ```

2. Wyświetlenie logów z bieżącej sesji rozruchowej:
   ```bash
   journalctl -b
   ```

3. Śledzenie nowych wpisów w dzienniku na żywo:
   ```bash
   journalctl -f
   ```

4. Wyświetlenie logów tylko dla jednostki `ssh.service`:
   ```bash
   journalctl -u ssh.service
   ```

5. Wyświetlenie logów w określonym zakresie czasowym:
   ```bash
   journalctl --since "2023-10-01" --until "2023-10-31"
   ```

## Wskazówki
- Używaj opcji `-p` do szybkiego filtrowania logów według poziomu ważności, co ułatwia diagnozowanie problemów.
- Regularnie przeglądaj logi, aby zidentyfikować potencjalne problemy zanim staną się poważne.
- Możesz używać `grep` w połączeniu z `journalctl`, aby wyszukiwać konkretne frazy w logach, na przykład:
  ```bash
  journalctl | grep "błąd"
  ```