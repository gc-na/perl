# [Linux] C Shell (csh) sha256sum 用法: 计算文件的SHA-256哈希值

## 概述
`sha256sum` 命令用于计算和验证文件的SHA-256哈希值。它常用于确保文件的完整性和安全性，特别是在下载文件后进行校验。

## 用法
基本语法如下：
```csh
sha256sum [options] [arguments]
```

## 常用选项
- `-b`：以二进制模式读取文件。
- `-c`：检查文件的SHA-256哈希值是否与给定的校验和匹配。
- `-o`：将输出写入指定文件。
- `--quiet`：在检查时不输出任何信息。

## 常见示例
1. 计算单个文件的SHA-256哈希值：
   ```csh
   sha256sum filename.txt
   ```

2. 计算多个文件的SHA-256哈希值：
   ```csh
   sha256sum file1.txt file2.txt
   ```

3. 将哈希值输出到文件：
   ```csh
   sha256sum filename.txt > checksum.sha256
   ```

4. 检查文件的SHA-256哈希值：
   ```csh
   sha256sum -c checksum.sha256
   ```

5. 以二进制模式读取文件并计算哈希值：
   ```csh
   sha256sum -b binaryfile.bin
   ```

## 小贴士
- 在下载文件后，使用 `sha256sum` 来验证文件的完整性，确保文件未被篡改。
- 将哈希值和文件一起存储，方便日后进行校验。
- 使用 `-o` 选项将输出重定向到文件，以便更好地管理和记录哈希值。