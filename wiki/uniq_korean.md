# [리눅스] C Shell (csh) uniq 사용법: 중복된 줄 제거

## Overview
`uniq` 명령어는 파일이나 입력 스트림에서 중복된 줄을 제거하는 데 사용됩니다. 이 명령어는 일반적으로 정렬된 데이터와 함께 사용되며, 중복된 줄을 한 번만 출력합니다.

## Usage
기본 구문은 다음과 같습니다:
```
uniq [options] [arguments]
```

## Common Options
- `-c`: 각 줄의 중복 횟수를 함께 출력합니다.
- `-d`: 중복된 줄만 출력합니다.
- `-u`: 중복되지 않은 줄만 출력합니다.
- `-i`: 대소문자를 무시하고 중복을 검사합니다.

## Common Examples
중복된 줄을 제거하는 기본 예제:
```bash
uniq input.txt output.txt
```

중복된 줄의 수를 출력하는 예제:
```bash
uniq -c input.txt
```

중복된 줄만 출력하는 예제:
```bash
uniq -d input.txt
```

대소문자를 무시하고 중복을 제거하는 예제:
```bash
uniq -i input.txt output.txt
```

## Tips
- `uniq` 명령어는 입력 데이터가 정렬되어 있어야 제대로 작동하므로, 필요할 경우 `sort` 명령어와 함께 사용하세요.
- 중복된 줄을 확인하고 싶다면 `-c` 옵션을 사용하여 각 줄의 개수를 확인하는 것이 유용합니다.
- 파일을 직접 수정하지 않고 결과를 다른 파일에 저장하는 것이 안전합니다.