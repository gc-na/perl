# [台灣] C Shell (csh) mpstat 使用方法：顯示 CPU 使用情況

## Overview
mpstat 命令用於顯示各個 CPU 的使用情況，幫助用戶監控系統性能。它可以提供有關 CPU 使用率的詳細資訊，讓用戶了解系統的負載情況。

## Usage
基本語法如下：
```
mpstat [options] [arguments]
```

## Common Options
- `-P ALL`：顯示所有 CPU 的統計資訊。
- `-u`：顯示 CPU 使用率的統計資訊。
- `-h`：顯示幫助資訊，列出所有可用選項。

## Common Examples
- 顯示所有 CPU 的使用情況：
  ```bash
  mpstat -P ALL
  ```

- 顯示 CPU 使用率：
  ```bash
  mpstat -u
  ```

- 每 5 秒顯示一次所有 CPU 的使用情況：
  ```bash
  mpstat -P ALL 5
  ```

## Tips
- 使用 `-P ALL` 選項可以獲得每個 CPU 的詳細資訊，這對於多核心系統特別有用。
- 定期監控 CPU 使用情況可以幫助及早發現性能瓶頸。
- 結合其他性能監控工具（如 `top` 或 `vmstat`）使用，可以獲得更全面的系統性能分析。