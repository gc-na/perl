# [操作系统] C Shell (csh) sftp 用法: 安全文件传输

## 概述
sftp（安全文件传输协议）是一个用于在网络上安全地传输文件的命令行工具。它基于SSH协议，提供了加密的文件传输功能，确保数据在传输过程中的安全性。

## 用法
sftp命令的基本语法如下：

```bash
sftp [options] [user@]host
```

## 常用选项
- `-P port`：指定连接的端口号，默认为22。
- `-o option`：设置特定的SSH选项。
- `-b batchfile`：从批处理文件中读取命令。

## 常见示例
1. 连接到远程主机：
   ```bash
   sftp user@hostname
   ```

2. 上传文件到远程主机：
   ```bash
   sftp user@hostname
   put localfile.txt
   ```

3. 从远程主机下载文件：
   ```bash
   sftp user@hostname
   get remotefile.txt
   ```

4. 列出远程目录中的文件：
   ```bash
   sftp user@hostname
   ls
   ```

5. 删除远程主机上的文件：
   ```bash
   sftp user@hostname
   rm remotefile.txt
   ```

## 小贴士
- 在使用sftp时，确保SSH服务在远程主机上运行。
- 使用`-P`选项可以连接到非默认端口的主机。
- 定期检查和更新SSH密钥，以增强安全性。