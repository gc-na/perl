<!--
Meta Description: # Perl中的getpeername函数详解 ## 概述 `getpeername` 是 Perl 中用于获取与套接字连接的对等方（peer）地址的函数。它通常用于网络编程，以便了解与本地套接字连接的远程主机的信息。 ## 文档 ### 目的 `getpeername` 函数的主要目的是返回与指定...
Meta Keywords: getpeername, socket, sock, peer_address, peer_sockaddr
-->

# Perl中的getpeername函数详解

## 概述
`getpeername` 是 Perl 中用于获取与套接字连接的对等方（peer）地址的函数。它通常用于网络编程，以便了解与本地套接字连接的远程主机的信息。

## 文档
### 目的
`getpeername` 函数的主要目的是返回与指定套接字连接的对等方的地址信息。这在进行网络通信时非常重要，因为它允许程序获取远程主机的 IP 地址和端口号。

### 用法
`getpeername` 的基本语法如下：
```perl
use Socket;

my $sock = ...;  # 需要是一个已连接的套接字
my $peer_address = getpeername($sock);

# 将地址转换为可读格式
my $peer_sockaddr = sockaddr_in($peer_address);
my ($port, $ip) = unpack_sockaddr_in($peer_sockaddr);
```
在这个例子中，`$sock` 是一个已经连接的套接字，`getpeername` 会返回该套接字连接的对等方的地址信息。

### 详细说明
- **参数**: `getpeername` 接受一个套接字作为参数，并返回一个包含对等方地址信息的字节串。
- **返回值**: 如果成功，返回对等方的地址信息；如果失败，返回 `undef`，并且 `$!` 包含错误信息。
- **注意**: 使用 `getpeername` 前，确保套接字已成功连接。

## 示例
### 示例1：获取对等方地址
```perl
use IO::Socket;
use Socket;

my $sock = IO::Socket::INET->new(
    PeerAddr => 'www.example.com',
    PeerPort => '80',
    Proto    => 'tcp'
) or die "Cannot create socket: $!";

my $peer_address = getpeername($sock);
my $peer_sockaddr = sockaddr_in($peer_address);
my ($port, $ip) = unpack_sockaddr_in($peer_sockaddr);

print "对等方IP: $ip\n";
print "对等方端口: $port\n";
```

### 示例2：处理错误
```perl
use IO::Socket;
use Socket;

my $sock = IO::Socket::INET->new(
    LocalPort => 8080,
    Proto     => 'tcp',
    Listen    => 1,
    Reuse     => 1
) or die "Cannot create socket: $!";

my $client = $sock->accept();
my $peer_address = getpeername($client);

if (defined $peer_address) {
    my $peer_sockaddr = sockaddr_in($peer_address);
    my ($port, $ip) = unpack_sockaddr_in($peer_sockaddr);
    print "连接来自 IP: $ip 端口: $port\n";
} else {
    print "获取对等方地址失败: $!\n";
}
```

## 说明
- **常见问题**: 使用 `getpeername` 时，确保套接字确实已连接，否则可能会返回 `undef`。
- **错误处理**: 在调用 `getpeername` 后应检查返回值，并根据需要处理错误信息。
- **网络环境**: 不同的网络环境可能会影响套接字连接的稳定性，因此请确保进行充分的测试。

## 一句话总结
`getpeername` 是 Perl 中用于获取与套接字连接的对等方地址信息的重要函数。