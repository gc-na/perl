# [리눅스] C Shell (csh) hostname 사용법: 호스트 이름 표시 및 설정

## Overview
`hostname` 명령은 시스템의 호스트 이름을 표시하거나 설정하는 데 사용됩니다. 이 명령은 네트워크에서 컴퓨터를 식별하는 데 중요한 역할을 합니다.

## Usage
기본 구문은 다음과 같습니다:
```
hostname [options] [arguments]
```

## Common Options
- `-s`: 짧은 호스트 이름만 표시합니다.
- `-f`: 전체 도메인 이름(FQDN)을 표시합니다.
- `-i`: 호스트의 IP 주소를 표시합니다.
- `--help`: 사용법 정보를 표시합니다.

## Common Examples
- 현재 호스트 이름 확인:
  ```csh
  hostname
  ```

- 짧은 호스트 이름 확인:
  ```csh
  hostname -s
  ```

- 전체 도메인 이름 확인:
  ```csh
  hostname -f
  ```

- 호스트의 IP 주소 확인:
  ```csh
  hostname -i
  ```

- 호스트 이름 변경:
  ```csh
  hostname new-hostname
  ```

## Tips
- 호스트 이름을 변경한 후에는 시스템을 재부팅해야 변경 사항이 적용될 수 있습니다.
- 네트워크 설정 파일에서 호스트 이름을 영구적으로 설정하는 것이 좋습니다.
- 호스트 이름은 알파벳, 숫자 및 하이픈만 포함해야 하며, 공백이나 특수 문자는 피해야 합니다.