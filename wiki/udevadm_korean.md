# [리눅스] C Shell (csh) udevadm 사용법: 장치 관리 명령어

## Overview
`udevadm` 명령어는 리눅스 시스템에서 장치 관리와 관련된 작업을 수행하는 도구입니다. 이 명령어는 udev 장치 관리 데몬과 상호작용하여 장치의 상태를 확인하고, 장치 이벤트를 모니터링하며, 장치 규칙을 관리하는 데 사용됩니다.

## Usage
기본 구문은 다음과 같습니다:

```
udevadm [options] [arguments]
```

## Common Options
- `info`: 특정 장치에 대한 정보를 표시합니다.
- `trigger`: 장치 이벤트를 트리거하여 udev 규칙을 실행합니다.
- `settle`: 현재의 모든 장치 이벤트가 완료될 때까지 대기합니다.
- `control`: udev 데몬의 동작을 제어합니다.

## Common Examples
장치 정보를 확인하는 예제:

```bash
udevadm info --query=all --name=/dev/sda
```

장치 이벤트를 트리거하는 예제:

```bash
udevadm trigger
```

모든 장치 이벤트가 완료될 때까지 대기하는 예제:

```bash
udevadm settle
```

## Tips
- `udevadm` 명령어를 사용할 때는 루트 권한이 필요할 수 있으므로, `sudo`를 사용하여 실행하는 것이 좋습니다.
- 장치 규칙을 수정한 후에는 `udevadm control --reload-rules` 명령어로 규칙을 다시 로드하는 것을 잊지 마세요.
- `udevadm monitor` 명령어를 사용하여 실시간으로 장치 이벤트를 모니터링할 수 있습니다.