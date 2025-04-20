# [리눅스] C Shell (csh) yum 사용법: 패키지 관리 명령어

## Overview
`yum`은 리눅스에서 소프트웨어 패키지를 설치, 업데이트 및 제거하는 데 사용되는 패키지 관리 도구입니다. 이 명령어는 RPM 패키지를 기반으로 하며, 의존성 문제를 자동으로 해결해 줍니다.

## Usage
기본 구문은 다음과 같습니다:
```
yum [options] [arguments]
```

## Common Options
- `install`: 패키지를 설치합니다.
- `remove`: 패키지를 제거합니다.
- `update`: 설치된 패키지를 업데이트합니다.
- `search`: 패키지를 검색합니다.
- `info`: 패키지에 대한 정보를 표시합니다.

## Common Examples
- 패키지 설치:
  ```bash
  yum install httpd
  ```
- 패키지 제거:
  ```bash
  yum remove httpd
  ```
- 패키지 업데이트:
  ```bash
  yum update httpd
  ```
- 패키지 검색:
  ```bash
  yum search nginx
  ```
- 패키지 정보 확인:
  ```bash
  yum info httpd
  ```

## Tips
- `yum` 명령어를 사용할 때는 항상 `sudo`를 붙여서 관리자 권한으로 실행하는 것이 좋습니다.
- 패키지 설치 후에는 `yum clean all` 명령어를 사용하여 캐시를 정리하는 것이 유용합니다.
- 주기적으로 `yum update`를 실행하여 시스템의 보안을 유지하세요.