# [리눅스] C Shell (csh) passwd 사용법: 사용자 비밀번호 변경

## Overview
`passwd` 명령어는 사용자 계정의 비밀번호를 변경하는 데 사용됩니다. 이 명령어를 통해 사용자는 자신의 비밀번호를 안전하게 업데이트할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```
passwd [options] [username]
```

## Common Options
- `-l`: 사용자 계정을 잠급니다.
- `-u`: 잠긴 사용자 계정을 활성화합니다.
- `-d`: 사용자의 비밀번호를 삭제합니다.
- `-e`: 사용자의 비밀번호를 즉시 만료시킵니다.

## Common Examples
- 자신의 비밀번호 변경:
  ```csh
  passwd
  ```
  
- 특정 사용자의 비밀번호 변경 (관리자 권한 필요):
  ```csh
  passwd username
  ```

- 사용자 계정 잠금:
  ```csh
  passwd -l username
  ```

- 사용자 계정 활성화:
  ```csh
  passwd -u username
  ```

- 비밀번호 삭제:
  ```csh
  passwd -d username
  ```

## Tips
- 비밀번호는 주기적으로 변경하여 보안을 강화하세요.
- 비밀번호는 대문자, 소문자, 숫자 및 특수 문자를 조합하여 강력하게 설정하세요.
- 비밀번호 변경 후, 새로운 비밀번호를 안전한 곳에 기록해 두는 것이 좋습니다.