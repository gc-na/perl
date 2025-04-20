# [台灣] C Shell (csh) timedatectl 使用方法: 設定和查詢系統時間與日期

## Overview
`timedatectl` 是一個用於查詢和設定系統時間與日期的命令。它可以顯示當前的時間、日期、時區以及系統的時間同步狀態。

## Usage
基本語法如下：
```csh
timedatectl [options] [arguments]
```

## Common Options
- `status`：顯示當前的時間和日期狀態。
- `set-time`：設定系統的時間。
- `set-timezone`：設定系統的時區。
- `set-ntp`：啟用或禁用 NTP（網路時間協定）同步。
- `list-timezones`：列出所有可用的時區。

## Common Examples
- 查看當前時間和日期狀態：
  ```csh
  timedatectl status
  ```

- 設定系統時間為 2023 年 10 月 1 日 12:00:
  ```csh
  timedatectl set-time '2023-10-01 12:00:00'
  ```

- 設定系統時區為台北：
  ```csh
  timedatectl set-timezone Asia/Taipei
  ```

- 啟用 NTP 同步：
  ```csh
  timedatectl set-ntp true
  ```

- 列出所有可用的時區：
  ```csh
  timedatectl list-timezones
  ```

## Tips
- 在設定時間和日期時，確保使用正確的格式，以避免錯誤。
- 定期檢查 NTP 同步狀態，以確保系統時間的準確性。
- 使用 `list-timezones` 命令可以幫助你找到正確的時區名稱。