# [操作系统] C Shell (csh) wget 使用方法: 下载文件的命令行工具

## 概述
`wget` 是一个用于从网络上下载文件的命令行工具。它支持 HTTP、HTTPS 和 FTP 协议，能够在不需要用户交互的情况下下载文件，非常适合批量下载和脚本自动化。

## 用法
基本语法如下：
```bash
wget [选项] [参数]
```

## 常用选项
- `-O <文件名>`: 指定下载文件的名称。
- `-q`: 安静模式，不显示下载进度。
- `-c`: 断点续传，继续未完成的下载。
- `--limit-rate=<速率>`: 限制下载速度。
- `-r`: 递归下载，下载整个网站或目录。

## 常见示例
1. 下载单个文件：
   ```bash
   wget http://example.com/file.zip
   ```

2. 指定下载文件名：
   ```bash
   wget -O myfile.zip http://example.com/file.zip
   ```

3. 断点续传：
   ```bash
   wget -c http://example.com/largefile.zip
   ```

4. 限制下载速度：
   ```bash
   wget --limit-rate=200k http://example.com/file.zip
   ```

5. 递归下载整个网站：
   ```bash
   wget -r http://example.com/
   ```

## 提示
- 使用 `-q` 选项可以在脚本中运行时减少输出信息。
- 在下载大文件时，使用 `-c` 选项可以避免重复下载已完成的部分。
- 结合 `--limit-rate` 选项，可以在网络带宽有限的情况下合理分配资源。