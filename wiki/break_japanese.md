# [UNIX] C Shell (csh) break の使い方: ループを終了する

## Overview
`break` コマンドは、C シェルのループを終了するために使用されます。特定の条件が満たされたときにループを中断し、次のコマンドに制御を移すことができます。

## Usage
基本的な構文は以下の通りです。

```csh
break [options]
```

## Common Options
`break` コマンドには特にオプションはありませんが、ループの中で使用されることが一般的です。

## Common Examples

### 例 1: 簡単なループの中での使用
```csh
foreach i (1 2 3 4 5)
    if ($i == 3) then
        break
    endif
    echo $i
end
```
この例では、1から5までの数字をループしますが、3に達した時点でループを終了します。

### 例 2: while ループでの使用
```csh
set count = 0
while ($count < 5)
    @ count++
    if ($count == 3) then
        break
    endif
    echo $count
end
```
このコードは、カウントが3に達したときにループを終了します。

### 例 3: ネストされたループでの使用
```csh
foreach i (1 2)
    foreach j (1 2 3)
        if ($j == 2) then
            break
        endif
        echo "$i $j"
    end
end
```
この例では、内側のループが2に達したときに終了します。

## Tips
- `break` コマンドは、特に条件付きループで非常に便利です。
- ループの中で複数の条件をチェックする場合、`break` を適切に使用して、必要なタイミングでループを終了させましょう。
- ネストされたループの場合、`break` は最も内側のループのみを終了しますので、注意が必要です。