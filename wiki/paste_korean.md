# [리눅스] C Shell (csh) paste 사용법: 여러 파일의 내용을 병합하기

## Overview
`paste` 명령은 여러 파일의 내용을 수평으로 병합하여 출력하는 데 사용됩니다. 각 파일의 동일한 행을 결합하여 탭으로 구분된 형식으로 결과를 제공합니다.

## Usage
기본 구문은 다음과 같습니다:
```
paste [options] [arguments]
```

## Common Options
- `-d`: 구분자를 지정합니다. 기본적으로 탭이 사용됩니다.
- `-s`: 각 파일의 내용을 수직으로 병합합니다.
- `-z`: 입력 파일의 끝에 NULL 문자를 사용합니다.

## Common Examples
여러 가지 실용적인 예시는 다음과 같습니다.

1. 두 파일의 내용을 병합하기:
   ```csh
   paste file1.txt file2.txt
   ```

2. 구분자를 쉼표로 설정하여 병합하기:
   ```csh
   paste -d ',' file1.txt file2.txt
   ```

3. 파일의 내용을 수직으로 병합하기:
   ```csh
   paste -s file1.txt file2.txt
   ```

4. 여러 파일을 동시에 병합하기:
   ```csh
   paste file1.txt file2.txt file3.txt
   ```

## Tips
- `paste` 명령은 파일의 행 수가 다를 경우, 짧은 파일의 빈 행은 자동으로 추가됩니다.
- 구분자를 지정할 때 여러 개의 구분자를 사용할 수 있습니다. 예를 들어, `-d ', '`를 사용하면 쉼표와 공백으로 구분할 수 있습니다.
- 결과를 다른 파일로 저장하려면 리다이렉션을 사용할 수 있습니다:
   ```csh
   paste file1.txt file2.txt > merged.txt
   ```