<!--
Meta Description: # Perl의 getsockname 함수: 소켓 주소 정보 가져오기 ## 개요 Perl의 `getsockname` 함수는 소켓의 로컬 주소 정보를 가져오는 데 사용됩니다. 이 함수는 네트워크 프로그래밍에서 소켓을 사용할 때 매우 유용합니다. ## 문서화 `getsock...
Meta Keywords: getsockname, socket, 소켓의, 정보를, 함수는
-->

# Perl의 getsockname 함수: 소켓 주소 정보 가져오기

## 개요
Perl의 `getsockname` 함수는 소켓의 로컬 주소 정보를 가져오는 데 사용됩니다. 이 함수는 네트워크 프로그래밍에서 소켓을 사용할 때 매우 유용합니다.

## 문서화
`getsockname` 함수는 소켓의 로컬 주소를 반환합니다. 이는 소켓이 바인딩된 IP 주소와 포트 번호를 포함합니다. 주로 클라이언트와 서버 간의 통신에서 서버가 자신의 주소를 확인할 때 사용됩니다.

### 사용법
```perl
use IO::Socket;

my $socket = IO::Socket::INET->new(
    LocalPort => 12345,
    Proto     => 'udp'
) or die "소켓 생성 실패: $!";

my $addr = getsockname($socket);
```

### 매개변수
- **$socket**: 소켓 객체로, 주소 정보를 가져올 소켓을 지정합니다.

### 반환값
`getsockname`은 소켓의 로컬 주소 정보를 담고 있는 배열을 반환합니다. 이 정보는 IP 주소와 포트 번호로 구성됩니다.

## 예제
### 기본 사용법
다음은 `getsockname`을 사용하여 소켓의 로컬 주소를 가져오는 간단한 예제입니다.

```perl
use IO::Socket;

# UDP 소켓 생성
my $socket = IO::Socket::INET->new(
    LocalPort => 12345,
    Proto     => 'udp'
) or die "소켓 생성 실패: $!";

# 로컬 주소 정보 가져오기
my $addr = getsockname($socket);
my ($port, $ip) = sockaddr_in($addr);

print "IP 주소: " . inet_ntoa($ip) . "\n";
print "포트 번호: $port\n";
```

## 설명
`getsockname`을 사용할 때 주의해야 할 점:
- 소켓이 바인딩되기 전에 `getsockname`을 호출하면 오류가 발생합니다. 따라서 소켓이 정상적으로 생성되고 바인딩된 후에 호출해야 합니다.
- TCP와 UDP 소켓 모두에서 사용할 수 있지만, 사용하는 프로토콜에 따라 수신하는 데이터의 형식이 달라질 수 있습니다.
- 반환된 주소 정보를 해석하기 위해 `sockaddr_in` 및 `inet_ntoa`와 같은 추가 함수가 필요할 수 있습니다.

## 한 줄 요약
Perl의 `getsockname` 함수는 소켓의 로컬 주소 정보를 반환하여 네트워크 프로그래밍에서 유용하게 활용됩니다.