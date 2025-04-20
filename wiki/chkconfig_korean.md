# [리눅스] C Shell (csh) chkconfig 사용법: 서비스 관리 명령어

## Overview
`chkconfig` 명령어는 리눅스 시스템에서 서비스의 시작 및 중지를 관리하는 데 사용됩니다. 이 명령어를 통해 시스템 부팅 시 자동으로 시작할 서비스와 그렇지 않은 서비스를 설정할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
chkconfig [options] [arguments]
```

## Common Options
- `--list`: 현재 설정된 모든 서비스의 상태를 나열합니다.
- `--add`: 새로운 서비스를 추가합니다.
- `--del`: 기존 서비스를 삭제합니다.
- `--level`: 특정 런레벨에서 서비스의 시작 여부를 설정합니다.
- `--on`: 서비스를 시작하도록 설정합니다.
- `--off`: 서비스를 중지하도록 설정합니다.

## Common Examples
- 현재 설정된 서비스 목록 보기:
  ```bash
  chkconfig --list
  ```

- 새로운 서비스 추가:
  ```bash
  chkconfig --add myservice
  ```

- 서비스 삭제:
  ```bash
  chkconfig --del myservice
  ```

- 특정 런레벨에서 서비스 시작 설정:
  ```bash
  chkconfig --level 2345 myservice on
  ```

- 서비스 중지 설정:
  ```bash
  chkconfig --level 2345 myservice off
  ```

## Tips
- 서비스의 상태를 변경하기 전에 항상 현재 상태를 확인하는 것이 좋습니다.
- 런레벨에 대한 이해가 필요하며, 각 런레벨이 무엇을 의미하는지 숙지해야 합니다.
- 시스템 부팅 시 자동으로 시작해야 하는 서비스만 `on`으로 설정하세요.