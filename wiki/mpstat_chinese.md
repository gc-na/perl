# [操作系统] C Shell (csh) mpstat 用法: 显示CPU统计信息

## 概述
`mpstat` 命令用于显示各个CPU的使用情况和性能统计信息。它可以帮助用户监控系统的CPU负载，识别性能瓶颈。

## 用法
基本语法如下：
```
mpstat [options] [arguments]
```

## 常用选项
- `-P ALL`：显示所有CPU的统计信息。
- `-u`：显示CPU的使用情况，包括用户、系统和空闲时间的百分比。
- `-w`：显示等待I/O的时间。
- `-h`：以人类可读的格式显示输出。

## 常见示例
1. 显示所有CPU的使用情况：
   ```bash
   mpstat -P ALL
   ```

2. 每隔2秒显示一次CPU使用情况：
   ```bash
   mpstat 2
   ```

3. 显示CPU使用情况，包括I/O等待时间：
   ```bash
   mpstat -u -w
   ```

4. 显示特定CPU（如CPU 0）的统计信息：
   ```bash
   mpstat -P 0
   ```

## 提示
- 定期监控CPU使用情况可以帮助及时发现性能问题。
- 可以将 `mpstat` 的输出重定向到文件，以便后续分析：
  ```bash
  mpstat -P ALL 2 > cpu_stats.txt
  ```
- 结合其他监控工具（如 `top` 或 `vmstat`）使用，可以获得更全面的系统性能视图。