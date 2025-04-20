# [台灣] C Shell (csh) mount 使用法: 挂載檔案系統

## Overview
`mount` 命令用來將檔案系統掛載到指定的目錄，這樣用戶就可以訪問和操作該檔案系統中的檔案。

## Usage
基本語法如下：
```
mount [options] [arguments]
```

## Common Options
- `-t type`：指定檔案系統的類型，例如 ext4 或 nfs。
- `-o options`：提供額外的掛載選項，如讀取/寫入權限。
- `-r`：以只讀模式掛載檔案系統。
- `-w`：以讀寫模式掛載檔案系統。

## Common Examples
1. 掛載一個 ext4 檔案系統：
   ```csh
   mount -t ext4 /dev/sda1 /mnt/mydisk
   ```

2. 以只讀模式掛載 NFS 檔案系統：
   ```csh
   mount -t nfs -o ro server:/exported/path /mnt/nfs
   ```

3. 掛載一個 ISO 映像檔：
   ```csh
   mount -o loop /path/to/image.iso /mnt/iso
   ```

4. 掛載一個 USB 隨身碟：
   ```csh
   mount /dev/sdb1 /mnt/usb
   ```

## Tips
- 確保在掛載之前，目錄已經存在。
- 使用 `umount` 命令來卸載已掛載的檔案系統。
- 檢查掛載的檔案系統狀態，可以使用 `df -h` 命令查看當前的掛載情況。