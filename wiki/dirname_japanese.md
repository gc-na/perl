# [UNIX] C Shell (csh) dirname の使い方: パスからディレクトリ名を取得する

## Overview
`dirname` コマンドは、指定したパスからディレクトリ名を抽出するためのコマンドです。ファイルのフルパスが与えられたときに、そのファイルが存在するディレクトリのパスを返します。

## Usage
基本的な構文は次の通りです。

```
dirname [options] [arguments]
```

## Common Options
- `-z` : 出力をゼロバイトで区切ります。
- `--help` : ヘルプメッセージを表示します。
- `--version` : バージョン情報を表示します。

## Common Examples
以下に、`dirname` コマンドのいくつかの実用的な例を示します。

1. フルパスからディレクトリ名を取得する:
   ```csh
   dirname /home/user/documents/file.txt
   ```
   出力:
   ```
   /home/user/documents
   ```

2. 相対パスからディレクトリ名を取得する:
   ```csh
   dirname ./projects/code/main.c
   ```
   出力:
   ```
   ./projects/code
   ```

3. 複数のパスを指定する:
   ```csh
   dirname /var/log/syslog /etc/hosts
   ```
   出力:
   ```
   /var/log
   /etc
   ```

## Tips
- `dirname` コマンドは、スクリプト内でファイルのディレクトリを動的に取得するのに便利です。
- 複数の引数を指定すると、それぞれのディレクトリ名が別々の行に出力されます。
- `dirname` を他のコマンドと組み合わせて使用することで、より複雑な処理を簡単に行うことができます。