# [리눅스] C Shell (csh) mtr 사용법: 네트워크 경로 추적 및 성능 분석

## Overview
mtr (My Traceroute) 명령은 네트워크 경로를 추적하고 각 홉에서의 패킷 손실 및 지연 시간을 측정하는 도구입니다. 이 명령은 traceroute와 ping의 기능을 결합하여 실시간으로 네트워크 상태를 모니터링할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:

```
mtr [options] [arguments]
```

## Common Options
- `-r`: 보고서 형식으로 출력합니다.
- `-c <count>`: 지정한 횟수만큼 패킷을 전송합니다.
- `-i <interval>`: 각 패킷 전송 사이의 간격을 설정합니다.
- `-p`: 패킷 전송을 중단하지 않고 계속 진행합니다.

## Common Examples
다음은 mtr 명령의 몇 가지 일반적인 사용 예입니다.

1. 기본 사용법:
   ```bash
   mtr example.com
   ```

2. 특정 횟수만큼 패킷 전송:
   ```bash
   mtr -c 5 example.com
   ```

3. 보고서 형식으로 출력:
   ```bash
   mtr -r example.com
   ```

4. 패킷 전송 간격 설정:
   ```bash
   mtr -i 2 example.com
   ```

## Tips
- mtr를 실행할 때 관리자 권한이 필요할 수 있으므로 `sudo`를 사용해 보세요.
- 네트워크 문제를 진단할 때는 여러 도메인에 대해 mtr을 실행하여 비교해 보세요.
- 결과를 파일로 저장하려면 `-r` 옵션과 리다이렉션을 함께 사용하세요.