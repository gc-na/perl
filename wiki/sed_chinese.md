# [操作系统] C Shell (csh) sed 用法等价: 文本流编辑器

## 概述
`sed` 是一个流编辑器，用于对文本进行基本的处理和转换。它可以对输入的文本进行查找、替换、删除和插入等操作，适用于处理文件或标准输入流中的数据。

## 用法
基本语法如下：
```bash
sed [options] [arguments]
```

## 常用选项
- `-e`：允许在命令行中指定多个编辑命令。
- `-f`：从文件中读取编辑命令。
- `-i`：直接修改文件，而不是输出到标准输出。
- `-n`：抑制自动输出，通常与 `p` 命令结合使用。

## 常见示例
1. **替换文本**
   ```bash
   sed 's/old_text/new_text/' filename
   ```
   这个命令将文件 `filename` 中的第一个 `old_text` 替换为 `new_text`。

2. **全局替换**
   ```bash
   sed 's/old_text/new_text/g' filename
   ```
   这个命令将文件 `filename` 中的所有 `old_text` 替换为 `new_text`。

3. **删除行**
   ```bash
   sed '3d' filename
   ```
   这个命令删除文件 `filename` 中的第三行。

4. **插入行**
   ```bash
   sed '2i\This is a new line' filename
   ```
   这个命令在文件 `filename` 的第二行之前插入一行文本 "This is a new line"。

5. **直接修改文件**
   ```bash
   sed -i 's/old_text/new_text/g' filename
   ```
   这个命令直接在文件 `filename` 中将所有 `old_text` 替换为 `new_text`。

## 小贴士
- 使用 `-n` 选项与 `p` 命令结合，可以仅输出匹配的行，避免输出整个文件。
- 在进行替换时，使用分隔符 `/` 可能会引起混淆，可以选择其他字符作为分隔符，例如 `#`。
- 在处理大文件时，使用 `-i` 选项时请小心，因为它会直接修改原文件，建议先备份文件。