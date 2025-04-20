# [리눅스] C Shell (csh) dirname 사용법: 파일 경로에서 디렉토리 이름 추출

## Overview
`dirname` 명령어는 주어진 파일 경로에서 디렉토리 이름을 추출하는 데 사용됩니다. 이 명령어는 파일의 위치를 식별할 때 유용합니다.

## Usage
기본 구문은 다음과 같습니다:
```
dirname [options] [arguments]
```

## Common Options
- `-z`: 입력이 비어 있는 경우 빈 문자열을 출력합니다.
- `--help`: 사용법에 대한 도움말을 표시합니다.
- `--version`: `dirname`의 버전 정보를 표시합니다.

## Common Examples
1. 기본 사용법:
   ```csh
   dirname /usr/local/bin/script.sh
   ```
   출력: `/usr/local/bin`

2. 상대 경로에서 디렉토리 이름 추출:
   ```csh
   dirname ./documents/report.txt
   ```
   출력: `./documents`

3. 여러 파일 경로에서 디렉토리 이름 추출:
   ```csh
   dirname /home/user/file1.txt /home/user/file2.txt
   ```
   출력:
   ```
   /home/user
   /home/user
   ```

## Tips
- `dirname` 명령어는 스크립트에서 파일 경로를 처리할 때 유용하게 사용될 수 있습니다.
- 경로가 없는 경우, `dirname`은 현재 디렉토리를 반환합니다.
- `dirname`과 `basename`을 함께 사용하면 파일 경로에서 디렉토리와 파일 이름을 쉽게 분리할 수 있습니다.