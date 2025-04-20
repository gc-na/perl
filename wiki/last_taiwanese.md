# [台灣] C Shell (csh) last 使用法: 顯示使用者登入紀錄

## Overview
`last` 命令用於顯示系統中使用者的登入紀錄。它會從 `/var/log/wtmp` 檔案中讀取資料，並列出最近的登入和登出事件，幫助管理員追蹤使用者活動。

## Usage
基本語法如下：
```
last [options] [arguments]
```

## Common Options
- `-n [number]`：顯示最近的登入紀錄數量。
- `-R`：不顯示主機名稱。
- `-x`：顯示系統關機和重啟的紀錄。

## Common Examples
- 顯示所有使用者的登入紀錄：
  ```csh
  last
  ```

- 顯示最近 5 筆登入紀錄：
  ```csh
  last -n 5
  ```

- 顯示不包含主機名稱的登入紀錄：
  ```csh
  last -R
  ```

- 顯示包括系統關機和重啟的紀錄：
  ```csh
  last -x
  ```

## Tips
- 使用 `last` 命令時，注意紀錄的時間範圍，特別是在高流量的系統中，可能會有大量的登入紀錄。
- 結合 `grep` 命令可以過濾特定使用者的登入紀錄，例如：
  ```csh
  last | grep username
  ```
- 定期檢查登入紀錄，有助於發現未經授權的訪問或異常活動。