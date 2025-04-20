# [리눅스] C Shell (csh) usermod 사용법: 사용자 계정 수정

## Overview
usermod 명령은 기존 사용자 계정의 속성을 수정하는 데 사용됩니다. 이 명령을 통해 사용자 이름, 홈 디렉토리, 사용자 그룹 등을 변경할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```
usermod [options] [arguments]
```

## Common Options
- `-l`: 사용자 이름을 변경합니다.
- `-d`: 사용자의 홈 디렉토리를 변경합니다.
- `-g`: 사용자의 기본 그룹을 변경합니다.
- `-aG`: 사용자를 추가 그룹에 추가합니다.
- `-s`: 사용자의 로그인 셸을 변경합니다.

## Common Examples
- 사용자 이름 변경:
  ```bash
  usermod -l newusername oldusername
  ```
  
- 홈 디렉토리 변경:
  ```bash
  usermod -d /new/home/directory username
  ```

- 기본 그룹 변경:
  ```bash
  usermod -g newgroup username
  ```

- 추가 그룹에 사용자 추가:
  ```bash
  usermod -aG group1,group2 username
  ```

- 로그인 셸 변경:
  ```bash
  usermod -s /bin/zsh username
  ```

## Tips
- 항상 `usermod` 명령을 실행하기 전에 현재 사용자 정보를 백업하는 것이 좋습니다.
- 사용자 이름이나 홈 디렉토리를 변경한 후에는 해당 사용자로 로그인하여 변경 사항이 적용되었는지 확인하세요.
- 그룹 변경 시, `-aG` 옵션을 사용하여 기존 그룹을 유지하는 것이 중요합니다.