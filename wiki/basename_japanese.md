# [UNIX系] C Shell (csh) basename の使い方: ファイル名の抽出

## 概要
`basename` コマンドは、指定したパスからファイル名を抽出するためのコマンドです。これにより、パスの情報を取り除き、純粋なファイル名だけを取得することができます。

## 使用法
基本的な構文は以下の通りです。

```
basename [options] [arguments]
```

## 一般的なオプション
- `-a` : 複数の引数を指定した場合、すべてのファイル名を抽出します。
- `-s` : 指定したサフィックスを削除します。

## 一般的な例
以下に、`basename` コマンドのいくつかの実用的な例を示します。

### 例1: 単一のファイル名を取得
```csh
basename /usr/local/bin/script.sh
```
出力:
```
script.sh
```

### 例2: サフィックスを削除
```csh
basename /usr/local/bin/script.sh .sh
```
出力:
```
script
```

### 例3: 複数のファイル名を取得
```csh
basename -a /usr/local/bin/script.sh /usr/local/bin/another_script.sh
```
出力:
```
script.sh
another_script.sh
```

## ヒント
- `basename` コマンドは、スクリプト内でファイル名を処理する際に非常に便利です。
- サフィックスを指定することで、特定の拡張子を持つファイル名を簡単に取得できます。
- 複数のファイルを一度に処理する場合は、`-a` オプションを活用しましょう。