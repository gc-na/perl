# [台灣] C Shell (csh) iostat 使用法: 監控系統 I/O 性能

## Overview
`iostat` 命令用於監控系統的輸入/輸出（I/O）性能，提供有關 CPU 使用率和各個存儲設備的 I/O 活動的統計資訊。這對於診斷性能瓶頸和優化系統資源的使用非常有幫助。

## Usage
基本語法如下：
```
iostat [options] [arguments]
```

## Common Options
- `-c`：顯示 CPU 使用率的統計資訊。
- `-d`：顯示每個設備的 I/O 活動。
- `-x`：顯示擴展的設備統計資訊，包括 I/O 等待時間等。
- `-h`：以人類可讀的格式顯示輸出。

## Common Examples
1. 顯示 CPU 使用率和設備 I/O 活動：
   ```csh
   iostat
   ```

2. 僅顯示 CPU 使用率：
   ```csh
   iostat -c
   ```

3. 顯示每個設備的 I/O 活動：
   ```csh
   iostat -d
   ```

4. 顯示擴展的設備統計資訊：
   ```csh
   iostat -x
   ```

5. 每 2 秒更新一次顯示：
   ```csh
   iostat 2
   ```

## Tips
- 定期使用 `iostat` 可以幫助你及時發現系統性能問題。
- 結合 `-x` 和 `-d` 選項可以獲得更全面的 I/O 性能視圖。
- 將 `iostat` 的輸出重定向到文件中，可以方便後續分析：
   ```csh
   iostat -d > iostat_output.txt
   ```