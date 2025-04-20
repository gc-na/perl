# [Linux] C Shell (csh) tmux użycie: Narzędzie do zarządzania sesjami terminalowymi

## Overview
tmux to terminal multiplexer, który pozwala na uruchamianie wielu sesji terminalowych w jednym oknie. Umożliwia użytkownikom podział ekranu, przełączanie się między sesjami oraz odłączanie i ponowne łączenie się z sesjami, co jest szczególnie przydatne w pracy zdalnej.

## Usage
Podstawowa składnia polecenia tmux jest następująca:

```bash
tmux [opcje] [argumenty]
```

## Common Options
- `new`: Tworzy nową sesję tmux.
- `attach`: Dołącza do istniejącej sesji.
- `detach`: Odłącza bieżącą sesję.
- `list-sessions`: Wyświetla listę aktywnych sesji.
- `kill-session`: Zamyka wskazaną sesję.

## Common Examples
- Aby utworzyć nową sesję tmux:
  ```bash
  tmux new -s moja_sesja
  ```

- Aby dołączyć do istniejącej sesji:
  ```bash
  tmux attach -t moja_sesja
  ```

- Aby odłączyć się od bieżącej sesji, można użyć kombinacji klawiszy:
  ```bash
  Ctrl + b, a następnie d
  ```

- Aby zobaczyć listę aktywnych sesji:
  ```bash
  tmux list-sessions
  ```

- Aby zamknąć sesję:
  ```bash
  tmux kill-session -t moja_sesja
  ```

## Tips
- Używaj nazw sesji, które są łatwe do zapamiętania, aby szybko się do nich odnosić.
- Korzystaj z podziału okna (split window) w tmux, aby pracować nad wieloma zadaniami jednocześnie.
- Regularnie zapisuj swoje sesje, aby uniknąć utraty postępu w pracy.