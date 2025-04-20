# [리눅스] C Shell (csh) tmux 사용법: 터미널 멀티플렉서

## Overview
tmux는 터미널 멀티플렉서로, 하나의 터미널 세션에서 여러 개의 세션을 관리할 수 있도록 도와줍니다. 이를 통해 사용자는 여러 작업을 동시에 수행하고, 세션을 분리하거나 재연결할 수 있습니다.

## Usage
tmux의 기본 구문은 다음과 같습니다:

```bash
tmux [options] [arguments]
```

## Common Options
- `new`: 새로운 tmux 세션을 생성합니다.
- `attach`: 기존 세션에 연결합니다.
- `detach`: 현재 세션에서 분리합니다.
- `list-sessions`: 현재 실행 중인 세션 목록을 보여줍니다.
- `kill-session`: 지정한 세션을 종료합니다.

## Common Examples
- 새로운 tmux 세션 시작하기:
    ```bash
    tmux new -s mysession
    ```
- 기존 세션에 연결하기:
    ```bash
    tmux attach -t mysession
    ```
- 현재 세션에서 분리하기:
    ```bash
    Ctrl-b d
    ```
- 실행 중인 세션 목록 보기:
    ```bash
    tmux list-sessions
    ```
- 특정 세션 종료하기:
    ```bash
    tmux kill-session -t mysession
    ```

## Tips
- tmux에서 세션을 분리할 때는 `Ctrl-b d`를 사용하여 쉽게 분리할 수 있습니다.
- 세션 이름을 지정하면 여러 세션을 관리하기가 수월합니다.
- tmux의 설정 파일(`~/.tmux.conf`)을 활용하여 개인화된 단축키와 설정을 추가할 수 있습니다.