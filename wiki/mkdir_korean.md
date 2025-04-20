# [리눅스] C Shell (csh) mkdir 사용법: 디렉토리 생성

## Overview
`mkdir` 명령어는 새로운 디렉토리를 생성하는 데 사용됩니다. 이 명령어를 통해 사용자는 파일 시스템 내에 원하는 위치에 새로운 폴더를 만들 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```
mkdir [options] [arguments]
```

## Common Options
- `-p`: 상위 디렉토리가 없을 경우, 상위 디렉토리도 함께 생성합니다.
- `-m`: 생성할 디렉토리의 권한을 설정합니다. 예를 들어, `-m 755`는 읽기 및 실행 권한을 부여합니다.
- `-v`: 생성된 디렉토리에 대한 정보를 출력합니다.

## Common Examples
1. 기본 디렉토리 생성:
   ```csh
   mkdir myfolder
   ```

2. 여러 디렉토리 한 번에 생성:
   ```csh
   mkdir folder1 folder2 folder3
   ```

3. 상위 디렉토리와 함께 생성:
   ```csh
   mkdir -p parent/child
   ```

4. 특정 권한으로 디렉토리 생성:
   ```csh
   mkdir -m 700 securefolder
   ```

5. 생성된 디렉토리 정보 출력:
   ```csh
   mkdir -v newfolder
   ```

## Tips
- 디렉토리를 생성할 때, `-p` 옵션을 사용하면 상위 디렉토리가 없더라도 자동으로 생성되므로 편리합니다.
- 권한 설정을 통해 보안을 강화할 수 있으니, 필요한 경우 `-m` 옵션을 활용하세요.
- 여러 디렉토리를 한 번에 생성할 때는 공백으로 구분하여 나열하면 됩니다.