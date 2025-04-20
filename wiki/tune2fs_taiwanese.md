# [台灣] C Shell (csh) tune2fs 使用法: 調整 ext2/ext3/ext4 檔案系統的參數

## Overview
`tune2fs` 是一個用於調整 ext2、ext3 和 ext4 檔案系統參數的命令。使用此命令，您可以修改檔案系統的各種屬性，例如檔案系統的檢查間隔、日誌選項等。

## Usage
基本的語法如下：
```bash
tune2fs [選項] [參數]
```

## Common Options
- `-c <次數>`: 設定檔案系統在檢查之前的最大掛載次數。
- `-i <時間>`: 設定檔案系統的檢查間隔時間。
- `-m <百分比>`: 設定保留給超級用戶的空間百分比。
- `-O <選項>`: 啟用或禁用特定的檔案系統功能。
- `-L <標籤>`: 設定檔案系統的標籤。

## Common Examples
以下是一些常見的使用範例：

1. 設定檔案系統在檢查之前的最大掛載次數為 20：
   ```bash
   tune2fs -c 20 /dev/sda1
   ```

2. 設定檔案系統的檢查間隔為 30 天：
   ```bash
   tune2fs -i 30d /dev/sda1
   ```

3. 設定保留給超級用戶的空間百分比為 5%：
   ```bash
   tune2fs -m 5 /dev/sda1
   ```

4. 啟用檔案系統的日誌功能：
   ```bash
   tune2fs -O journal_data /dev/sda1
   ```

5. 設定檔案系統的標籤為 "MyDisk"：
   ```bash
   tune2fs -L MyDisk /dev/sda1
   ```

## Tips
- 在執行 `tune2fs` 前，建議先備份重要資料，以防不測。
- 確保在未掛載的狀態下對檔案系統進行調整，以避免資料損壞。
- 使用 `tune2fs -l /dev/sda1` 可以查看檔案系統的當前參數設定。