# [리눅스] C Shell (csh) mkfifo 사용법: FIFO(선입선출) 특수 파일 생성

## Overview
`mkfifo` 명령어는 FIFO(First In, First Out) 특수 파일을 생성하는 데 사용됩니다. FIFO 파일은 프로세스 간의 통신을 위한 일종의 파이프 역할을 하며, 데이터를 순차적으로 읽고 쓸 수 있게 해줍니다.

## Usage
기본 구문은 다음과 같습니다:

```
mkfifo [옵션] [파일 이름]
```

## Common Options
- `-m, --mode`: 생성할 FIFO 파일의 권한을 설정합니다.
- `-Z, --context`: SELinux 보안 컨텍스트를 설정합니다.

## Common Examples
다음은 `mkfifo` 명령어의 몇 가지 일반적인 예입니다.

1. 기본 FIFO 파일 생성:
   ```csh
   mkfifo myfifo
   ```

2. 특정 권한으로 FIFO 파일 생성:
   ```csh
   mkfifo -m 644 myfifo
   ```

3. SELinux 보안 컨텍스트를 설정하여 FIFO 파일 생성:
   ```csh
   mkfifo -Z myfifo
   ```

## Tips
- FIFO 파일을 생성한 후, 다른 프로세스에서 읽기 및 쓰기 작업을 수행할 수 있도록 적절한 권한을 설정하는 것이 좋습니다.
- FIFO 파일은 한 프로세스가 데이터를 쓰고 다른 프로세스가 이를 읽는 구조로 작동하므로, 두 프로세스가 동시에 실행되고 있어야 합니다.
- FIFO 파일을 삭제하려면 `rm` 명령어를 사용하세요.