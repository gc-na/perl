# [Unix系] C Shell (csh) endsw の使い方: 条件分岐の終了を示す

## 概要
`endsw` コマンドは、C Shell スクリプトにおいて条件分岐の終了を示すために使用されます。`switch` 文のブロックを終了させるために必要な構文です。

## 使用法
基本的な構文は以下の通りです。

```
endsw
```

## 一般的なオプション
`endsw` には特にオプションはありません。単純に `endsw` と記述することで、`switch` 文の終了を示します。

## 一般的な例
以下に、`endsw` を使用したいくつかの実用的な例を示します。

### 例1: 基本的な switch 文
```csh
set var = "apple"
switch ($var)
    case "apple":
        echo "This is an apple."
        breaksw
    case "banana":
        echo "This is a banana."
        breaksw
    default:
        echo "Unknown fruit."
endsw
```

### 例2: 複数の条件
```csh
set num = 2
switch ($num)
    case 1:
        echo "Number is one."
        breaksw
    case 2:
        echo "Number is two."
        breaksw
    case 3:
        echo "Number is three."
        breaksw
    default:
        echo "Number is not one, two, or three."
endsw
```

## ヒント
- `endsw` は必ず `switch` 文の後に記述してください。これにより、条件分岐が正しく終了します。
- `breaksw` を使用して、各ケースの処理を終了させることを忘れないでください。これにより、次のケースに進むことを防ぎます。
- 複雑な条件分岐を行う場合は、適切にインデントを使用して可読性を向上させましょう。