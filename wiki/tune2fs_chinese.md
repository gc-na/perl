# [Linux] C Shell (csh) tune2fs 用法: 调整 ext2/ext3/ext4 文件系统参数

## 概述
`tune2fs` 命令用于调整 ext2、ext3 和 ext4 文件系统的参数。它允许用户修改文件系统的特性，以优化性能或满足特定需求。

## 用法
基本语法如下：
```shell
tune2fs [选项] [参数]
```

## 常用选项
- `-c <max_mount_count>`: 设置最大挂载次数。
- `-i <interval>`: 设置检查间隔时间。
- `-O <feature>`: 启用或禁用文件系统特性。
- `-L <label>`: 设置文件系统标签。
- `-e <error_behavior>`: 设置错误处理策略。

## 常见示例
1. 设置最大挂载次数为 20 次：
   ```shell
   tune2fs -c 20 /dev/sda1
   ```

2. 设置检查间隔为 30 天：
   ```shell
   tune2fs -i 30d /dev/sda1
   ```

3. 启用文件系统特性，例如大文件支持：
   ```shell
   tune2fs -O large_file /dev/sda1
   ```

4. 设置文件系统标签为 "MyDisk"：
   ```shell
   tune2fs -L MyDisk /dev/sda1
   ```

5. 设置错误处理策略为重启：
   ```shell
   tune2fs -e remount-ro /dev/sda1
   ```

## 提示
- 在使用 `tune2fs` 之前，确保文件系统已卸载，以避免数据损坏。
- 定期检查文件系统状态，以确保其健康和性能。
- 使用 `tune2fs -l /dev/sda1` 命令查看当前文件系统的参数设置。