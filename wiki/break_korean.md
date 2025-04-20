# [리눅스] C Shell (csh) break 사용법: 루프 종료

## Overview
`break` 명령은 C Shell 스크립트에서 루프를 종료하는 데 사용됩니다. 이 명령을 사용하면 현재 실행 중인 반복문을 즉시 중단하고 루프 밖으로 나갈 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```csh
break [options]
```

## Common Options
- `n`: 종료할 루프의 깊이를 지정합니다. 기본값은 1로, 가장 안쪽 루프를 종료합니다.

## Common Examples
- **기본 사용법**: 가장 안쪽 루프 종료
```csh
foreach i (1 2 3)
    echo $i
    if ($i == 2) break
end
```
위의 예제에서는 `i`가 2일 때 루프가 종료됩니다.

- **루프 깊이 지정**: 두 번째 루프 종료
```csh
foreach i (1 2)
    foreach j (1 2 3)
        echo "$i, $j"
        if ($j == 2) break 2
    end
end
```
이 예제에서는 `j`가 2일 때 가장 바깥쪽 루프도 종료됩니다.

- **조건에 따른 종료**: 특정 조건에서 루프 종료
```csh
set count = 0
while ($count < 5)
    @ count++
    if ($count == 3) break
    echo $count
end
```
여기서는 `count`가 3일 때 루프가 종료됩니다.

## Tips
- `break` 명령은 루프 내에서 조건부로 사용하면 유용합니다.
- 루프 깊이를 지정할 때는 주의하여 사용하세요. 잘못된 깊이를 지정하면 예상치 못한 결과를 초래할 수 있습니다.
- `break`와 함께 `continue` 명령을 사용하여 루프의 흐름을 더 세밀하게 제어할 수 있습니다.