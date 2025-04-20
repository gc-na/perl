# [리눅스] C Shell (csh) sort 사용법: 데이터 정렬

## Overview
`sort` 명령어는 텍스트 파일의 내용을 정렬하는 데 사용됩니다. 이 명령어는 기본적으로 각 줄을 알파벳 순서 또는 숫자 순서로 정렬하여 출력합니다.

## Usage
기본 구문은 다음과 같습니다:
```
sort [options] [arguments]
```

## Common Options
- `-r`: 역순으로 정렬합니다.
- `-n`: 숫자 값을 기준으로 정렬합니다.
- `-k`: 특정 필드를 기준으로 정렬합니다.
- `-u`: 중복된 줄을 제거합니다.

## Common Examples
- 기본 정렬:
  ```csh
  sort filename.txt
  ```

- 역순 정렬:
  ```csh
  sort -r filename.txt
  ```

- 숫자 기준 정렬:
  ```csh
  sort -n numbers.txt
  ```

- 특정 필드 기준 정렬 (예: 두 번째 필드):
  ```csh
  sort -k 2 filename.txt
  ```

- 중복 제거 후 정렬:
  ```csh
  sort -u filename.txt
  ```

## Tips
- 정렬할 파일이 클 경우, `-o` 옵션을 사용하여 정렬된 결과를 다른 파일에 저장할 수 있습니다.
- 여러 옵션을 조합하여 사용할 수 있으므로, 필요에 따라 적절한 옵션을 선택하세요.
- 정렬할 데이터의 형식에 따라 적절한 옵션을 선택하는 것이 중요합니다.