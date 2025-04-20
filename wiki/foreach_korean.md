# [리눅스] C Shell (csh) foreach 사용법: 반복 작업 수행

## Overview
`foreach` 명령은 C Shell에서 반복 작업을 수행하는 데 사용됩니다. 주어진 리스트의 각 항목에 대해 명령을 실행할 수 있도록 해줍니다.

## Usage
기본 구문은 다음과 같습니다:
```
foreach variable (list)
    command
end
```

## Common Options
`foreach` 명령에는 특별한 옵션이 없지만, 반복할 리스트와 실행할 명령을 적절히 설정하는 것이 중요합니다.

## Common Examples
다음은 `foreach` 명령의 몇 가지 일반적인 예입니다.

1. **리스트의 각 항목 출력하기**
   ```csh
   foreach item (apple banana cherry)
       echo $item
   end
   ```

2. **파일 확장자 변경하기**
   ```csh
   foreach file (*.txt)
       mv $file `basename $file .txt`.bak
   end
   ```

3. **디렉토리 내 파일 삭제하기**
   ```csh
   foreach file (*~)
       rm $file
   end
   ```

4. **숫자 반복하기**
   ```csh
   foreach num (1 2 3 4 5)
       echo "Number: $num"
   end
   ```

## Tips
- `foreach` 명령은 리스트의 항목 수에 따라 반복 횟수가 결정되므로, 리스트를 적절히 설정하는 것이 중요합니다.
- 복잡한 명령을 실행할 때는 명령을 여러 줄로 나누어 가독성을 높일 수 있습니다.
- `foreach`와 함께 `end`를 꼭 사용하여 반복의 끝을 명확히 해야 합니다.