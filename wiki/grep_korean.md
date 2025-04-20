# [리눅스] C Shell (csh) grep 사용법: 텍스트에서 패턴 검색

## Overview
`grep` 명령어는 텍스트 파일에서 특정 패턴이나 문자열을 검색하는 데 사용됩니다. 이 명령어는 매우 강력하며, 다양한 옵션을 통해 검색 결과를 필터링하고 조작할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:

```csh
grep [options] [arguments]
```

## Common Options
- `-i`: 대소문자를 구분하지 않고 검색합니다.
- `-v`: 패턴과 일치하지 않는 행을 출력합니다.
- `-r`: 디렉토리 내의 모든 파일을 재귀적으로 검색합니다.
- `-n`: 일치하는 행의 번호를 함께 출력합니다.
- `-l`: 패턴과 일치하는 파일의 이름만 출력합니다.

## Common Examples
- 특정 문자열이 포함된 파일의 행을 검색하기:
  ```csh
  grep "hello" filename.txt
  ```

- 대소문자를 구분하지 않고 검색하기:
  ```csh
  grep -i "hello" filename.txt
  ```

- 디렉토리 내의 모든 파일에서 패턴 검색하기:
  ```csh
  grep -r "hello" /path/to/directory
  ```

- 일치하는 행의 번호와 함께 출력하기:
  ```csh
  grep -n "hello" filename.txt
  ```

- 특정 패턴과 일치하지 않는 행 출력하기:
  ```csh
  grep -v "hello" filename.txt
  ```

## Tips
- 검색할 패턴을 작은 따옴표(')로 감싸면 쉘에서 해석되는 것을 방지할 수 있습니다.
- 정규 표현식을 사용하여 더 복잡한 패턴을 검색할 수 있습니다.
- `grep` 명령어는 파이프와 함께 사용하여 다른 명령의 출력 결과를 필터링하는 데 유용합니다.