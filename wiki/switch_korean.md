# [리눅스] C Shell (csh) switch 사용법: 조건에 따라 명령 실행

## Overview
`switch` 명령은 C Shell에서 여러 조건을 평가하여 해당 조건에 맞는 명령을 실행하는 데 사용됩니다. 이는 복잡한 조건문을 간단하게 처리할 수 있도록 도와줍니다.

## Usage
기본 구문은 다음과 같습니다:

```
switch (expression)
    case pattern1:
        commands
        breaksw
    case pattern2:
        commands
        breaksw
    default:
        commands
        breaksw
endsw
```

## Common Options
- `case pattern:`: 특정 패턴에 대한 조건을 정의합니다.
- `breaksw`: 현재 `case` 블록을 종료하고 `switch` 문을 빠져나갑니다.
- `default:`: 어떤 `case`에도 해당하지 않을 경우 실행되는 명령을 정의합니다.

## Common Examples

### 예제 1: 숫자에 따른 메시지 출력
```csh
set num = 2
switch ($num)
    case 1:
        echo "숫자는 1입니다."
        breaksw
    case 2:
        echo "숫자는 2입니다."
        breaksw
    default:
        echo "숫자는 1도 2도 아닙니다."
        breaksw
endsw
```

### 예제 2: 파일 확장자에 따른 처리
```csh
set file = "document.txt"
switch ($file)
    case *.txt:
        echo "텍스트 파일입니다."
        breaksw
    case *.jpg:
        echo "JPEG 이미지입니다."
        breaksw
    default:
        echo "알 수 없는 파일 형식입니다."
        breaksw
endsw
```

### 예제 3: 사용자 입력에 따른 반응
```csh
set input = "yes"
switch ($input)
    case yes:
        echo "사용자가 '예'라고 응답했습니다."
        breaksw
    case no:
        echo "사용자가 '아니오'라고 응답했습니다."
        breaksw
    default:
        echo "알 수 없는 응답입니다."
        breaksw
endsw
```

## Tips
- `switch` 문을 사용할 때는 `breaksw`를 잊지 말고 추가하여 원치 않는 추가 실행을 방지하세요.
- 패턴 매칭을 사용할 때는 와일드카드(`*`)를 활용하여 다양한 경우를 처리할 수 있습니다.
- `default` 구문을 통해 모든 경우를 처리하지 못했을 때의 기본 동작을 정의하는 것이 좋습니다.