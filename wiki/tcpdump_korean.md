# [리눅스] C Shell (csh) tcpdump 사용법: 네트워크 패킷 캡처

## Overview
tcpdump는 네트워크 인터페이스를 통해 흐르는 패킷을 캡처하고 분석하는 데 사용되는 강력한 명령어입니다. 이 도구는 네트워크 트래픽을 모니터링하고 문제를 진단하는 데 유용합니다.

## Usage
tcpdump 명령어의 기본 구문은 다음과 같습니다:

```csh
tcpdump [options] [arguments]
```

## Common Options
- `-i <interface>`: 패킷을 캡처할 네트워크 인터페이스를 지정합니다.
- `-n`: 호스트 이름을 해석하지 않고 IP 주소를 그대로 표시합니다.
- `-v`: 패킷에 대한 자세한 정보를 출력합니다. `-vv` 또는 `-vvv`를 사용하면 더 많은 정보를 볼 수 있습니다.
- `-c <count>`: 캡처할 패킷의 수를 지정합니다.
- `-w <file>`: 캡처한 패킷을 파일에 저장합니다.

## Common Examples
다음은 tcpdump의 몇 가지 일반적인 사용 예입니다.

1. 특정 인터페이스에서 패킷 캡처하기:
   ```csh
   tcpdump -i eth0
   ```

2. 패킷 수 제한하기:
   ```csh
   tcpdump -i eth0 -c 10
   ```

3. 패킷을 파일로 저장하기:
   ```csh
   tcpdump -i eth0 -w output.pcap
   ```

4. IP 주소를 해석하지 않고 캡처하기:
   ```csh
   tcpdump -i eth0 -n
   ```

5. 자세한 패킷 정보 출력하기:
   ```csh
   tcpdump -i eth0 -v
   ```

## Tips
- tcpdump를 사용할 때는 관리자 권한이 필요할 수 있으므로 `sudo`를 사용하는 것이 좋습니다.
- 캡처한 데이터를 분석할 때는 Wireshark와 같은 GUI 도구를 사용하면 더 편리합니다.
- 필터를 사용하여 특정 트래픽만 캡처하면 데이터의 양을 줄이고 분석을 쉽게 할 수 있습니다. 예를 들어, 특정 포트의 트래픽만 캡처하려면 `tcpdump -i eth0 port 80`과 같이 사용할 수 있습니다.