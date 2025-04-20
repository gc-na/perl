# [台灣] C Shell (csh) nice 使用法: 調整進程優先權

## Overview
`nice` 命令用於調整進程的優先權，讓用戶能夠控制進程在系統中的運行優先級。透過改變優先權，使用者可以讓某些進程獲得更多的 CPU 資源，或是降低其他進程的優先權。

## Usage
基本語法如下：
```
nice [options] [arguments]
```

## Common Options
- `-n`：指定優先權的數值，範圍從 -20（最高優先權）到 19（最低優先權）。
- `-h`：顯示幫助信息。

## Common Examples
1. 以默認優先權啟動一個進程：
   ```csh
   nice ./my_program
   ```

2. 以較低的優先權啟動一個進程：
   ```csh
   nice -n 10 ./my_program
   ```

3. 以較高的優先權啟動一個進程：
   ```csh
   nice -n -5 ./my_program
   ```

4. 查看當前進程的優先權：
   ```csh
   ps -o pid,ni,comm
   ```

## Tips
- 使用 `nice` 命令時，記得選擇合適的優先權，以免影響系統的整體性能。
- 在多用戶環境中，合理調整進程優先權可以提高系統的使用效率。
- 若需要更改已運行進程的優先權，可以使用 `renice` 命令。