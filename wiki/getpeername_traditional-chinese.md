<!--
Meta Description: # getpeername：Perl 中的套接字函數 ## 概述 `getpeername` 是一個 Perl 中用於獲取與套接字連接的對等方地址的系統調用。此函數在網絡編程中非常重要，特別是在處理客戶端和伺服器之間的通信時。 ## 文檔 ### 目的 `getpeername` 函數的主要目的是獲...
Meta Keywords: getpeername, socket, perl, use, peer_addr
-->

# getpeername：Perl 中的套接字函數

## 概述
`getpeername` 是一個 Perl 中用於獲取與套接字連接的對等方地址的系統調用。此函數在網絡編程中非常重要，特別是在處理客戶端和伺服器之間的通信時。

## 文檔
### 目的
`getpeername` 函數的主要目的是獲取與指定套接字相連的對等設備的地址資訊。這通常用於確定連接的來源，例如在伺服器端識別客戶端的 IP 地址和端口號。

### 使用方法
`getpeername` 函數的基本語法如下：
```perl
use IO::Socket;

my $socket = IO::Socket::INET->new(
    PeerAddr => '127.0.0.1',
    PeerPort => '8080',
    Proto    => 'tcp',
) or die "無法建立連接: $!";

my $peer_addr = getpeername($socket);
```

### 參數
- `$socket`: 要獲取對等地址的套接字對象。

### 返回值
此函數返回一個包含對等方地址的二進制字符串。如果失敗，則返回 `undef`，並設置 `$!` 為錯誤代碼。

### 相關模塊
- `IO::Socket`: 提供了與套接字操作相關的功能。

## 範例
以下是使用 `getpeername` 的基本範例：

```perl
use IO::Socket;
use Socket;

my $server = IO::Socket::INET->new(
    LocalAddr => '127.0.0.1',
    LocalPort => 8080,
    Proto     => 'tcp',
    Listen    => 5,
) or die "無法建立伺服器: $!";

while (my $client = $server->accept()) {
    my $peer_addr = getpeername($client);
    my ($port, $iaddr) = sockaddr_in($peer_addr);
    my $ip_address = inet_ntoa($iaddr);
    
    print "連接來自: $ip_address, 端口: $port\n";
    close($client);
}
```

## 解釋
使用 `getpeername` 時，需要注意以下幾點：
- 確保傳入的套接字是有效的並且已經連接。
- 如果套接字沒有連接，則 `getpeername` 將會失敗，返回 `undef`。
- 在處理返回的地址時，通常需要使用 `sockaddr_in` 和 `inet_ntoa` 函數將二進制地址轉換為可讀的 IP 地址格式。

## 一句總結
`getpeername` 是 Perl 中一個重要的函數，用於獲取與套接字相連的對等方的地址資訊，廣泛應用於網絡通信的開發中。