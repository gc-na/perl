# [리눅스] C Shell (csh) if 사용법: 조건문 실행

## Overview
`if` 명령은 C Shell 스크립트에서 조건을 평가하고, 그 결과에 따라 특정 명령을 실행하는 데 사용됩니다. 이는 프로그램 흐름을 제어하는 데 매우 유용합니다.

## Usage
기본 구문은 다음과 같습니다:
```
if (조건) 명령
```

## Common Options
- `else`: 조건이 false일 때 실행할 명령을 지정합니다.
- `else if`: 추가 조건을 평가할 수 있습니다.

## Common Examples

### 기본 사용 예
```csh
if ( -e 파일.txt ) echo "파일이 존재합니다."
```

### else 사용 예
```csh
if ( -e 파일.txt ) then
    echo "파일이 존재합니다."
else
    echo "파일이 존재하지 않습니다."
endif
```

### else if 사용 예
```csh
if ( -e 파일.txt ) then
    echo "파일이 존재합니다."
else if ( -e 다른파일.txt ) then
    echo "다른 파일이 존재합니다."
else
    echo "두 파일 모두 존재하지 않습니다."
endif
```

## Tips
- 조건문을 사용할 때는 항상 `endif`로 블록을 종료해야 합니다.
- 복잡한 조건을 사용할 경우, 괄호를 적절히 사용하여 가독성을 높이세요.
- 스크립트의 흐름을 명확히 하기 위해 주석을 추가하는 것이 좋습니다.