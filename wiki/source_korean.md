# [리눅스] C Shell (csh) source 사용법: 현재 쉘에서 스크립트 실행

## Overview
`source` 명령은 C Shell에서 스크립트 파일을 현재 쉘 환경에서 실행하는 데 사용됩니다. 이 명령을 사용하면 스크립트 내의 변수와 함수가 현재 쉘에 적용되어, 이후의 명령에서 이를 사용할 수 있게 됩니다.

## Usage
기본 구문은 다음과 같습니다:

```
source [options] [arguments]
```

## Common Options
- `-c`: 명령을 문자열로 실행합니다.
- `-q`: 오류 메시지를 표시하지 않습니다.

## Common Examples
다음은 `source` 명령의 몇 가지 일반적인 사용 예입니다.

### 예제 1: 스크립트 파일 실행
```csh
source myscript.csh
```
이 명령은 `myscript.csh` 파일을 현재 쉘에서 실행합니다.

### 예제 2: 환경 변수 설정
```csh
source setenv.csh
```
이 명령은 `setenv.csh` 파일을 실행하여 환경 변수를 설정합니다.

### 예제 3: 함수 정의 포함
```csh
source functions.csh
```
이 명령은 `functions.csh` 파일에 정의된 함수를 현재 쉘에 포함시킵니다.

## Tips
- 스크립트 파일을 실행하기 전에 해당 파일의 권한이 올바르게 설정되어 있는지 확인하세요.
- `source` 명령을 사용하여 환경 설정 파일을 로드하면, 변경 사항이 즉시 적용됩니다.
- 스크립트 내에서 오류가 발생하면, `source` 명령은 해당 오류를 출력하므로 디버깅에 유용합니다.