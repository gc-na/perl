# [台灣] C Shell (csh) e2fsck 用法: 檢查和修復檔案系統

## Overview
e2fsck 是一個用於檢查和修復 Linux 檔案系統的命令，特別是 ext2、ext3 和 ext4 檔案系統。它能夠檢查檔案系統的一致性，並在發現錯誤時進行修復。

## Usage
基本語法如下：
```
e2fsck [options] [arguments]
```

## Common Options
- `-p`：自動修復檔案系統錯誤，無需用戶確認。
- `-f`：強制檢查，即使檔案系統看起來是乾淨的。
- `-y`：對所有問題自動回答「是」，進行修復。
- `-n`：不進行任何修復，只顯示錯誤。
- `-c`：檢查檔案系統的區塊是否損壞。

## Common Examples
1. **自動修復檔案系統錯誤**
   ```bash
   e2fsck -p /dev/sda1
   ```

2. **強制檢查檔案系統**
   ```bash
   e2fsck -f /dev/sda1
   ```

3. **自動修復所有問題**
   ```bash
   e2fsck -y /dev/sda1
   ```

4. **僅顯示錯誤，不進行修復**
   ```bash
   e2fsck -n /dev/sda1
   ```

5. **檢查區塊損壞**
   ```bash
   e2fsck -c /dev/sda1
   ```

## Tips
- 在執行 e2fsck 前，建議先卸載檔案系統，以避免資料損壞。
- 定期檢查檔案系統可以幫助預防未來的問題。
- 在進行重大修復前，務必備份重要資料。