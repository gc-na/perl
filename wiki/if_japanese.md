# [Unix系] C Shell (csh) if コマンド: 条件分岐を実行する

## Overview
`if` コマンドは、特定の条件が真であるかどうかを評価し、その結果に基づいてコマンドを実行するための制御構文です。これにより、スクリプト内で条件に応じた処理を行うことができます。

## Usage
基本的な構文は次のとおりです。

```
if (条件) then
    コマンド
endif
```

## Common Options
- `then`: 条件が真の場合に実行するコマンドを開始するために使用します。
- `endif`: `if` 文の終了を示します。

## Common Examples

### 例1: 簡単な条件分岐
```csh
set var = 10
if ($var > 5) then
    echo "変数は5より大きい"
endif
```

### 例2: ファイルの存在チェック
```csh
if (-e "file.txt") then
    echo "file.txt は存在します"
else
    echo "file.txt は存在しません"
endif
```

### 例3: 複数の条件を使用
```csh
set num = 20
if ($num < 10) then
    echo "numは10未満です"
else if ($num == 20) then
    echo "numは20です"
else
    echo "numは10以上かつ20未満です"
endif
```

## Tips
- 条件式はカッコで囲む必要があります。
- `else` や `else if` を使用することで、より複雑な条件分岐を作成できます。
- スクリプトの可読性を高めるために、適切にインデントを使用しましょう。