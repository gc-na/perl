# [리눅스] C Shell (csh) continue 사용법: 루프에서 다음 반복으로 넘어가기

## Overview
`continue` 명령은 C Shell 스크립트에서 루프의 현재 반복을 종료하고 다음 반복으로 넘어가게 하는 데 사용됩니다. 주로 조건문과 함께 사용되어 특정 조건이 충족될 때 다음 반복으로 건너뛰는 데 유용합니다.

## Usage
기본 구문은 다음과 같습니다:

```
continue [options]
```

## Common Options
`continue` 명령은 일반적으로 옵션을 사용하지 않으며, 루프 내에서만 사용됩니다. 그러나 특정 루프에서 특정 반복을 건너뛰고 싶을 때는 루프의 레벨을 지정할 수 있습니다.

## Common Examples

### 예제 1: 기본 사용법
```csh
foreach i (1 2 3 4 5)
    if ($i == 3) then
        continue
    endif
    echo $i
end
```
위의 예제는 1, 2, 4, 5를 출력합니다. 3일 경우 `continue` 명령으로 인해 출력되지 않습니다.

### 예제 2: while 루프에서 사용
```csh
set i = 0
while ($i < 5)
    @ i++
    if ($i == 2) then
        continue
    endif
    echo $i
end
```
이 예제는 1, 3, 4를 출력합니다. 2일 경우 `continue` 명령으로 인해 출력되지 않습니다.

### 예제 3: 중첩 루프에서 사용
```csh
foreach i (1 2)
    foreach j (1 2 3)
        if ($j == 2) then
            continue
        endif
        echo "$i $j"
    end
end
```
이 예제는 다음과 같은 출력을 생성합니다:
```
1 1
1 3
2 1
2 3
```
여기서 j가 2일 경우 건너뛰게 됩니다.

## Tips
- `continue` 명령은 루프 내에서만 사용해야 하며, 루프의 흐름을 제어하는 데 유용합니다.
- 조건문과 함께 사용하여 특정 조건에서만 다음 반복으로 넘어가도록 설정할 수 있습니다.
- 중첩 루프에서 `continue`를 사용할 경우, 현재 루프의 레벨을 고려하여 사용해야 합니다.