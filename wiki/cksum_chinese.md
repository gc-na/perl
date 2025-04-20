# [Linux] C Shell (csh) cksum 用法: 计算文件的校验和

## 概述
`cksum` 命令用于计算文件的校验和和字节数。它可以帮助用户验证文件的完整性，确保文件在传输或存储过程中没有被损坏。

## 用法
基本语法如下：
```
cksum [options] [arguments]
```

## 常用选项
- `-a`：指定校验和算法（如 MD5、SHA256 等）。
- `-h`：显示帮助信息。
- `-o`：输出格式选项。

## 常见示例
1. 计算单个文件的校验和：
   ```csh
   cksum filename.txt
   ```

2. 计算多个文件的校验和：
   ```csh
   cksum file1.txt file2.txt file3.txt
   ```

3. 将输出重定向到文件：
   ```csh
   cksum filename.txt > checksum.txt
   ```

4. 使用选项指定算法（假设支持）：
   ```csh
   cksum -a md5 filename.txt
   ```

## 提示
- 在传输文件后，使用 `cksum` 验证文件的完整性是一个好习惯。
- 对于大型文件，考虑将输出重定向到文件，以便后续查看。
- 定期检查备份文件的校验和，以确保数据的安全性。