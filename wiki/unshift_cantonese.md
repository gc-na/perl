<!--
Meta Description: # Perl 的 unshift 命令：將元素加到數組的開頭 ## 概述 `unshift` 是 Perl 中的一個內建函數，用於將一個或多個元素添加到數組的開頭，並返回新的數組大小。這使得 `unshift` 在需要在數組開頭插入數據的情況下非常有用。 ## 文檔 ### 目的 `unshift`...
Meta Keywords: unshift, perl, fruits, print, numbers
-->

# Perl 的 unshift 命令：將元素加到數組的開頭

## 概述
`unshift` 是 Perl 中的一個內建函數，用於將一個或多個元素添加到數組的開頭，並返回新的數組大小。這使得 `unshift` 在需要在數組開頭插入數據的情況下非常有用。

## 文檔
### 目的
`unshift` 函數的主要目的是在數組的開頭插入一個或多個元素，從而改變數組的順序。這在需要維護優先級或添加新數據到列表的開頭時特別有用。

### 使用方法
`unshift` 的基本語法如下：
```perl
unshift ARRAY, LIST
```
- `ARRAY` 是你想要操作的數組。
- `LIST` 是要添加到數組開頭的元素，可以是一個或多個元素。

### 詳細說明
- `unshift` 會直接修改原始的數組。
- 返回值是數組的新大小。
- 如果數組未定義，`unshift` 會自動將其初始化為一個空數組。

## 例子
以下是一些 `unshift` 的基本使用範例：

### 範例 1：將單個元素添加到數組
```perl
my @fruits = ("apple", "banana");
unshift(@fruits, "orange");
print "@fruits";  # 輸出: orange apple banana
```

### 範例 2：將多個元素添加到數組
```perl
my @numbers = (2, 3, 4);
unshift(@numbers, 0, 1);
print "@numbers";  # 輸出: 0 1 2 3 4
```

### 範例 3：未初始化數組的情況
```perl
my @empty_array;
unshift(@empty_array, "first");
print "@empty_array";  # 輸出: first
```

## 解釋
- **常見陷阱**：確保數組在使用 `unshift` 之前已正確初始化，否則可能會導致意外行為。
- **效率**：`unshift` 比起在數組尾部添加元素的 `push`，在性能上可能會較慢，因為它需要移動數組中的現有元素。
- **返回值**：注意 `unshift` 的返回值是數組的新大小，而不是新數組的內容。

## 總結
`unshift` 是一個強大的 Perl 函數，用於在數組的開頭添加元素，並返回數組的新大小。