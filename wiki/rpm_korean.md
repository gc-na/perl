# [리눅스] C Shell (csh) rpm 사용법: 패키지 관리 명령어

## Overview
`rpm` 명령어는 Red Hat 패키지 관리 시스템에서 사용되는 도구로, 소프트웨어 패키지를 설치, 제거, 업데이트 및 관리하는 데 사용됩니다. 이 명령어는 RPM 형식의 패키지를 다루며, 시스템의 소프트웨어 상태를 쉽게 관리할 수 있도록 도와줍니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
rpm [options] [arguments]
```

## Common Options
- `-i`: 패키지를 설치합니다.
- `-e`: 패키지를 제거합니다.
- `-U`: 패키지를 업그레이드합니다.
- `-q`: 패키지 정보를 조회합니다.
- `--install`: 패키지를 설치하는 명령어의 전체 옵션입니다.
- `--remove`: 패키지를 제거하는 명령어의 전체 옵션입니다.

## Common Examples
- 패키지 설치:
```bash
rpm -i package.rpm
```
- 패키지 제거:
```bash
rpm -e package-name
```
- 패키지 업그레이드:
```bash
rpm -U package.rpm
```
- 설치된 패키지 목록 조회:
```bash
rpm -qa
```
- 특정 패키지 정보 조회:
```bash
rpm -qi package-name
```

## Tips
- 패키지를 설치하기 전에 항상 의존성 문제를 확인하세요.
- `-v` 옵션을 추가하여 자세한 출력을 받을 수 있습니다.
- 패키지를 제거하기 전에 해당 패키지가 다른 패키지에 의존하고 있는지 확인하는 것이 좋습니다.