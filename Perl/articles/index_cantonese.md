<!--
Meta Description: # Perl 中的 index 函數：字串搜尋的強大工具 ## 簡介 `index` 函數是 Perl 語言中一個常用的內建函數，用於在字串中搜尋子字串的位置。這個函數對於處理文字和字串操作的程式設計師來說非常有用。 ## 文檔 ### 目的 `index` 函數的主要用途是尋找一個子字串在主要字串...
Meta Keywords: position, index, perl, string, hello
-->

# Perl 中的 index 函數：字串搜尋的強大工具

## 簡介
`index` 函數是 Perl 語言中一個常用的內建函數，用於在字串中搜尋子字串的位置。這個函數對於處理文字和字串操作的程式設計師來說非常有用。

## 文檔
### 目的
`index` 函數的主要用途是尋找一個子字串在主要字串中的首次出現位置。如果找到該子字串，函數會返回其起始位置（以 0 為基礎的索引），如果未找到，則返回 -1。

### 用法
```perl
index STR, SUBSTR [, POSITION]
```
- **STR**：要搜尋的主要字串。
- **SUBSTR**：要尋找的子字串。
- **POSITION**（可選）：從哪個位置開始搜尋，預設值為 0。

### 詳細說明
- `index` 函數是大小寫敏感的，這意味著 "abc" 和 "ABC" 被視為不同的字串。
- 若 `POSITION` 參數的值超過 `STR` 的長度，則返回 -1。
- 若 `SUBSTR` 是空字串，則 `index` 函數將返回 `POSITION` 的值。

## 範例
### 基本用法
```perl
my $string = "Hello, world!";
my $position = index($string, "world");
print $position;  # 輸出 7
```

### 使用 POSITION 參數
```perl
my $string = "Hello, world! Hello again!";
my $position = index($string, "Hello", 10);
print $position;  # 輸出 14
```

### 尋找不存在的子字串
```perl
my $string = "Hello, world!";
my $position = index($string, "Perl");
print $position;  # 輸出 -1
```

## 解釋
在使用 `index` 函數時，常見的陷阱包括：
- 忘記考慮大小寫敏感性，這可能導致意想不到的結果。
- 使用負值或超出範圍的 `POSITION` 參數，這將直接返回 -1。
- 如果在搜尋過程中使用了空字串，會返回 `POSITION` 的值，這可能會引起混淆。

## 一句總結
`index` 函數是 Perl 中一個強大的工具，用於查找字串中子字串的起始位置，並能有效處理各種字串操作需求。