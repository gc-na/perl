# [Linux] C Shell (csh) tail 用法: 显示文件的最后几行

## 概述
`tail` 命令用于显示文件的最后几行内容。它通常用于查看日志文件的最新条目或监控文件的实时更新。

## 用法
基本语法如下：
```
tail [options] [arguments]
```

## 常用选项
- `-n [number]`：显示文件的最后指定行数。例如，`-n 10` 显示最后 10 行。
- `-f`：实时跟踪文件的变化，适合监控日志文件。
- `-c [number]`：显示文件的最后指定字节数。

## 常见示例
- 显示文件的最后 10 行：
  ```csh
  tail -n 10 filename.txt
  ```

- 实时跟踪日志文件的更新：
  ```csh
  tail -f /var/log/syslog
  ```

- 显示文件的最后 100 字节：
  ```csh
  tail -c 100 filename.txt
  ```

## 小贴士
- 使用 `tail -f` 时，可以按 `Ctrl + C` 停止跟踪。
- 结合 `grep` 使用，可以过滤出特定内容，例如：
  ```csh
  tail -f /var/log/syslog | grep "error"
  ```
- 如果需要查看多个文件的最后几行，可以在命令中列出多个文件名。