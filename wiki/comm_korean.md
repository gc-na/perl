# [리눅스] C Shell (csh) comm 사용법: 두 파일의 공통된 줄 찾기

## Overview
`comm` 명령은 두 개의 정렬된 파일을 비교하여 공통된 줄, 첫 번째 파일에만 있는 줄, 두 번째 파일에만 있는 줄을 출력하는 데 사용됩니다. 이 명령은 파일 간의 차이를 분석할 때 유용합니다.

## Usage
기본 구문은 다음과 같습니다:
```
comm [options] [arguments]
```

## Common Options
- `-1`: 첫 번째 파일에만 있는 줄을 출력하지 않습니다.
- `-2`: 두 번째 파일에만 있는 줄을 출력하지 않습니다.
- `-3`: 공통된 줄을 출력하지 않습니다.
- `-i`: 대소문자를 구분하지 않고 비교합니다.

## Common Examples
1. 두 개의 파일 `file1.txt`와 `file2.txt`를 비교하여 모든 줄을 출력합니다.
   ```csh
   comm file1.txt file2.txt
   ```

2. 첫 번째 파일에만 있는 줄만 출력합니다.
   ```csh
   comm -13 file1.txt file2.txt
   ```

3. 두 번째 파일에만 있는 줄만 출력합니다.
   ```csh
   comm -23 file1.txt file2.txt
   ```

4. 공통된 줄만 출력합니다.
   ```csh
   comm -12 file1.txt file2.txt
   ```

5. 대소문자를 무시하고 비교합니다.
   ```csh
   comm -i file1.txt file2.txt
   ```

## Tips
- `comm` 명령을 사용하기 전에 두 파일이 정렬되어 있는지 확인하세요. 정렬되지 않은 파일을 비교하면 예상치 못한 결과가 나올 수 있습니다.
- 결과를 파일로 저장하려면 리다이렉션을 사용하세요. 예를 들어, `comm file1.txt file2.txt > result.txt`와 같이 사용할 수 있습니다.
- `sort` 명령과 함께 사용하여 파일을 정렬한 후 비교하는 것이 좋습니다.