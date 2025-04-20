# [리눅스] C Shell (csh) basename 사용법: 파일 경로에서 파일 이름 추출

## Overview
`basename` 명령어는 주어진 파일 경로에서 파일 이름만 추출하여 출력하는 데 사용됩니다. 이 명령어는 파일의 전체 경로를 간단하게 처리하고, 필요한 경우 확장자를 제거할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:

```
basename [options] [arguments]
```

## Common Options
- `-a`: 여러 개의 경로를 한 번에 처리합니다.
- `-s`: 지정한 접미사를 제거합니다.

## Common Examples
다음은 `basename` 명령어의 몇 가지 실용적인 예입니다.

### 예제 1: 기본 사용법
파일 경로에서 파일 이름만 추출합니다.
```csh
basename /usr/local/bin/script.sh
```
출력:
```
script.sh
```

### 예제 2: 확장자 제거
파일 이름에서 특정 확장자를 제거합니다.
```csh
basename /usr/local/bin/script.sh .sh
```
출력:
```
script
```

### 예제 3: 여러 경로 처리
여러 파일 경로를 한 번에 처리합니다.
```csh
basename -a /usr/local/bin/script.sh /home/user/document.txt
```
출력:
```
script.sh
document.txt
```

## Tips
- `basename`을 사용할 때, 파일 경로가 실제로 존재하는지 확인하는 것이 좋습니다.
- 스크립트에서 `basename`을 사용하여 파일 이름을 동적으로 처리할 수 있습니다.
- 여러 파일을 처리할 때는 `-a` 옵션을 활용하여 효율성을 높이세요.