# [Linux] C Shell (csh) parted 用法: 分区管理工具

## 概述
`parted` 是一个用于管理磁盘分区的命令行工具。它允许用户创建、删除、调整大小和检查磁盘分区，支持多种文件系统。

## 用法
基本语法如下：
```
parted [options] [arguments]
```

## 常用选项
- `-l`：列出所有可用的磁盘和分区。
- `-s`：静默模式，不显示提示信息。
- `mklabel`：创建新的分区表。
- `mkpart`：创建新的分区。
- `rm`：删除指定的分区。
- `resizepart`：调整指定分区的大小。

## 常见示例
1. 列出所有磁盘和分区：
   ```bash
   parted -l
   ```

2. 创建新的分区表：
   ```bash
   parted /dev/sda mklabel gpt
   ```

3. 创建新的分区：
   ```bash
   parted /dev/sda mkpart primary ext4 1MiB 100MiB
   ```

4. 删除指定的分区：
   ```bash
   parted /dev/sda rm 1
   ```

5. 调整分区大小：
   ```bash
   parted /dev/sda resizepart 1 200MiB
   ```

## 小贴士
- 在执行分区操作之前，请确保备份重要数据，以防数据丢失。
- 使用 `-s` 选项可以避免在脚本中出现交互提示。
- 在对分区进行任何更改之前，先使用 `print` 命令查看当前的分区布局。