# [Unix系] C Shell (csh) rev コマンド: 文字列を逆に表示する

## Overview
`rev` コマンドは、入力された各行の文字列を逆に表示するためのコマンドです。主にテキスト処理やデバッグの際に役立ちます。

## Usage
基本的な構文は以下の通りです。

```
rev [options] [arguments]
```

## Common Options
- `-` : 標準入力からデータを読み取ります。
- `-o <file>` : 逆にした結果を指定したファイルに出力します。

## Common Examples
以下に `rev` コマンドのいくつかの実用的な例を示します。

### 例1: 標準入力からの逆表示
```bash
echo "Hello, World!" | rev
```
出力:
```
!dlroW ,olleH
```

### 例2: ファイルの内容を逆に表示
```bash
rev example.txt
```
このコマンドは `example.txt` の各行を逆に表示します。

### 例3: 結果をファイルに出力
```bash
rev example.txt -o reversed.txt
```
このコマンドは `example.txt` の内容を逆にし、`reversed.txt` に保存します。

## Tips
- `rev` コマンドはパイプと組み合わせて使用すると便利です。他のコマンドの出力を逆にすることができます。
- 大きなファイルを処理する際は、出力をファイルにリダイレクトすることで、結果を保存しやすくなります。