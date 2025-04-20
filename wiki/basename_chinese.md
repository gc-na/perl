# [Linux] C Shell (csh) basename 用法等价: 提取文件名

## 概述
`basename` 命令用于从给定的路径中提取文件名部分。它可以去掉路径中的目录部分，只保留文件名及其扩展名。

## 用法
基本语法如下：
```csh
basename [options] [arguments]
```

## 常用选项
- `-a`：处理多个路径，返回每个路径的文件名。
- `-s`：去掉指定的后缀。

## 常见示例
以下是一些常见的 `basename` 使用示例：

1. 提取文件名：
   ```csh
   basename /usr/local/bin/script.sh
   ```
   输出：
   ```
   script.sh
   ```

2. 提取文件名并去掉扩展名：
   ```csh
   basename /usr/local/bin/script.sh .sh
   ```
   输出：
   ```
   script
   ```

3. 处理多个路径：
   ```csh
   basename -a /usr/local/bin/script.sh /usr/bin/another_script.py
   ```
   输出：
   ```
   script.sh
   another_script.py
   ```

4. 去掉自定义后缀：
   ```csh
   basename /path/to/file.txt .txt
   ```
   输出：
   ```
   file
   ```

## 小贴士
- 使用 `basename` 时，确保提供正确的路径，以避免意外的输出。
- 可以结合其他命令使用，例如与 `find` 命令结合，提取查找到的文件名。
- 对于处理多个文件名，使用 `-a` 选项可以简化操作。