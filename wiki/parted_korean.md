# [리눅스] C Shell (csh) parted 사용법: 파티션 관리 도구

## Overview
`parted` 명령어는 디스크 파티션을 관리하는 데 사용되는 도구입니다. 이 명령어를 통해 파티션을 생성, 삭제, 크기 조정 및 포맷할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```
parted [options] [arguments]
```

## Common Options
- `-l` : 현재 시스템의 모든 파티션 테이블을 나열합니다.
- `-s` : 간단 모드로 실행하여 출력 메시지를 최소화합니다.
- `mkpart` : 새로운 파티션을 생성합니다.
- `rm` : 지정된 파티션을 삭제합니다.
- `resizepart` : 기존 파티션의 크기를 조정합니다.

## Common Examples
- 모든 파티션 목록 보기:
  ```bash
  parted -l
  ```

- 새로운 파티션 생성:
  ```bash
  parted /dev/sda mkpart primary ext4 1MiB 100MiB
  ```

- 파티션 삭제:
  ```bash
  parted /dev/sda rm 1
  ```

- 파티션 크기 조정:
  ```bash
  parted /dev/sda resizepart 1 200MiB
  ```

## Tips
- `parted`를 사용할 때는 항상 중요한 데이터를 백업하는 것이 좋습니다.
- 파티션 작업을 수행하기 전에 현재 파티션 상태를 확인하세요.
- `-s` 옵션을 사용하여 스크립트에서 실행할 때 출력 메시지를 줄일 수 있습니다.