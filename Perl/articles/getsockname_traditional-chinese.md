<!--
Meta Description: # Perl 中的 getsockname 函數：用於獲取 Socket 的本地地址 ## 摘要 `getsockname` 是 Perl 中一個重要的函數，用於獲取與特定套接字相關聯的本地地址和端口號。這對於網絡編程非常重要，因為它使程式能夠獲取其所使用的實際網絡資訊。 ## 文件說明 `gets...
Meta Keywords: getsockname, socket, sock, name, perl
-->

# Perl 中的 getsockname 函數：用於獲取 Socket 的本地地址

## 摘要
`getsockname` 是 Perl 中一個重要的函數，用於獲取與特定套接字相關聯的本地地址和端口號。這對於網絡編程非常重要，因為它使程式能夠獲取其所使用的實際網絡資訊。

## 文件說明
`getsockname` 函數的主要目的是從一個已經綁定的套接字中檢索其本地的地址和端口。此函數接收一個套接字作為參數，並將地址資訊填充到指定的變量中。

### 使用方法
```perl
use Socket;

my $sock;  # 假設這是一個已經創建並綁定的套接字
my $name;

# 獲取本地地址
my $result = getsockname($sock, $name);
```

### 參數
- **$sock**: 套接字句柄，必須是有效的套接字。
- **$name**: 將儲存本地地址和端口的變量。

### 返回值
`getsockname` 返回一個真值表示成功，如果失敗則返回 undef，並且可以通過 `$!` 獲取錯誤信息。

## 範例
以下是一個基本的使用範例，展示如何使用 `getsockname` 獲取套接字的本地地址：

```perl
use strict;
use warnings;
use Socket;

# 創建一個 TCP 套接字
socket(my $sock, PF_INET, SOCK_STREAM, getprotobyname('tcp')) or die "Cannot create socket: $!";
bind($sock, sockaddr_in(0, INADDR_ANY)) or die "Cannot bind socket: $!";
listen($sock, SOMAXCONN) or die "Cannot listen on socket: $!";

# 獲取本地地址
my $name;
if (getsockname($sock, $name)) {
    my ($port, $ip) = sockaddr_in($name);
    print "本地地址: " . inet_ntoa($ip) . ", 端口: " . $port . "\n";
} else {
    die "getsockname failed: $!";
}
```

## 解釋
在使用 `getsockname` 時，有幾個常見的注意事項：
- 確保套接字在調用 `getsockname` 之前已經創建並綁定，否則將無法獲得有效的地址資訊。
- 此函數不會為未綁定的套接字提供任何信息。
- 如果函數返回 undef，應檢查 `$!` 獲取具體的錯誤原因。

## 總結
`getsockname` 函數是 Perl 中用於獲取套接字本地地址的重要工具，適用於網絡編程中需要獲取地址和端口資訊的情境。