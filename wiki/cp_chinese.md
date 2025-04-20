# [Linux] C Shell (csh) cp 用法: 复制文件和目录

## 概述
`cp` 命令用于在 Unix 和类 Unix 系统中复制文件和目录。它可以将一个或多个源文件复制到目标位置。

## 用法
基本语法如下：
```csh
cp [options] [arguments]
```

## 常用选项
- `-i`：在覆盖文件之前提示确认。
- `-r`：递归复制目录及其内容。
- `-u`：仅在源文件比目标文件新时复制。
- `-v`：在复制过程中显示详细信息。

## 常见示例
1. 复制单个文件：
   ```csh
   cp file1.txt file2.txt
   ```
   这将把 `file1.txt` 复制为 `file2.txt`。

2. 复制多个文件到目标目录：
   ```csh
   cp file1.txt file2.txt /path/to/directory/
   ```
   这将把 `file1.txt` 和 `file2.txt` 复制到指定的目录。

3. 递归复制目录：
   ```csh
   cp -r /path/to/source_directory /path/to/destination_directory
   ```
   这将复制整个目录及其内容。

4. 使用提示确认覆盖：
   ```csh
   cp -i file1.txt file2.txt
   ```
   如果 `file2.txt` 已存在，系统会提示确认是否覆盖。

## 提示
- 在复制重要文件时，使用 `-i` 选项可以避免意外覆盖。
- 使用 `-v` 选项可以帮助你跟踪复制过程，特别是在处理多个文件时。
- 定期备份重要文件，使用 `cp` 命令可以快速完成此操作。