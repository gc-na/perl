<!--
Meta Description: # Perl의 fileno 함수: 파일 핸들의 정수 식별자 가져오기 ## 개요 Perl의 `fileno` 함수는 파일 핸들에 대한 정수 식별자를 반환합니다. 이 함수는 파일 핸들로부터 파일 디스크립터를 얻는 데 유용하며, 파일의 상태를 검사하거나 저수준의 I/O 작업을...
Meta Keywords: fileno, socket, 함수는, 디스크립터를, undef
-->

# Perl의 fileno 함수: 파일 핸들의 정수 식별자 가져오기

## 개요
Perl의 `fileno` 함수는 파일 핸들에 대한 정수 식별자를 반환합니다. 이 함수는 파일 핸들로부터 파일 디스크립터를 얻는 데 유용하며, 파일의 상태를 검사하거나 저수준의 I/O 작업을 수행할 때 사용됩니다.

## 문서화
### 목적
`fileno` 함수는 주어진 파일 핸들에 대한 파일 디스크립터를 반환합니다. 이 파일 디스크립터는 운영 체제에서 파일이나 소켓을 식별하는 데 사용되는 정수 값입니다.

### 사용법
함수의 기본 문법은 다음과 같습니다:

```perl
my $fileno = fileno($fh);
```

여기서 `$fh`는 파일 핸들입니다. 함수는 성공적으로 파일 디스크립터를 찾으면 해당 값을 반환하고, 실패할 경우 `undef`를 반환합니다.

### 세부 사항
- `fileno`는 읽기 전용 파일 핸들, 쓰기 전용 파일 핸들 또는 양방향 파일 핸들 모두에 대해 사용할 수 있습니다.
- 파일 핸들이 `undef`인 경우, `fileno`는 `undef`를 반환합니다.
- 소켓 핸들에 대해서도 `fileno`를 사용할 수 있습니다.
- Perl의 `IO::Handle` 모듈을 사용하는 경우, `fileno` 메서드를 통해서도 파일 디스크립터를 얻을 수 있습니다.

## 예제
다음은 `fileno` 함수의 기본 사용 예제입니다.

### 예제 1: 파일 핸들로부터 파일 디스크립터 얻기
```perl
open my $fh, '<', 'example.txt' or die "Cannot open file: $!";
my $fileno = fileno($fh);
print "File descriptor: $fileno\n";
close $fh;
```

### 예제 2: 소켓 핸들에 대한 파일 디스크립터 얻기
```perl
use IO::Socket::INET;

my $socket = IO::Socket::INET->new(
    PeerAddr => 'localhost',
    PeerPort => '8080',
    Proto    => 'tcp',
) or die "Cannot create socket: $!";

my $fileno = fileno($socket);
print "Socket file descriptor: $fileno\n";
close $socket;
```

## 설명
- `fileno`를 사용할 때 주의해야 할 점은 파일 핸들이 유효하지 않거나 이미 닫힌 경우 `undef`를 반환한다는 것입니다. 따라서 반환 값이 `undef`인지 확인하는 것이 중요합니다.
- `fileno`는 시스템 호출에 의존하기 때문에, 운영 체제에 따라 다르게 동작할 수 있습니다. 예를 들어, POSIX 시스템에서는 파일 디스크립터가 0부터 시작하는 반면, 다른 시스템에서는 다를 수 있습니다.

## 한 줄 요약
`fileno` 함수는 Perl에서 파일 핸들로부터 해당 파일의 정수 식별자인 파일 디스크립터를 반환하는 함수입니다.