# [操作系统] C Shell (csh) rsync 用法： 文件同步和备份工具

## 概述
`rsync` 是一个用于文件和目录同步的命令行工具。它可以在本地和远程系统之间高效地复制和同步文件，支持增量备份和多种传输选项。

## 用法
基本语法如下：
```bash
rsync [options] [arguments]
```

## 常用选项
- `-a`：归档模式，表示递归复制文件并保持文件属性。
- `-v`：详细输出，显示传输过程中的详细信息。
- `-z`：在传输过程中压缩文件，以减少带宽使用。
- `-r`：递归复制整个目录。
- `--delete`：删除目标中源文件没有的文件，以保持同步。

## 常见示例
1. **本地文件同步**
   ```bash
   rsync -av /path/to/source/ /path/to/destination/
   ```

2. **远程文件同步**
   ```bash
   rsync -avz /path/to/local/ user@remote_host:/path/to/remote/
   ```

3. **使用压缩进行远程同步**
   ```bash
   rsync -avz --progress /path/to/local/ user@remote_host:/path/to/remote/
   ```

4. **删除目标中多余的文件**
   ```bash
   rsync -av --delete /path/to/source/ /path/to/destination/
   ```

## 提示
- 在进行大规模同步之前，可以使用 `--dry-run` 选项来预览将要执行的操作。
- 确保在使用远程同步时，SSH 连接正常，以避免传输中断。
- 定期备份重要文件，使用 `rsync` 可以有效减少备份时间和存储空间。