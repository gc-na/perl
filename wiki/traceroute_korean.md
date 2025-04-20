# [한국어] C Shell (csh) traceroute 사용법: 네트워크 경로 추적

## 개요
traceroute 명령은 네트워크에서 데이터 패킷이 목적지에 도달하기까지 거치는 경로를 추적하는 데 사용됩니다. 이 명령은 각 홉에서의 응답 시간을 측정하여 네트워크 성능을 분석하는 데 유용합니다.

## 사용법
기본 구문은 다음과 같습니다:

```
traceroute [옵션] [인수]
```

## 일반 옵션
- `-m <값>`: 최대 홉 수를 설정합니다.
- `-n`: 호스트 이름 대신 IP 주소를 표시합니다.
- `-w <초>`: 각 홉에 대한 응답 대기 시간을 설정합니다.

## 일반 예제
다음은 traceroute 명령의 몇 가지 실제 예입니다.

1. 기본 traceroute 실행:
   ```bash
   traceroute example.com
   ```

2. 최대 홉 수를 15로 설정:
   ```bash
   traceroute -m 15 example.com
   ```

3. IP 주소만 표시:
   ```bash
   traceroute -n example.com
   ```

4. 응답 대기 시간을 2초로 설정:
   ```bash
   traceroute -w 2 example.com
   ```

## 팁
- traceroute 명령은 네트워크 문제를 진단하는 데 유용하므로, 문제가 발생했을 때 자주 사용하세요.
- 여러 번 실행하여 결과를 비교하면 네트워크의 일관성을 확인할 수 있습니다.
- 방화벽이나 보안 설정에 따라 traceroute 결과가 제한될 수 있으므로, 이를 고려하여 분석하세요.