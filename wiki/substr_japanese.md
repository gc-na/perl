<!--
Meta Description: # Perlのsubstr関数: 文字列操作の基本 ## 概要 Perlの`substr`関数は、文字列の特定の部分を抽出したり、置換したりするための強力なツールです。この関数を使用することで、文字列操作を簡単に行うことができます。 ## ドキュメンテーション `substr`は、指定された位置から...
Meta Keywords: substr, perl, string, string2, offset
-->

# Perlのsubstr関数: 文字列操作の基本

## 概要
Perlの`substr`関数は、文字列の特定の部分を抽出したり、置換したりするための強力なツールです。この関数を使用することで、文字列操作を簡単に行うことができます。

## ドキュメンテーション
`substr`は、指定された位置から始まる文字列のサブストリングを取得または置換するための関数です。

### 構文
```perl
substr($string, $offset, $length, $replacement);
```

- **$string**: 操作対象の文字列。
- **$offset**: 抽出または置換を開始する位置（0から始まるインデックス）。
- **$length**: 抽出する文字数。省略した場合、$offsetから文字列の最後までを取得します。
- **$replacement**: （省略可能）指定した位置に挿入する文字列。これを指定すると、該当部分が置換されます。

### 目的
`substr`関数は主に以下の目的で使用されます：
- 文字列の特定の部分を取得する。
- 文字列の一部を別の文字列で置換する。

## 例
### 基本的な使用例

```perl
# 文字列から部分を取得する
my $string = "Perlプログラミング";
my $substring = substr($string, 4, 6); # "プログラ"
print $substring; # 出力: プログラ

# 文字列の一部を置換する
my $string2 = "Hello World";
substr($string2, 6, 5, "Perl");
print $string2; # 出力: Hello Perl
```

## 説明
- **オフセットの指定**: オフセットは0から始まるため、最初の文字はインデックス0に該当します。負の値を指定すると、文字列の末尾からのオフセットとして扱われます。
- **長さの指定**: 長さを指定しない場合、$offsetから文字列の末尾までを取得します。
- **置換の注意点**: 置換を行う場合、指定した長さの文字数が存在しない場合でも、$replacementの文字列がその位置に挿入されます。このため、元の文字列の長さが変わることに注意が必要です。

## 一行まとめ
`substr`は、Perlで文字列の特定部分を抽出または置換するための便利な関数です。