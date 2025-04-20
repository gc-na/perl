# [리눅스] C Shell (csh) chgrp 사용법: 파일 그룹 변경

## Overview
`chgrp` 명령은 파일이나 디렉토리의 그룹 소유자를 변경하는 데 사용됩니다. 이 명령을 통해 사용자는 특정 파일이나 디렉토리에 대한 접근 권한을 그룹 단위로 조정할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:

```csh
chgrp [옵션] [인수]
```

## Common Options
- `-R`: 하위 디렉토리와 파일에 대해 재귀적으로 그룹을 변경합니다.
- `-v`: 변경된 파일에 대한 정보를 자세히 출력합니다.
- `-c`: 변경된 파일에 대한 정보를 출력합니다.

## Common Examples
1. 특정 파일의 그룹을 변경하기:
   ```csh
   chgrp developers project.txt
   ```

2. 여러 파일의 그룹을 동시에 변경하기:
   ```csh
   chgrp admins report1.txt report2.txt
   ```

3. 디렉토리와 그 하위 파일의 그룹을 재귀적으로 변경하기:
   ```csh
   chgrp -R team /path/to/directory
   ```

4. 변경된 파일에 대한 정보를 출력하기:
   ```csh
   chgrp -v users file.txt
   ```

## Tips
- 그룹 소유자를 변경하기 전에 현재 파일의 그룹 소유자를 확인하려면 `ls -l` 명령을 사용하세요.
- 그룹 변경 권한이 없는 경우, `sudo` 명령을 사용하여 관리자 권한으로 실행할 수 있습니다.
- 그룹 이름을 정확히 입력해야 하며, 시스템에 존재하는 그룹이어야 합니다.