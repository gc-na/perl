# [리눅스] C Shell (csh) logrotate 사용법: 로그 파일 관리

## Overview
logrotate 명령어는 시스템의 로그 파일을 관리하는 데 사용됩니다. 이 명령어는 로그 파일의 크기가 일정 수준에 도달했을 때 자동으로 회전시키고, 오래된 로그 파일을 삭제하거나 압축하여 디스크 공간을 절약합니다.

## Usage
기본 구문은 다음과 같습니다:

```csh
logrotate [options] [arguments]
```

## Common Options
- `-f`: 강제로 로그 회전을 수행합니다.
- `-s`: 상태 파일을 지정합니다.
- `-v`: 자세한 출력을 표시합니다.
- `-d`: 실제로 회전을 수행하지 않고, 어떤 작업이 이루어질지를 보여줍니다.

## Common Examples
1. 기본 설정 파일을 사용하여 로그 회전 수행:
   ```csh
   logrotate /etc/logrotate.conf
   ```

2. 강제로 로그 회전 수행:
   ```csh
   logrotate -f /etc/logrotate.conf
   ```

3. 로그 회전 상태 확인 (실행하지 않음):
   ```csh
   logrotate -d /etc/logrotate.conf
   ```

4. 특정 상태 파일 사용:
   ```csh
   logrotate -s /var/lib/logrotate/status /etc/logrotate.conf
   ```

## Tips
- 로그 파일의 크기와 회전 주기를 적절히 설정하여 시스템 자원을 효율적으로 관리하세요.
- 로그 회전 후 오래된 로그 파일을 자동으로 삭제하도록 설정하면 디스크 공간을 절약할 수 있습니다.
- 설정 변경 후에는 `logrotate -d` 옵션을 사용하여 예상되는 동작을 미리 확인하는 것이 좋습니다.