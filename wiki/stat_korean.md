# [리눅스] C Shell (csh) stat 사용법: 파일의 상태 정보 확인

## Overview
`stat` 명령어는 파일이나 디렉토리에 대한 상세한 상태 정보를 표시합니다. 이 정보에는 파일의 크기, 수정 시간, 접근 권한 등이 포함됩니다.

## Usage
기본 구문은 다음과 같습니다:
```csh
stat [options] [arguments]
```

## Common Options
- `-c` : 사용자 정의 형식으로 출력합니다.
- `-f` : 파일 시스템 정보를 표시합니다.
- `-L` : 심볼릭 링크를 따라가서 실제 파일의 정보를 표시합니다.

## Common Examples
- 특정 파일의 상태 정보 확인:
```csh
stat filename.txt
```

- 사용자 정의 형식으로 출력:
```csh
stat -c '%s bytes' filename.txt
```

- 심볼릭 링크를 따라가서 정보 확인:
```csh
stat -L symlink
```

- 여러 파일의 상태 정보를 한 번에 확인:
```csh
stat file1.txt file2.txt
```

## Tips
- 파일의 상태 정보를 자주 확인해야 하는 경우, `alias`를 사용하여 자주 사용하는 옵션을 단축할 수 있습니다.
- `stat` 명령어의 출력을 파이프하여 다른 명령어와 결합하여 사용할 수 있습니다. 예를 들어, `grep`을 사용하여 특정 정보를 필터링할 수 있습니다.