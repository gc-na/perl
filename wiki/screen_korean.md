# [리눅스] C Shell (csh) screen 사용법: 터미널 세션 관리

## Overview
`screen` 명령어는 여러 개의 터미널 세션을 관리하고, 세션을 분리하거나 재연결할 수 있게 해주는 유틸리티입니다. 이를 통해 사용자는 원격 서버에서 작업을 지속적으로 수행할 수 있으며, 네트워크 연결이 끊어져도 작업이 중단되지 않습니다.

## Usage
기본 구문은 다음과 같습니다:

```csh
screen [options] [arguments]
```

## Common Options
- `-S [session_name]`: 세션에 이름을 지정합니다.
- `-d -r`: 분리된 세션을 재연결합니다.
- `-list`: 현재 실행 중인 세션 목록을 표시합니다.
- `-L`: 세션의 출력을 로그 파일에 저장합니다.

## Common Examples
- 새로운 세션 시작하기:
    ```csh
    screen -S mysession
    ```

- 분리된 세션 목록 보기:
    ```csh
    screen -list
    ```

- 분리된 세션 재연결하기:
    ```csh
    screen -d -r mysession
    ```

- 세션 로그 저장하기:
    ```csh
    screen -L -S mysession
    ```

## Tips
- 세션 이름을 지정하면 여러 세션을 쉽게 관리할 수 있습니다.
- `Ctrl-a` 키를 누른 후 `d`를 눌러 세션을 분리할 수 있습니다.
- 세션을 종료하려면 `exit` 명령어를 입력하거나 `Ctrl-a` 후 `k`를 눌러 세션을 종료할 수 있습니다.