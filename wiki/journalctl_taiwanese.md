# [台灣] C Shell (csh) journalctl 用法: 查看系統日誌

## Overview
`journalctl` 是一個用於查看系統日誌的命令，特別是由 systemd 管理的日誌。它可以幫助用戶檢查系統的運行狀態、錯誤和其他重要事件。

## Usage
基本語法如下：
```csh
journalctl [options] [arguments]
```

## Common Options
- `-b`：顯示當前啟動的日誌。
- `-f`：實時跟蹤日誌輸出。
- `--since`：顯示從指定時間以來的日誌。
- `--until`：顯示直到指定時間的日誌。
- `-u`：顯示特定單元（如服務）的日誌。

## Common Examples
- 查看當前啟動的日誌：
```csh
journalctl -b
```
- 實時跟蹤日誌：
```csh
journalctl -f
```
- 查看從特定日期以來的日誌：
```csh
journalctl --since "2023-10-01"
```
- 查看特定服務的日誌：
```csh
journalctl -u ssh.service
```

## Tips
- 使用 `-f` 選項可以方便地監控系統日誌，特別是在排查問題時。
- 結合 `--since` 和 `--until` 可以精確篩選日誌，方便查找特定時間範圍內的事件。
- 定期檢查日誌可以幫助及早發現潛在的系統問題。