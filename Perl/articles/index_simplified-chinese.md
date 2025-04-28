<!--
Meta Description: # Perl 中的 index 函数：查找子字符串的强大工具 ## 摘要 `index` 是 Perl 中用于查找字符串中子字符串位置的内置函数，能够返回子字符串首次出现的位置。 ## 文档 ### 目的 `index` 函数用于查找一个字符串中另一个字符串的起始位置。如果找到，返回子字符串的索引；...
Meta Keywords: index, perl, string, position, hello
-->

# Perl 中的 index 函数：查找子字符串的强大工具

## 摘要
`index` 是 Perl 中用于查找字符串中子字符串位置的内置函数，能够返回子字符串首次出现的位置。

## 文档
### 目的
`index` 函数用于查找一个字符串中另一个字符串的起始位置。如果找到，返回子字符串的索引；如果未找到，返回 -1。

### 使用方法
```perl
index STRING, SUBSTRING, [POSITION]
```
- `STRING`：要搜索的主字符串。
- `SUBSTRING`：要查找的子字符串。
- `POSITION`（可选）：从该位置开始搜索，默认为 0。

### 详细描述
- `index` 函数是区分大小写的。
- 如果主字符串或子字符串为空，返回值将是特定的：
  - 如果 `SUBSTRING` 为空，返回 `0`。
  - 如果 `STRING` 为空，返回 `-1`，除非 `SUBSTRING` 也为空。
- `POSITION` 参数允许用户指定从字符串的哪个位置开始查找，若该位置超出字符串长度，则返回 -1。

## 示例
### 示例 1：基本用法
```perl
my $string = "Hello, world!";
my $position = index($string, "world");
print $position;  # 输出 7
```

### 示例 2：指定起始位置
```perl
my $string = "Hello, world! Hello, Perl!";
my $position = index($string, "Hello", 10);
print $position;  # 输出 20
```

### 示例 3：未找到子字符串
```perl
my $string = "Hello, world!";
my $position = index($string, "Perl");
print $position;  # 输出 -1
```

## 解释
- **常见问题**：在使用 `index` 时，确保子字符串确实存在于主字符串中，否则会得到 -1。
- **大小写敏感**：`index` 函数是大小写敏感的，"hello" 和 "Hello" 会被视为不同的字符串。
- **性能考虑**：对于长字符串，频繁调用 `index` 可能会影响性能，因此在性能敏感的场合应谨慎使用。

## 一句话总结
`index` 函数在 Perl 中用于查找子字符串在主字符串中的首次出现位置，是字符串处理的基本工具之一。