# [日本語] C Shell (csh) grep 使用法: テキスト内のパターン検索

## Overview
`grep` コマンドは、指定したパターンに一致する行をファイルから検索するためのツールです。テキストデータの中から特定の情報を見つけるのに非常に便利です。

## Usage
基本的な構文は以下の通りです。

```csh
grep [options] [arguments]
```

## Common Options
- `-i`: 大文字と小文字を区別せずに検索します。
- `-v`: 指定したパターンに一致しない行を表示します。
- `-r`: ディレクトリ内のファイルを再帰的に検索します。
- `-n`: 一致した行の行番号を表示します。
- `-l`: 一致したファイル名のみを表示します。

## Common Examples
以下にいくつかの実用的な例を示します。

### 例1: 基本的な検索
特定のファイル内で「example」という単語を検索します。
```csh
grep "example" filename.txt
```

### 例2: 大文字と小文字を区別しない検索
大文字と小文字を無視して「example」を検索します。
```csh
grep -i "example" filename.txt
```

### 例3: 行番号を表示
一致した行の行番号を表示します。
```csh
grep -n "example" filename.txt
```

### 例4: ディレクトリ内の再帰的検索
指定したディレクトリ内の全ファイルから「example」を検索します。
```csh
grep -r "example" /path/to/directory
```

### 例5: 一致しない行を表示
「example」を含まない行を表示します。
```csh
grep -v "example" filename.txt
```

## Tips
- 検索パターンに正規表現を使うと、より柔軟な検索が可能です。
- 複数のファイルを同時に検索することもできます。ファイル名をスペースで区切って指定してください。
- 結果をファイルにリダイレクトすることで、検索結果を保存できます。例えば、`grep "example" filename.txt > results.txt` のように使用します。