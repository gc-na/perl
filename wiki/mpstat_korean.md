# [리눅스] C Shell (csh) mpstat 사용법: CPU 통계 모니터링

## Overview
mpstat 명령은 시스템의 CPU 사용률을 모니터링하는 데 사용됩니다. 이 명령은 각 CPU의 사용 현황을 보여주어 성능 분석 및 문제 해결에 유용합니다.

## Usage
기본 구문은 다음과 같습니다:
```
mpstat [options] [arguments]
```

## Common Options
- `-P ALL`: 모든 CPU의 통계를 표시합니다.
- `-u`: CPU 사용률을 보여줍니다.
- `-r`: 메모리 사용률을 표시합니다.
- `-h`: 출력 형식을 사람이 읽기 쉽게 표시합니다.

## Common Examples
- 모든 CPU의 사용률 확인:
  ```bash
  mpstat -P ALL
  ```

- CPU 사용률을 5초 간격으로 3번 확인:
  ```bash
  mpstat 5 3
  ```

- CPU 사용률과 메모리 사용률을 함께 표시:
  ```bash
  mpstat -u -r
  ```

## Tips
- CPU 사용률이 지속적으로 90% 이상인 경우, 시스템 성능 저하의 원인을 분석해야 합니다.
- 정기적으로 mpstat 명령을 실행하여 CPU 사용 패턴을 기록하면 성능 문제를 사전에 예방할 수 있습니다.
- 스크립트를 작성하여 특정 시간 간격으로 mpstat를 실행하고 결과를 로그 파일에 저장하는 것도 유용합니다.