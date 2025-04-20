# [리눅스] C Shell (csh) test 사용법: 조건 평가

## Overview
`test` 명령은 주어진 조건을 평가하여 참(true) 또는 거짓(false)을 반환하는 명령입니다. 주로 스크립트 내에서 조건문을 작성할 때 사용됩니다.

## Usage
기본 구문은 다음과 같습니다:
```
test [options] [arguments]
```

## Common Options
- `-e 파일`: 파일이 존재하는지 확인합니다.
- `-d 디렉토리`: 주어진 경로가 디렉토리인지 확인합니다.
- `-f 파일`: 주어진 경로가 일반 파일인지 확인합니다.
- `-z 문자열`: 문자열의 길이가 0인지 확인합니다.
- `-n 문자열`: 문자열의 길이가 0이 아닌지 확인합니다.
- `=`: 두 문자열이 같은지 비교합니다.
- `!=`: 두 문자열이 다른지 비교합니다.

## Common Examples
- 파일 존재 여부 확인:
  ```csh
  if ( `test -e myfile.txt` ) then
      echo "파일이 존재합니다."
  else
      echo "파일이 존재하지 않습니다."
  endif
  ```

- 디렉토리 확인:
  ```csh
  if ( `test -d /path/to/directory` ) then
      echo "디렉토리가 존재합니다."
  else
      echo "디렉토리가 존재하지 않습니다."
  endif
  ```

- 문자열 비교:
  ```csh
  set str1 = "hello"
  set str2 = "world"
  if ( `test $str1 = $str2` ) then
      echo "문자열이 같습니다."
  else
      echo "문자열이 다릅니다."
  endif
  ```

- 문자열 길이 확인:
  ```csh
  set myString = ""
  if ( `test -z $myString` ) then
      echo "문자열이 비어 있습니다."
  else
      echo "문자열이 비어 있지 않습니다."
  endif
  ```

## Tips
- `test` 명령은 조건문에서 매우 유용하므로 자주 사용하게 됩니다. 
- `[`와 `]`를 사용하여 `test` 명령을 대체할 수 있습니다. 예: `[ -e myfile.txt ]`.
- 조건문을 사용할 때는 항상 `then`과 `endif`를 잊지 마세요.