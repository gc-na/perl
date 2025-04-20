# [Linux] C Shell (csh) journalctl 用法: 查看系统日志

## 概述
`journalctl` 是一个用于查看和管理系统日志的命令。它可以访问由 `systemd` 日志系统收集的日志信息，帮助用户监控和排查系统问题。

## 用法
基本语法如下：
```bash
journalctl [options] [arguments]
```

## 常用选项
- `-b`：显示当前启动以来的日志。
- `-f`：实时跟踪日志输出。
- `-u <unit>`：显示特定服务单元的日志。
- `--since <time>`：从指定时间开始显示日志。
- `--until <time>`：直到指定时间显示日志。

## 常见示例
- 查看当前启动以来的所有日志：
  ```bash
  journalctl -b
  ```

- 实时跟踪日志输出：
  ```bash
  journalctl -f
  ```

- 查看特定服务的日志，例如 `ssh.service`：
  ```bash
  journalctl -u ssh.service
  ```

- 查看从特定时间开始的日志，例如从昨天开始：
  ```bash
  journalctl --since "yesterday"
  ```

- 查看直到特定时间的日志，例如直到今天中午：
  ```bash
  journalctl --until "12:00"
  ```

## 提示
- 使用 `-p <priority>` 选项可以过滤日志级别，例如只查看错误日志：
  ```bash
  journalctl -p err
  ```
- 可以结合多个选项使用，例如同时查看特定服务的实时日志：
  ```bash
  journalctl -u ssh.service -f
  ```
- 定期检查日志可以帮助及时发现系统问题，建议将其纳入日常维护工作中。