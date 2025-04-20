# [리눅스] C Shell (csh) getopts 사용법: 명령줄 옵션 처리

## Overview
`getopts` 명령은 C Shell 스크립트에서 명령줄 옵션을 처리하는 데 사용됩니다. 이 명령은 스크립트에 전달된 인수들을 분석하여, 사용자에게 유용한 옵션을 제공할 수 있도록 도와줍니다.

## Usage
기본 구문은 다음과 같습니다:

```csh
getopts [options] [arguments]
```

## Common Options
- `-a`: 모든 옵션을 처리합니다.
- `-b`: 옵션을 비활성화합니다.
- `-c`: 옵션의 기본값을 설정합니다.

## Common Examples
다음은 `getopts`를 사용하는 몇 가지 예시입니다.

### 예제 1: 간단한 옵션 처리
```csh
#!/bin/csh
set optstring = "ab:"
while (getopts "$optstring" option)
    switch ($option)
        case "a":
            echo "옵션 A가 선택되었습니다."
            breaksw
        case "b":
            echo "옵션 B가 선택되었습니다. 값: $OPTARG"
            breaksw
        default:
            echo "유효하지 않은 옵션입니다."
    endsw
end
```

### 예제 2: 여러 옵션 처리
```csh
#!/bin/csh
set optstring = "abc"
while (getopts "$optstring" option)
    echo "옵션: $option"
end
```

### 예제 3: 옵션과 인수 함께 사용
```csh
#!/bin/csh
set optstring = "f:"
while (getopts "$optstring" option)
    switch ($option)
        case "f":
            echo "파일 이름: $OPTARG"
            breaksw
        default:
            echo "유효하지 않은 옵션입니다."
    endsw
end
```

## Tips
- `getopts`는 옵션을 처리할 때, 각 옵션의 인수를 `$OPTARG` 변수에 저장합니다. 이를 활용하여 인수를 쉽게 사용할 수 있습니다.
- 옵션 문자열에서 콜론(`:`)을 사용하여 인수가 필요한 옵션을 정의할 수 있습니다.
- 스크립트에서 `getopts`를 사용할 때는 항상 `while` 루프를 사용하여 모든 옵션을 처리하는 것이 좋습니다.