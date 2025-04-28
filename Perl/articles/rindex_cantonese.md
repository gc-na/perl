<!--
Meta Description: # Perl 中的 rindex 函數：找到字串最後一次出現的位置 ## 概述 `rindex` 是 Perl 中用來查找子字串在父字串中最後一次出現的位置的內建函數。此函數非常有用，當你需要從字串的尾部開始搜尋時。 ## 文檔 ### 目的 `rindex` 函數的主要目的是返回指定子字串在父字串...
Meta Keywords: rindex, position, world, perl, string
-->

# Perl 中的 rindex 函數：找到字串最後一次出現的位置

## 概述
`rindex` 是 Perl 中用來查找子字串在父字串中最後一次出現的位置的內建函數。此函數非常有用，當你需要從字串的尾部開始搜尋時。

## 文檔
### 目的
`rindex` 函數的主要目的是返回指定子字串在父字串中最後一次出現的索引位置。如果子字串未找到，則返回 -1。

### 使用方法
`rindex` 的基本語法如下：

```perl
my $position = rindex($string, $substring, $position);
```

- `$string`：要搜尋的父字串。
- `$substring`：要查找的子字串。
- `$position`（可選）：從哪個位置開始反向搜尋，若未指定，將從字串的末尾開始搜尋。

### 詳細說明
- 返回值：如果找到子字串，返回其在父字串中的索引（從0開始計算），否則返回 -1。
- 索引是從 0 開始計算的，即第一個字符的索引為 0。
- 若提供 `$position`，搜尋將從該索引向前進行。

## 範例
以下是一些 `rindex` 的基本用法示例：

### 示例 1：基本用法
```perl
my $string = "Hello World! World!";
my $position = rindex($string, "World");
print $position;  # 輸出：13
```

### 示例 2：指定起始位置
```perl
my $string = "Hello World! World!";
my $position = rindex($string, "World", 12);
print $position;  # 輸出：6
```

### 示例 3：子字串不存在
```perl
my $string = "Hello World!";
my $position = rindex($string, "Perl");
print $position;  # 輸出：-1
```

## 解釋
在使用 `rindex` 時，可能會遇到以下問題：
- **空字符串**：如果父字串或子字串為空，返回 -1。
- **區分大小寫**：`rindex` 進行區分大小寫的搜尋，這意味著 "world" 和 "World" 是不同的。
- **未找到情況**：如果子字串在父字串中不存在，確保檢查返回值是否為 -1，以避免在後續操作中出錯。

## 總結
`rindex` 是一個強大的 Perl 函數，用於查找子字串在父字串中最後一次出現的位置，對於需要從字串尾部進行搜尋的情況特別有用。