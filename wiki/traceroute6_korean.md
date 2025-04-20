# [리눅스] C Shell (csh) traceroute6 사용법: IPv6 경로 추적

## Overview
traceroute6 명령은 IPv6 네트워크에서 패킷이 목적지에 도달하기까지 거치는 경로를 추적하는 데 사용됩니다. 이 명령은 네트워크 문제를 진단하고, 패킷이 이동하는 경로를 시각화하는 데 유용합니다.

## Usage
기본 구문은 다음과 같습니다:
```
traceroute6 [options] [arguments]
```

## Common Options
- `-m <max_ttl>`: 최대 TTL(Time To Live) 값을 설정합니다.
- `-p <port>`: 사용하려는 포트 번호를 지정합니다.
- `-q <nqueries>`: 각 홉에서 전송할 쿼리의 수를 설정합니다.
- `-w <wait>`: 응답을 기다리는 시간을 설정합니다.

## Common Examples
1. 기본 사용법:
   ```bash
   traceroute6 google.com
   ```

2. 최대 TTL을 30으로 설정:
   ```bash
   traceroute6 -m 30 google.com
   ```

3. 특정 포트(예: 80)로 traceroute 수행:
   ```bash
   traceroute6 -p 80 google.com
   ```

4. 각 홉에서 3개의 쿼리 전송:
   ```bash
   traceroute6 -q 3 google.com
   ```

5. 응답 대기 시간을 5초로 설정:
   ```bash
   traceroute6 -w 5 google.com
   ```

## Tips
- traceroute6를 사용할 때는 네트워크 방화벽 설정이 응답에 영향을 줄 수 있으므로, 방화벽 규칙을 확인하는 것이 좋습니다.
- 다양한 옵션을 조합하여 사용하면 더욱 상세한 경로 정보를 얻을 수 있습니다.
- 결과를 분석할 때, 각 홉의 응답 시간을 비교하여 네트워크 병목 현상을 파악할 수 있습니다.