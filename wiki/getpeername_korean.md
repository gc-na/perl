<!--
Meta Description: # Perl의 getpeername 함수: 소켓의 원격 주소 가져오기 ## 개요 `getpeername`는 Perl에서 소켓 프로그래밍을 할 때, 연결된 소켓의 원격 주소 정보를 가져오는 함수입니다. 이 함수는 네트워크 프로그래밍에서 클라이언트의 IP 주소와 포트를 확...
Meta Keywords: getpeername, socket, 정보를, 소켓의, 연결된
-->

# Perl의 getpeername 함수: 소켓의 원격 주소 가져오기

## 개요
`getpeername`는 Perl에서 소켓 프로그래밍을 할 때, 연결된 소켓의 원격 주소 정보를 가져오는 함수입니다. 이 함수는 네트워크 프로그래밍에서 클라이언트의 IP 주소와 포트를 확인하는 데 유용합니다.

## 문서화

### 목적
`getpeername`는 소켓의 원격 주소를 반환하여, 연결된 클라이언트나 서버의 정보를 알아내는 데 사용됩니다. 주로 TCP/IP 소켓에서 사용되며, 소켓을 통해 연결된 상대방의 IP 주소와 포트를 식별할 수 있습니다.

### 사용법
`getpeername` 함수는 소켓 핸들을 인자로 받아, 그 소켓의 원격 주소 정보를 반환합니다. 사용 방법은 아래와 같습니다.

```perl
use IO::Socket;

my $socket = IO::Socket::INET->new(
    PeerAddr => 'example.com',
    PeerPort => 'http',
    Proto    => 'tcp',
) or die "소켓 생성 실패: $!";

my $peer_address = getpeername($socket);
```

### 세부사항
- `getpeername`은 소켓 핸들을 인자로 받아야 하며, 성공 시 원격 주소 정보를 포함한 배열을 반환합니다.
- 반환된 주소 정보는 `Socket` 모듈을 통해 처리할 수 있습니다.
- 실패할 경우 `undef`를 반환하고, `$!` 변수에 오류 메시지가 설정됩니다.

## 예제

### 기본 사용 예제
아래는 `getpeername`을 사용하여 클라이언트의 IP 주소를 출력하는 간단한 예제입니다.

```perl
use IO::Socket;
use Socket;

my $server = IO::Socket::INET->new(
    LocalPort => 7890,
    Proto     => 'udp',
    Listen    => 1,
) or die "서버 소켓 생성 실패: $!";

while (my $client = $server->accept()) {
    my $peer_address = getpeername($client);
    my ($port, $ip_address) = unpack_sockaddr_in($peer_address);
    print "클라이언트 IP: ", inet_ntoa($ip_address), ", 포트: $port\n";
    close($client);
}
```

## 설명
`getpeername`을 사용할 때 주의해야 할 점은 다음과 같습니다:
- 소켓이 연결되어 있지 않거나, 유효하지 않은 소켓 핸들을 전달할 경우 오류가 발생합니다.
- `getpeername`은 주로 TCP 소켓에서 사용되며, UDP와 같은 연결less 프로토콜에서는 사용되지 않습니다.
- 반환된 주소 정보를 처리할 때, `Socket` 모듈의 다양한 함수를 사용하여 IP 주소와 포트 번호를 추출할 수 있습니다.

## 한 줄 요약
`getpeername`는 Perl 소켓 프로그래밍에서 연결된 소켓의 원격 주소 정보를 가져오는 함수입니다.