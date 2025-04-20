# [操作系统] C Shell (csh) rmdir 用法: 删除空目录

## 概述
`rmdir` 命令用于删除空目录。如果目录中仍有文件或子目录，`rmdir` 将无法删除该目录。

## 用法
基本语法如下：
```
rmdir [选项] [参数]
```

## 常用选项
- `-p`：递归删除目录，删除指定目录及其所有空父目录。

## 常见示例
1. 删除一个空目录：
   ```csh
   rmdir my_empty_directory
   ```

2. 递归删除空目录及其父目录：
   ```csh
   rmdir -p my_empty_directory/parent_directory
   ```

3. 尝试删除非空目录（将会失败）：
   ```csh
   rmdir non_empty_directory
   ```

## 提示
- 确保目录为空后再使用 `rmdir`，否则命令将失败。
- 使用 `-p` 选项时，请小心，因为它会删除所有空的父目录。
- 可以使用 `ls` 命令检查目录内容，确保在删除前目录是空的。