<!--
Meta Description: # Perl 中的 getpeername 函數：用於獲取 Socket 的對端地址 ## 概述 `getpeername` 是 Perl 中用於獲取與 socket 連接的對端地址的函數。此函數常用於網絡編程中，幫助開發者獲取與其 socket 相關的遠端主機信息。 ## 文檔 `getpeern...
Meta Keywords: socket, getpeername, perl, peer_address, use
-->

# Perl 中的 getpeername 函數：用於獲取 Socket 的對端地址

## 概述
`getpeername` 是 Perl 中用於獲取與 socket 連接的對端地址的函數。此函數常用於網絡編程中，幫助開發者獲取與其 socket 相關的遠端主機信息。

## 文檔
`getpeername` 函數的主要用途是從已經連接的 socket 中獲取對端的地址和端口信息。它的使用方式如下：

### 語法
```perl
use IO::Socket;

my $socket = IO::Socket::INET->new(
    PeerAddr => 'www.example.com',
    PeerPort => '80',
    Proto    => 'tcp'
) or die "Cannot create socket: $!";

my $peer_address = getpeername($socket);
```

### 參數
- `$socket`：一個已經連接的 socket 對象，通常是通過 `IO::Socket` 模塊創建的。

### 返回值
`getpeername` 返回對端的地址信息，通常以一個二進制格式的字符串存在。開發者可以使用 `Socket` 模塊中的其他函數（如 `unpack`）將其轉換為可讀的格式。

## 範例
這裡有幾個基本的使用範例：

### 範例 1：建立連接並獲取對端地址
```perl
use IO::Socket;
use Socket;

my $socket = IO::Socket::INET->new(
    PeerAddr => 'www.example.com',
    PeerPort => '80',
    Proto    => 'tcp'
) or die "Cannot create socket: $!";

my $peer_address = getpeername($socket);
my ($port, $ip) = unpack_sockaddr_in($peer_address);
print "對端 IP: " . inet_ntoa($ip) . "\n";
print "對端端口: $port\n";
```

### 範例 2：錯誤處理
```perl
use IO::Socket;
use Socket;

my $socket = IO::Socket::INET->new(
    PeerAddr => 'invalid.address',
    PeerPort => '80',
    Proto    => 'tcp'
) or die "Cannot create socket: $!";

my $peer_address = getpeername($socket);
if (defined $peer_address) {
    my ($port, $ip) = unpack_sockaddr_in($peer_address);
    print "對端 IP: " . inet_ntoa($ip) . "\n";
    print "對端端口: $port\n";
} else {
    warn "無法獲取對端地址: $!";
}
```

## 解釋
在使用 `getpeername` 時，有幾個常見的陷阱和注意事項：
- **必須是連接狀態**：`getpeername` 只能在已經連接的 socket 上調用，如果 socket 尚未連接，將無法獲取對端地址。
- **返回值處理**：返回的地址信息需要正確處理，通常需要配合 `unpack_sockaddr_in` 使用，才能獲得可讀的 IP 和端口信息。
- **錯誤處理**：在調用 `getpeername` 時，應該檢查返回值以避免潛在的錯誤，特別是在 socket 失效的情況下。

## 總結
`getpeername` 是一個在 Perl 中用於獲取 socket 對端地址的重要函數，對於網絡編程中的連接管理至關重要。