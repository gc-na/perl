<!--
Meta Description: # Perl 的 substr 函數：字符串操作的利器 ## 簡介 `substr` 是 Perl 中用於截取字符串的內建函數，能夠有效地從給定字符串中提取指定範圍的子字符串。 ## 文檔 ### 目的 `substr` 函數的主要目的是從一個字符串中提取出部分內容，這對於字符串處理和數據操作非常有...
Meta Keywords: substr, perl, string, offset, world
-->

# Perl 的 substr 函數：字符串操作的利器

## 簡介
`substr` 是 Perl 中用於截取字符串的內建函數，能夠有效地從給定字符串中提取指定範圍的子字符串。

## 文檔
### 目的
`substr` 函數的主要目的是從一個字符串中提取出部分內容，這對於字符串處理和數據操作非常有用。

### 使用方法
```perl
substr(EXPRESSION, OFFSET, LENGTH, REPLACEMENT);
```
- **EXPRESSION**：要操作的原始字符串。
- **OFFSET**：開始提取的索引，從 0 開始。如果值為負數，則從字符串的末尾開始計算。
- **LENGTH**：要提取的字符數。如果省略，則提取從 OFFSET 開始到字符串末尾的所有字符。
- **REPLACEMENT**（可選）：如果提供，則會用此字符串替換指定的子字符串，並返回替換後的字符串。

### 詳細資訊
`substr` 函數在處理字符串時提供了靈活性，支持從任意位置開始提取子字符串，並且可以選擇性地進行替換操作。此函數對於解析和修改字符串內容非常有用，特別是在數據清洗和格式化時。

## 示例
### 基本用法
```perl
my $string = "Hello, World!";
my $substring = substr($string, 7, 5);
print $substring;  # 輸出: World
```

### 使用 OFFSET 和 LENGTH
```perl
my $string = "Perl Programming";
my $part = substr($string, 5, 11);
print $part;  # 輸出: Programming
```

### 使用負數 OFFSET
```perl
my $string = "Hello, World!";
my $last_chars = substr($string, -6);
print $last_chars;  # 輸出: World!
```

### 替換子字符串
```perl
my $string = "Hello, World!";
substr($string, 7, 5, "Perl");
print $string;  # 輸出: Hello, Perl!
```

## 解釋
在使用 `substr` 時，開發者應注意以下幾點：
- 使用負數 OFFSET 會從字符串的末尾計算，這可能會導致意外的結果，特別是在處理變長字符串時。
- 當 LENGTH 超出原始字符串的範圍時，`substr` 只會返回從 OFFSET 開始到字符串末尾的部分。
- 如果 OFFSET 超出字符串長度，`substr` 會返回空字符串。

## 一句總結
`substr` 是 Perl 中用於提取和替換字符串部分的強大工具，靈活且易於使用。