<!--
Meta Description: # Perl 中的 getsockname 函數：用於獲取套接字名稱 ## 概述 `getsockname` 是 Perl 中一個用於獲取現有套接字的本地地址和端口的函數。它對於網絡編程特別重要，因為它可以幫助開發者獲取與套接字相關的位置信息。 ## 文檔 ### 目的 `getsockname` ...
Meta Keywords: getsockname, perl, socket, local_address, port
-->

# Perl 中的 getsockname 函數：用於獲取套接字名稱

## 概述
`getsockname` 是 Perl 中一個用於獲取現有套接字的本地地址和端口的函數。它對於網絡編程特別重要，因為它可以幫助開發者獲取與套接字相關的位置信息。

## 文檔
### 目的
`getsockname` 函數的主要作用是取得與指定的套接字相關聯的本地地址。這在建立和管理網絡連接時非常有用。

### 用法
在 Perl 中使用 `getsockname` 函數時，通常需要先創建一個套接字，然後將其傳遞給該函數。以下是基本的語法：

```perl
getsockname SOCKET
```

- **SOCKET**：一個已經創建的套接字句柄。

### 詳細資訊
`getsockname` 返回一個包含本地地址和端口的列表。這些信息通常以二進制格式返回，因此你可能需要進一步處理以將其轉換為可讀的字符串格式。

## 示例
以下是使用 `getsockname` 的基本示例：

```perl
use IO::Socket;

# 創建一個 TCP 套接字
my $socket = IO::Socket::INET->new(
    LocalPort => 8080,
    Listen    => SOMAXCONN,
    Reuse     => 1
) or die "無法創建套接字：$!";

# 獲取本地地址
my $local_address = getsockname($socket);
my ($port, $ip_address) = sockaddr_in($local_address);

print "本地 IP 地址: " . inet_ntoa($ip_address) . "\n";
print "本地端口: $port\n";
```

## 解釋
使用 `getsockname` 時的常見陷阱包括：

- **未正確創建套接字**：在調用 `getsockname` 之前，必須確保套接字已成功創建，否則函數將返回 `undef`。
- **地址格式**：返回的地址需要使用 `sockaddr_in` 進行解碼，否則將無法獲取可讀的 IP 地址和端口。
- **錯誤處理**：應該在調用 `getsockname` 之後檢查返回值，以確保沒有發生錯誤。

## 總結
`getsockname` 是一個關鍵函數，用於獲取 Perl 中套接字的本地地址和端口資訊。