# [操作系统] C Shell (csh) scp 用法: 远程文件复制

## 概述
`scp`（安全复制）命令用于在本地和远程计算机之间安全地复制文件。它使用SSH协议进行数据传输，确保数据在传输过程中的安全性。

## 用法
基本语法如下：
```bash
scp [options] [arguments]
```

## 常用选项
- `-r`：递归复制整个目录。
- `-P port`：指定远程主机的端口号（注意是大写的P）。
- `-i identity_file`：指定用于身份验证的私钥文件。
- `-v`：详细模式，显示调试信息。

## 常见示例
1. 从本地复制文件到远程主机：
   ```bash
   scp localfile.txt user@remotehost:/path/to/destination/
   ```

2. 从远程主机复制文件到本地：
   ```bash
   scp user@remotehost:/path/to/remotefile.txt /local/destination/
   ```

3. 递归复制整个目录到远程主机：
   ```bash
   scp -r localdir user@remotehost:/path/to/destination/
   ```

4. 指定端口号进行复制：
   ```bash
   scp -P 2222 localfile.txt user@remotehost:/path/to/destination/
   ```

## 小贴士
- 在使用`scp`时，确保你有远程主机的访问权限。
- 使用`-v`选项可以帮助你调试连接问题。
- 对于大文件传输，可以考虑使用`rsync`，它在网络不稳定时表现更好。