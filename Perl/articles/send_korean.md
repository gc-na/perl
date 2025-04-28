<!--
Meta Description: # Perl에서의 send 명령어: 소켓 통신의 기초 ## 개요 `send`는 Perl에서 소켓을 통해 데이터를 전송하는 데 사용되는 함수입니다. 이 함수는 네트워크 프로그래밍 및 IPC(Inter-Process Communication)에서 필수적인 역할을 하며, 데...
Meta Keywords: socket, send, udp, bytes_sent, 소켓을
-->

# Perl에서의 send 명령어: 소켓 통신의 기초

## 개요
`send`는 Perl에서 소켓을 통해 데이터를 전송하는 데 사용되는 함수입니다. 이 함수는 네트워크 프로그래밍 및 IPC(Inter-Process Communication)에서 필수적인 역할을 하며, 데이터를 특정 소켓으로 전송할 수 있도록 합니다.

## 문서화
### 목적
`send` 함수는 클라이언트와 서버 간의 데이터 전송을 가능하게 하며, UDP 및 TCP 소켓을 통해 사용될 수 있습니다. 이 함수는 소켓의 파일 핸들을 통해 전송할 데이터를 지정하고, 전송할 데이터의 길이 및 전송 방식(예: 비동기 전송)을 설정합니다.

### 사용법
```perl
my $bytes_sent = send($socket, $data, $flags);
```
- `$socket`: 데이터를 전송할 소켓의 핸들.
- `$data`: 전송할 데이터. 문자열 형식으로 제공.
- `$flags`: 전송 옵션을 지정하는 플래그. 기본값은 0.

### 세부사항
- `send` 함수는 성공 시 전송된 바이트 수를 반환하며, 실패할 경우 `undef`를 반환하고 `$!` 변수를 통해 에러 메시지를 확인할 수 있습니다.
- 이 함수는 비차단(non-blocking) 모드에서 사용될 수 있으며, 이 경우 전송할 데이터가 부족할 경우 즉시 반환됩니다.
- TCP 소켓의 경우에는 연결된 상태에서만 사용해야 하며, UDP 소켓은 연결이 필요하지 않습니다.

## 예제
### 예제 1: TCP 소켓을 통한 데이터 전송
```perl
use IO::Socket::INET;

# 소켓 생성
my $socket = IO::Socket::INET->new(
    PeerHost => 'localhost',
    PeerPort => '7890',
    Proto    => 'tcp'
) or die "Could not create socket: $!\n";

my $data = "Hello, Server!";
my $bytes_sent = send($socket, $data, 0);

if (defined $bytes_sent) {
    print "Successfully sent $bytes_sent bytes.\n";
} else {
    die "Send failed: $!\n";
}
```

### 예제 2: UDP 소켓을 통한 데이터 전송
```perl
use IO::Socket::INET;

# UDP 소켓 생성
my $socket = IO::Socket::INET->new(
    LocalPort => 7890,
    Proto     => 'udp'
) or die "Could not create socket: $!\n";

my $data = "Hello, UDP Server!";
my $bytes_sent = send($socket, $data, 0, sockaddr_in(7891, inet_aton('localhost')));

if (defined $bytes_sent) {
    print "Successfully sent $bytes_sent bytes via UDP.\n";
} else {
    die "Send failed: $!\n";
}
```

## 설명
- `send` 함수를 사용할 때 가장 흔히 발생하는 오류는 소켓이 올바르게 생성되지 않았거나 연결이 이루어지지 않았을 때 발생합니다.
- 또한, UDP 소켓을 사용할 경우, 데이터가 도착하지 않을 수 있으므로, 전송 후 수신 확인을 통해 데이터 전송을 검증하는 것이 좋습니다.
- 비차단 모드에서 사용할 경우, 전송이 완료되지 않은 상태에서 반환될 수 있으므로 결과를 체크하는 로직이 필요합니다.

## 한 줄 요약
`send`는 Perl에서 소켓을 통해 데이터를 전송하는 기능으로, TCP 및 UDP 소켓 통신에 필수적인 명령어입니다.