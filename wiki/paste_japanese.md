# [Unix系] C Shell (csh) paste 使用法: 複数ファイルを結合する

## Overview
`paste` コマンドは、複数のファイルを行単位で結合し、タブ区切りで出力するために使用されます。このコマンドは、テキストファイルの内容を横に並べて表示するのに便利です。

## Usage
基本的な構文は以下の通りです。

```
paste [options] [arguments]
```

## Common Options
- `-d` : 区切り文字を指定します。デフォルトはタブです。
- `-s` : 各ファイルの行を縦に結合します。
- `-z` : 入力の終端を null 文字（\0）で指定します。

## Common Examples
以下は `paste` コマンドのいくつかの実用的な例です。

### 例1: 複数ファイルの結合
```bash
paste file1.txt file2.txt
```
このコマンドは、`file1.txt` と `file2.txt` の内容を行ごとに結合して表示します。

### 例2: 区切り文字の指定
```bash
paste -d ',' file1.txt file2.txt
```
このコマンドは、カンマで区切って `file1.txt` と `file2.txt` を結合します。

### 例3: 縦に結合
```bash
paste -s file1.txt file2.txt
```
このコマンドは、`file1.txt` と `file2.txt` の内容を縦に結合して表示します。

### 例4: null 文字での結合
```bash
paste -z file1.txt file2.txt
```
このコマンドは、null 文字を使用して `file1.txt` と `file2.txt` を結合します。

## Tips
- 複数のファイルを結合する際は、ファイルの行数が異なる場合、短いファイルは空白で埋められます。
- 結合結果を新しいファイルに保存したい場合は、リダイレクトを使用できます。
  ```bash
  paste file1.txt file2.txt > output.txt
  ```
- 区切り文字をカスタマイズすることで、出力形式を柔軟に変更できます。