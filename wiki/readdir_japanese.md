<!--
Meta Description: # Perlにおけるreaddir関数の完全ガイド ## 概要 `readdir`は、Perlでディレクトリの内容を読み取るための関数です。この関数を使用することで、指定したディレクトリ内のファイルやサブディレクトリのリストを取得できます。 ## ドキュメンテーション ### 目的 `readdir...
Meta Keywords: readdir, file, dir_handle, directory, opendir
-->

# Perlにおけるreaddir関数の完全ガイド

## 概要
`readdir`は、Perlでディレクトリの内容を読み取るための関数です。この関数を使用することで、指定したディレクトリ内のファイルやサブディレクトリのリストを取得できます。

## ドキュメンテーション
### 目的
`readdir`は、オープンしたディレクトリハンドルから次のエントリを取得するために使用されます。この関数は、ファイルシステム内のディレクトリを操作する際に非常に便利です。

### 使用法
`readdir`関数は、以下の形式で使用されます：

```perl
my $dir_handle; 
opendir($dir_handle, '/path/to/directory') or die "Cannot open directory: $!";
while (my $entry = readdir($dir_handle)) {
    print "$entry\n";
}
closedir($dir_handle);
```

### 詳細
- `opendir`関数により、指定したディレクトリがオープンされ、ディレクトリハンドルが作成されます。
- `readdir`は、ディレクトリハンドルが指すディレクトリから一つのエントリを取得します。すべてのエントリが読み取られるまで呼び出しを続けます。
- エントリには、`.`（現在のディレクトリ）および`..`（親ディレクトリ）が含まれるため、これらの処理が必要な場合もあります。
- 最後に`closedir`を使ってディレクトリを閉じることを忘れないでください。

## 例
### 基本的な使用例
以下は、指定したディレクトリ内のファイルをリストする基本的なスクリプトです。

```perl
my $dir = '/path/to/directory';
opendir(my $dh, $dir) or die "Cannot open directory: $!";
while (my $file = readdir($dh)) {
    next if ($file eq '.' || $file eq '..'); # 現在のディレクトリと親ディレクトリをスキップ
    print "$file\n";
}
closedir($dh);
```

## 説明
### 一般的な落とし穴
- `readdir`は、オープンしているディレクトリハンドルに対してのみ使用可能です。ディレクトリがオープンされていない状態で呼び出すと、エラーが発生します。
- 返されるエントリには、`.`および`..`が含まれるため、必要に応じてフィルタリングする必要があります。
- `readdir`は、エントリを1つずつ返しますが、配列としてまとめて取得することはできません。全エントリを一度に取得したい場合は、`readdir`関数（`File::Basename`モジュール）を検討してください。

## 一文での要約
`readdir`は、Perlでディレクトリの内容を逐次的に読み取るための関数です。