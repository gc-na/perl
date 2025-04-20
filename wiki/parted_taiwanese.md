# [台灣] C Shell (csh) parted 使用法: 磁碟分割管理工具

## Overview
`parted` 是一個用於管理磁碟分割的命令行工具。它可以用來創建、刪除、調整大小和檢查磁碟分割，並支援多種檔案系統格式。

## Usage
基本語法如下：
```
parted [options] [arguments]
```

## Common Options
- `-l`：列出所有可用的磁碟和其分割資訊。
- `-s`：靜默模式，不顯示提示訊息。
- `mkpart`：創建一個新的分割。
- `rm`：刪除指定的分割。
- `resizepart`：調整指定分割的大小。

## Common Examples
以下是一些常見的使用範例：

1. 列出所有磁碟：
   ```bash
   parted -l
   ```

2. 創建一個新的分割：
   ```bash
   parted /dev/sda mkpart primary ext4 1MiB 100MiB
   ```

3. 刪除一個分割：
   ```bash
   parted /dev/sda rm 1
   ```

4. 調整分割大小：
   ```bash
   parted /dev/sda resizepart 1 200MiB
   ```

## Tips
- 在執行 `parted` 命令之前，請確保備份重要資料，以防止資料遺失。
- 使用 `-s` 選項可以使腳本執行時更為安靜，適合自動化任務。
- 在調整分割大小時，務必確認新的大小不會影響到其他分割的資料。