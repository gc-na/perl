# [台灣] C Shell (csh) case 用法: 根據模式執行命令

## Overview
`case` 命令用於根據指定的模式來匹配變數的值，並執行相應的命令。這在需要根據不同情況執行不同操作時非常有用。

## Usage
基本語法如下：

```csh
case [變數] in
    [模式1] ) [命令1];;
    [模式2] ) [命令2];;
    ...
    * ) [預設命令];;
esac
```

## Common Options
`case` 命令本身沒有特定的選項，但可以根據需要使用不同的模式來匹配變數的值。

## Common Examples

### 示例 1: 簡單的模式匹配
```csh
set fruit = "apple"
case $fruit in
    apple ) echo "這是一個蘋果";;
    banana ) echo "這是一根香蕉";;
    * ) echo "這不是蘋果或香蕉";;
esac
```

### 示例 2: 處理多個選項
```csh
set day = "Monday"
case $day in
    Monday | Tuesday | Wednesday ) echo "這是工作日";;
    Saturday | Sunday ) echo "這是週末";;
    * ) echo "未知的日子";;
esac
```

### 示例 3: 根據檔案擴展名執行不同命令
```csh
set file = "document.txt"
case $file in
    *.txt ) echo "這是一個文本檔案";;
    *.jpg ) echo "這是一個圖片檔案";;
    * ) echo "未知的檔案類型";;
esac
```

## Tips
- 使用 `|` 符號可以在同一模式中匹配多個選項，這樣可以簡化代碼。
- 確保在每個模式後面使用 `;;` 來結束該模式的命令。
- 使用 `*` 作為預設模式，可以捕捉所有未匹配的情況，這樣可以避免錯過任何情況。