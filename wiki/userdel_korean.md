# [리눅스] C Shell (csh) userdel 사용법: 사용자 계정 삭제

## Overview
`userdel` 명령은 시스템에서 사용자 계정을 삭제하는 데 사용됩니다. 이 명령을 사용하면 특정 사용자의 모든 정보와 관련된 파일을 제거할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:

```
userdel [options] [arguments]
```

## Common Options
- `-r`: 사용자의 홈 디렉토리와 메일 스풀을 함께 삭제합니다.
- `-f`: 사용자가 로그인 중일 때도 강제로 삭제합니다.
- `-Z`: SELinux 사용자 맵을 함께 삭제합니다.

## Common Examples
사용자 계정을 삭제하는 몇 가지 예시는 다음과 같습니다:

1. 기본 사용자 삭제:
   ```shell
   userdel username
   ```

2. 사용자와 그 홈 디렉토리 삭제:
   ```shell
   userdel -r username
   ```

3. 로그인 중인 사용자 강제 삭제:
   ```shell
   userdel -f username
   ```

4. SELinux 사용자 맵과 함께 삭제:
   ```shell
   userdel -Z username
   ```

## Tips
- 사용자 계정을 삭제하기 전에 해당 사용자의 데이터 백업을 고려하세요.
- `-r` 옵션을 사용할 때는 주의해야 하며, 삭제된 데이터는 복구할 수 없습니다.
- 시스템 관리자 권한이 필요하므로, `sudo` 명령과 함께 사용하는 것이 좋습니다.