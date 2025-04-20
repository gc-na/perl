# [台灣] C Shell (csh) pidstat 使用說明: 監控進程統計資訊

## Overview
`pidstat` 是一個用於顯示進程統計資訊的命令。它可以顯示每個進程的 CPU 使用率、記憶體使用情況等，幫助用戶監控系統性能。

## Usage
基本語法如下：
```shell
pidstat [options] [arguments]
```

## Common Options
- `-h`：顯示幫助訊息。
- `-r`：顯示記憶體使用情況。
- `-u`：顯示 CPU 使用率。
- `-p <pid>`：指定要監控的進程 ID。
- `-t`：顯示所有進程的統計資訊。

## Common Examples
以下是一些常見的使用範例：

1. 監控所有進程的 CPU 使用率：
   ```shell
   pidstat -u
   ```

2. 監控特定進程的記憶體使用情況：
   ```shell
   pidstat -r -p 1234
   ```

3. 每隔 2 秒顯示一次所有進程的統計資訊：
   ```shell
   pidstat 2
   ```

4. 監控所有進程的 CPU 和記憶體使用情況：
   ```shell
   pidstat -u -r
   ```

## Tips
- 使用 `-h` 選項可以快速查看所有可用選項，幫助你更有效地使用 `pidstat`。
- 定期監控進程的性能可以幫助及早發現潛在的系統問題。
- 結合其他命令（如 `grep`）使用，可以更精確地篩選出需要的進程資訊。