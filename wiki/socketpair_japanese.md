<!--
Meta Description: # Perlにおけるsocketpairの使い方と詳細ガイド ## 概要 `socketpair`は、Perlで双方向の通信を可能にするソケットペアを作成するための関数です。この機能は、プロセス間通信（IPC）やマルチスレッドプログラミングにおいて非常に便利です。 ## ドキュメンテーション ###...
Meta Keywords: socketpair, sock1, sock2, close, af_unix
-->

# Perlにおけるsocketpairの使い方と詳細ガイド

## 概要
`socketpair`は、Perlで双方向の通信を可能にするソケットペアを作成するための関数です。この機能は、プロセス間通信（IPC）やマルチスレッドプログラミングにおいて非常に便利です。

## ドキュメンテーション
### 目的
`socketpair`は、2つの接続されたソケットを作成します。これにより、同一のマシン上で動作するプロセス間でデータの送受信が可能になります。

### 使用法
`socketpair`は、次の形式で使用されます。

```perl
socketpair(SOCKET1, SOCKET2, DOMAIN, TYPE, PROTOCOL);
```

- `SOCKET1`と`SOCKET2`は、作成されるソケットのハンドルを格納する変数です。
- `DOMAIN`は、ソケットのドメインを指定します（通常は`AF_UNIX`）。
- `TYPE`は、ソケットのタイプを指定します（通常は`SOCK_STREAM`または`SOCK_DGRAM`）。
- `PROTOCOL`は、使用するプロトコルを指定します（通常は0）。

### 詳細
`socketpair`は、通常のソケットと同様に動作しますが、特に同一のホスト内でのプロセス間通信に特化しています。作成された2つのソケットは、互いにデータの送受信を行うために使用されます。

## 例
以下は、`socketpair`の基本的な使用例です。

```perl
use IO::Socket;

my ($sock1, $sock2);
socketpair($sock1, $sock2, AF_UNIX, SOCK_STREAM) or die "socketpair: $!";

# 子プロセスを作成
if (my $pid = fork()) {
    # 親プロセス
    close($sock2);
    print $sock1 "Hello from parent\n";
    close($sock1);
} else {
    # 子プロセス
    close($sock1);
    my $line = <$sock2>;
    print "Received: $line";
    close($sock2);
}
```

この例では、親プロセスが子プロセスにメッセージを送信し、子プロセスがそのメッセージを受信して表示します。

## 説明
### よくある落とし穴
- **ドメインの指定**: `AF_UNIX`の代わりに`AF_INET`を使うと、エラーが発生することがあります。
- **ソケットのクローズ**: どちらのソケットも適切にクローズしないと、リソースリークが発生する可能性があります。
- **エラーハンドリング**: `socketpair`が失敗した場合には、エラーメッセージを表示することを忘れないようにしましょう。

## 一文の要約
`socketpair`は、Perlでプロセス間通信を実現するための双方向ソケットを作成する関数です。