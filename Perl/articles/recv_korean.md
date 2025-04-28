<!--
Meta Description: # Perl의 recv: 소켓에서 데이터 수신하기 ## 개요 Perl의 `recv` 함수는 소켓을 통해 데이터를 수신하는 데 사용됩니다. 이 함수는 주로 네트워크 프로그래밍에서 클라이언트와 서버 간의 통신을 처리할 때 유용합니다. ## 문서 `recv` 함수는 소켓에서...
Meta Keywords: recv, socket, 데이터, 함수는, length
-->

# Perl의 recv: 소켓에서 데이터 수신하기

## 개요
Perl의 `recv` 함수는 소켓을 통해 데이터를 수신하는 데 사용됩니다. 이 함수는 주로 네트워크 프로그래밍에서 클라이언트와 서버 간의 통신을 처리할 때 유용합니다.

## 문서
`recv` 함수는 소켓에서 들어오는 데이터를 읽어들이는 기능을 제공합니다. 이를 통해 클라이언트가 서버에 요청을 보낼 때, 서버는 클라이언트로부터의 응답을 받을 수 있습니다. 이 함수의 기본적인 사용법은 다음과 같습니다.

### 사용법
```perl
recv(SOCKET, SCALAR, LENGTH, FLAGS)
```

- **SOCKET**: 데이터 수신을 위한 소켓 핸들.
- **SCALAR**: 수신된 데이터가 저장될 변수.
- **LENGTH**: 수신할 최대 바이트 수.
- **FLAGS**: 수신 동작에 대한 플래그 (선택 사항).

### 목적
`recv` 함수는 주로 비동기 소켓 통신을 통해 데이터 수신을 처리하고, 클라이언트와 서버 간의 상호작용을 원활하게 합니다.

## 예제
다음은 `recv` 함수를 사용하는 간단한 예제입니다.

### 예제 1: 기본 수신
```perl
use IO::Socket;

# 소켓 생성
my $socket = IO::Socket::INET->new(
    PeerAddr => 'localhost',
    PeerPort => '7890',
    Proto    => 'tcp',
) or die "소켓 생성 실패: $!";

my $data;
my $length = 1024;

# 데이터 수신
recv($socket, $data, $length, 0) or die "데이터 수신 실패: $!";
print "수신된 데이터: $data\n";

# 소켓 닫기
close($socket);
```

### 예제 2: 비동기 수신
```perl
use IO::Socket;

# 소켓 생성
my $socket = IO::Socket::INET->new(
    LocalPort => '7890',
    Proto     => 'udp',
    Listen     => 1,
) or die "소켓 생성 실패: $!";

while (my $client = $socket->accept()) {
    my $data;
    my $length = 1024;
    
    # 클라이언트로부터 데이터 수신
    recv($client, $data, $length, 0) or die "데이터 수신 실패: $!";
    print "클라이언트로부터 수신된 데이터: $data\n";

    close($client);
}
```

## 설명
- `recv` 함수는 블로킹 모드에서 작동할 때, 데이터가 도착할 때까지 대기합니다. 비동기 방식에서는 `select` 함수를 사용하여 소켓의 준비 상태를 확인할 수 있습니다.
- 수신할 데이터의 길이를 초과하여 `recv`를 호출하면 최대 길이만큼의 데이터만 수신됩니다.
- `recv`는 UDP 소켓에서도 사용될 수 있으며, 이 경우 비연결형 데이터 전송을 처리합니다.

## 한줄 요약
Perl의 `recv` 함수는 소켓을 통해 데이터를 수신하는 데 사용되며, 네트워크 프로그래밍에서 중요한 역할을 합니다.