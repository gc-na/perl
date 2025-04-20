# [리눅스] C Shell (csh) timedatectl 사용법: 시스템 시간 및 날짜 관리

## Overview
`timedatectl` 명령어는 시스템의 시간 및 날짜를 설정하고 관리하는 데 사용됩니다. 이 명령어를 통해 현재 시간, 날짜, 타임존 및 NTP(Network Time Protocol) 설정을 확인하고 조정할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:

```csh
timedatectl [options] [arguments]
```

## Common Options
- `status`: 현재 시간 및 날짜 정보를 표시합니다.
- `set-time`: 시스템 시간을 설정합니다.
- `set-timezone`: 시스템의 타임존을 설정합니다.
- `set-ntp`: NTP 동기화를 활성화 또는 비활성화합니다.
- `list-timezones`: 사용 가능한 타임존 목록을 표시합니다.

## Common Examples
- 현재 시간 및 날짜 정보 확인:
```csh
timedatectl status
```

- 시스템 시간 설정 (예: 2023년 10월 1일 12시 30분):
```csh
timedatectl set-time '2023-10-01 12:30:00'
```

- 시스템 타임존 설정 (예: 아시아/서울):
```csh
timedatectl set-timezone Asia/Seoul
```

- NTP 동기화 활성화:
```csh
timedatectl set-ntp true
```

- 사용 가능한 타임존 목록 보기:
```csh
timedatectl list-timezones
```

## Tips
- 시간을 설정할 때는 항상 올바른 형식(`YYYY-MM-DD HH:MM:SS`)을 사용하세요.
- 타임존을 변경한 후에는 시스템의 모든 시간 관련 서비스에 영향을 미칠 수 있으므로 주의가 필요합니다.
- NTP 동기화를 활성화하면 시스템 시간이 자동으로 인터넷 시간 서버와 동기화됩니다.