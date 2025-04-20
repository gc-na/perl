# [台灣] C Shell (csh) ps 使用法: 顯示當前進程資訊

## Overview
`ps` 命令用於顯示當前系統中的進程狀態。它可以讓使用者查看正在運行的程序及其相關資訊，如進程ID、使用的CPU和記憶體等。

## Usage
基本語法如下：
```
ps [options] [arguments]
```

## Common Options
- `-e`：顯示所有進程。
- `-f`：以完整格式顯示進程資訊。
- `-u`：顯示指定用戶的進程。
- `-l`：以長格式顯示進程資訊。
- `-p`：顯示指定進程ID的進程。

## Common Examples
1. 顯示所有進程：
   ```csh
   ps -e
   ```

2. 以完整格式顯示進程資訊：
   ```csh
   ps -ef
   ```

3. 顯示特定用戶的進程：
   ```csh
   ps -u username
   ```

4. 顯示指定進程ID的進程：
   ```csh
   ps -p 1234
   ```

5. 以長格式顯示進程資訊：
   ```csh
   ps -l
   ```

## Tips
- 使用 `ps -ef | grep process_name` 可以快速找到特定進程。
- 結合 `sort` 命令，可以根據CPU或記憶體使用量排序進程。
- 定期檢查進程狀態有助於系統維護和性能優化。