<!--
Meta Description: # Perl 的 substr 函數：字串操作的利器 ## 摘要 `substr` 是 Perl 語言中的一個內建函數，用於從字串中提取子字串。此函數使得字串的操作變得更加靈活和高效，對於字串處理和解析非常有用。 ## 文件說明 ### 目的 `substr` 函數的主要目的是從給定的字串中提取一部...
Meta Keywords: substr, string, perl, offset, world
-->

# Perl 的 substr 函數：字串操作的利器

## 摘要
`substr` 是 Perl 語言中的一個內建函數，用於從字串中提取子字串。此函數使得字串的操作變得更加靈活和高效，對於字串處理和解析非常有用。

## 文件說明
### 目的
`substr` 函數的主要目的是從給定的字串中提取一部分，這部分可以根據指定的起始位置和長度來決定。該函數不僅可以用來提取字串，還可以用於修改字串的特定部分。

### 使用方法
`substr` 的基本語法如下：

```perl
substr(STRING, OFFSET, LENGTH, REPLACEMENT)
```

- **STRING**：要操作的原始字串。
- **OFFSET**：開始提取的起始位置（從 0 開始計算）。
- **LENGTH**：要提取的子字串長度。如果省略，則將提取從 OFFSET 開始到字串結尾的所有字符。
- **REPLACEMENT**：可選的參數，用於替換從 OFFSET 開始的長度為 LENGTH 的字串。

### 詳細說明
- 當 `LENGTH` 參數被省略時，`substr` 將返回從 `OFFSET` 開始到字串結尾的所有字符。
- 如果 `OFFSET` 為負數，則表示從字串的末尾開始計算位置。
- 使用 `REPLACEMENT` 參數時，可以將指定的字串替換為原字串中的一部分，這使得 `substr` 可以同時用於提取和修改字串。

## 範例
以下是一些 `substr` 的基本使用範例：

### 範例 1：提取子字串
```perl
my $string = "Hello, World!";
my $sub = substr($string, 7, 5);
print $sub;  # 輸出: World
```

### 範例 2：提取到結尾
```perl
my $string = "Hello, World!";
my $sub = substr($string, 7);
print $sub;  # 輸出: World!
```

### 範例 3：使用負數 OFFSET
```perl
my $string = "Hello, World!";
my $sub = substr($string, -6, 5);
print $sub;  # 輸出: World
```

### 範例 4：替換字串
```perl
my $string = "Hello, World!";
substr($string, 7, 5, "Perl");
print $string;  # 輸出: Hello, Perl!
```

## 說明
在使用 `substr` 時，有一些常見的陷阱和注意事項：

- 當 `OFFSET` 超出字串長度時，`substr` 將返回空字串。
- 如果 `LENGTH` 大於可用字符數，則提取的子字串將從 `OFFSET` 開始到字串結尾。
- 確保 `REPLACEMENT` 的長度不會影響其他部分的字串結構，特別是在進行替換操作時。

## 一句總結
`substr` 函數是 Perl 中強大的字串操作工具，能夠有效提取和替換字串的特定部分。