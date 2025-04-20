# [台灣] C Shell (csh) umount 使用方式: 卸載檔案系統

## Overview
`umount` 命令用於卸載已掛載的檔案系統。這是管理檔案系統的重要步驟，可以確保資料的完整性並釋放系統資源。

## Usage
基本語法如下：
```
umount [選項] [參數]
```

## Common Options
- `-a`：卸載所有檔案系統。
- `-f`：強制卸載，即使檔案系統忙碌。
- `-l`：延遲卸載，立即返回，但在後台完成卸載。
- `-r`：如果卸載失敗，則以只讀模式重新掛載。

## Common Examples
1. 卸載指定的檔案系統：
   ```csh
   umount /mnt/mydisk
   ```

2. 強制卸載檔案系統：
   ```csh
   umount -f /mnt/mydisk
   ```

3. 卸載所有檔案系統：
   ```csh
   umount -a
   ```

4. 延遲卸載檔案系統：
   ```csh
   umount -l /mnt/mydisk
   ```

5. 以只讀模式重新掛載檔案系統：
   ```csh
   umount -r /mnt/mydisk
   ```

## Tips
- 在卸載之前，確保沒有進程正在使用該檔案系統，以避免資料損壞。
- 使用 `df` 命令檢查當前掛載的檔案系統，確認要卸載的檔案系統名稱。
- 強制卸載時要小心，因為這可能會導致資料損失。