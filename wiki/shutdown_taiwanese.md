# [台灣] C Shell (csh) shutdown 用法: 關閉系統

## Overview
`shutdown` 命令用於安全地關閉或重啟系統。這個命令可以讓系統管理員在指定的時間內關閉系統，並且可以發送警告訊息給所有登入的使用者。

## Usage
基本語法如下：
```
shutdown [options] [arguments]
```

## Common Options
- `-h`：關閉系統。
- `-r`：重啟系統。
- `-k`：發送警告訊息，但不實際關閉系統。
- `+m`：在 m 分鐘後關閉系統（例如 `+5` 表示 5 分鐘後關閉）。
- `hh:mm`：在指定的時間關閉系統（例如 `23:00` 表示晚上 11 點）。

## Common Examples
1. **立即關閉系統**：
   ```csh
   shutdown -h now
   ```

2. **在 5 分鐘後關閉系統**：
   ```csh
   shutdown -h +5
   ```

3. **在晚上 11 點關閉系統**：
   ```csh
   shutdown -h 23:00
   ```

4. **重啟系統**：
   ```csh
   shutdown -r now
   ```

5. **發送警告訊息但不關閉系統**：
   ```csh
   shutdown -k now
   ```

## Tips
- 使用 `shutdown` 命令前，最好通知所有使用者，以避免資料遺失。
- 可以使用 `wall` 命令發送關閉通知給所有登入的使用者。
- 確保在關閉系統前，所有重要的工作都已儲存。