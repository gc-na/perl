<!--
Meta Description: # Perlのgetsockname関数: ソケットのローカルアドレスを取得する方法 ## 概要 `getsockname`は、Perlのソケットプログラミングにおいて、ソケットのローカルアドレスを取得するための関数です。この関数を使用することで、バインドされたアドレス情報を確認することができます。...
Meta Keywords: getsockname, socket, port, sockaddr_in, bind
-->

# Perlのgetsockname関数: ソケットのローカルアドレスを取得する方法

## 概要
`getsockname`は、Perlのソケットプログラミングにおいて、ソケットのローカルアドレスを取得するための関数です。この関数を使用することで、バインドされたアドレス情報を確認することができます。

## ドキュメント
`getsockname`は、指定されたソケットのローカルアドレスを取得するために使用されます。この関数は、ソケットがバインドされたアドレスを返し、通常はIPアドレスとポート番号から構成されます。

### 使用法
以下の手順で`getsockname`を使用します：

1. ソケットを作成する。
2. ソケットにアドレスをバインドする。
3. `getsockname`を呼び出してローカルアドレスを取得する。

### 詳細
```perl
use Socket;

# ソケットの作成
socket(SOCK, PF_INET, SOCK_STREAM, 0) or die "Socket creation failed: $!";
my $port = 8080;
my $addr = sockaddr_in($port, INADDR_ANY);

# ソケットにバインド
bind(SOCK, $addr) or die "Bind failed: $!";

# ローカルアドレスの取得
my $local_addr = getsockname(SOCK);
my ($local_port, $local_ip) = sockaddr_in($local_addr);

print "Local Address: ", inet_ntoa($local_ip), " Port: ", $local_port, "\n";
```

## 例
以下は`getsockname`の基本的な使用例です。

### 例1: ソケットのローカルアドレスを取得
```perl
use Socket;

socket(SOCK, PF_INET, SOCK_STREAM, 0) or die "Socket creation failed: $!";
bind(SOCK, sockaddr_in(0, INADDR_ANY)) or die "Bind failed: $!";

my $local_addr = getsockname(SOCK);
my ($local_port, $local_ip) = sockaddr_in($local_addr);

print "Local IP: ", inet_ntoa($local_ip), "\n";
print "Local Port: ", $local_port, "\n";
```

### 例2: サーバーソケットのバインドと取得
```perl
use Socket;

my $port = 9090;
socket(SERVER, PF_INET, SOCK_STREAM, 0) or die "Socket creation failed: $!";
bind(SERVER, sockaddr_in($port, INADDR_ANY)) or die "Bind failed: $!";

my $local_addr = getsockname(SERVER);
my ($local_port, $local_ip) = sockaddr_in($local_addr);

print "Server is running on IP: ", inet_ntoa($local_ip), " Port: ", $local_port, "\n";
```

## 説明
`getsockname`を使用する際の一般的な落とし穴には、以下のようなものがあります：

- **バインド前に呼び出す**: `getsockname`を呼び出す前に、必ず`bind`関数でソケットにアドレスをバインドしてください。
- **エラーハンドリング**: ソケット操作は失敗することがあるため、適切なエラーハンドリングを行うことが重要です。
- **アドレス形式の理解**: 取得したアドレスは、`sockaddr_in`形式であるため、`inet_ntoa`を使って人間が読める形に変換する必要があります。

## まとめ
`getsockname`は、Perlでソケットプログラミングを行う際に、ソケットのローカルアドレスを取得するための便利な関数です。