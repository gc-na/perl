# [中文] C Shell (csh) comm 命令: 比较文件内容

## 概述
`comm` 命令用于比较两个已排序的文件，并输出它们的不同之处和相同之处。它将文件的内容分为三列：仅在第一个文件中出现的行、仅在第二个文件中出现的行，以及在两个文件中都出现的行。

## 用法
基本语法如下：
```csh
comm [选项] [参数]
```

## 常用选项
- `-1`：抑制仅在第一个文件中出现的行。
- `-2`：抑制仅在第二个文件中出现的行。
- `-3`：抑制在两个文件中都出现的行。
- `-i`：忽略大小写进行比较。

## 常见示例
以下是一些实用的 `comm` 命令示例：

1. 比较两个文件并显示所有行：
   ```csh
   comm file1.txt file2.txt
   ```

2. 仅显示在 `file1.txt` 中出现的行：
   ```csh
   comm -13 file1.txt file2.txt
   ```

3. 仅显示在 `file2.txt` 中出现的行：
   ```csh
   comm -23 file1.txt file2.txt
   ```

4. 忽略大小写进行比较：
   ```csh
   comm -i file1.txt file2.txt
   ```

## 小贴士
- 确保比较的文件是已排序的，否则 `comm` 的输出可能不正确。
- 使用 `sort` 命令对文件进行排序，例如：
  ```csh
  sort file1.txt > sorted_file1.txt
  sort file2.txt > sorted_file2.txt
  comm sorted_file1.txt sorted_file2.txt
  ```
- 可以将 `comm` 命令的输出重定向到文件中，以便后续查看：
  ```csh
  comm file1.txt file2.txt > comparison_result.txt
  ```