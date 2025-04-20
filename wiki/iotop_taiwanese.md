# [台灣] C Shell (csh) iotop 使用法: 監控磁碟 I/O 活動

## Overview
iotop 是一個用於監控系統中磁碟 I/O 活動的命令行工具。它可以顯示哪些進程正在使用磁碟，並提供即時的 I/O 數據，幫助用戶識別性能瓶頸。

## Usage
基本語法如下：
```
iotop [options] [arguments]
```

## Common Options
- `-o`：只顯示正在進行 I/O 操作的進程。
- `-b`：以批次模式運行，適合於腳本使用。
- `-n NUM`：指定批次模式下的更新次數。
- `-d SEC`：設定更新的時間間隔（以秒為單位）。

## Common Examples
- 監控所有進程的 I/O 活動：
  ```bash
  iotop
  ```

- 只顯示正在進行 I/O 操作的進程：
  ```bash
  iotop -o
  ```

- 以批次模式運行，更新 5 次，每次間隔 2 秒：
  ```bash
  iotop -b -n 5 -d 2
  ```

## Tips
- 在使用 iotop 時，建議以 root 權限運行，以便獲得完整的進程資訊。
- 使用 `-o` 選項可以幫助你快速找出哪些進程正在消耗磁碟 I/O，這對於性能調優特別有用。
- 定期監控 I/O 活動可以幫助你及早發現潛在的系統問題。