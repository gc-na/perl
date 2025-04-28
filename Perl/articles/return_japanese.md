<!--
Meta Description: # Perlの「return」: 戻り値の制御 ## 概要 Perlにおける「return」文は、サブルーチンからの戻り値を指定し、呼び出し元に制御を戻すために使用されます。これにより、サブルーチンの実行結果を利用したり、制御フローを管理することができます。 ## ドキュメンテーション ### 目的...
Meta Keywords: return, perl, sub, numerator, denominator
-->

# Perlの「return」: 戻り値の制御

## 概要
Perlにおける「return」文は、サブルーチンからの戻り値を指定し、呼び出し元に制御を戻すために使用されます。これにより、サブルーチンの実行結果を利用したり、制御フローを管理することができます。

## ドキュメンテーション
### 目的
「return」文は、サブルーチン内で計算された値を返すために使用されます。サブルーチンが正常に終了した場合、その結果を呼び出し元に返すことができます。

### 使用法
```perl
sub example_sub {
    my $value = shift;  # 引数を取得
    return $value * 2;  # 引数の2倍を返す
}
```

この例では、`example_sub`というサブルーチンが引数を受け取り、その値の2倍を返します。

### 詳細
- **戻り値の型**: Perlでは、戻り値としてスカラー、配列、ハッシュなど、任意のデータ型を返すことができます。
- **複数の戻り値**: 複数の値を返す場合、リストコンテキストで使用できます。
  ```perl
  sub multi_return {
      return (1, 2, 3);
  }

  my ($a, $b, $c) = multi_return();  # $a=1, $b=2, $c=3
  ```

## 例
### 基本的な使用例
```perl
sub add {
    my ($x, $y) = @_;
    return $x + $y;  # 2つの引数の合計を返す
}

my $result = add(5, 10);  # $resultは15
print $result;  # 出力: 15
```

### 複数の戻り値の例
```perl
sub divide {
    my ($numerator, $denominator) = @_;
    return ($numerator / $denominator, $numerator % $denominator);  # 商と余りを返す
}

my ($quotient, $remainder) = divide(10, 3);  # $quotientは3, $remainderは1
```

## 説明
- **戻り値がない場合**: `return`文を省略すると、最後に評価された式の値が自動的に戻り値となりますが、明示的に`return`文を使用することが推奨されます。
- **スコープの注意**: `return`は、サブルーチンのスコープ内でのみ有効であり、他のスコープからはアクセスできません。

## ワンライナーサマリー
Perlの「return」文は、サブルーチンからの戻り値を明示的に指定し、制御を呼び出し元に戻すために使用されます。