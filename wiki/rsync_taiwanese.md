# [台灣] C Shell (csh) rsync 使用法: 用於檔案同步與備份

## Overview
`rsync` 是一個強大的工具，用於在本地和遠端系統之間同步檔案和目錄。它的主要特點是高效的增量備份，只傳輸變更的部分，從而節省帶寬和時間。

## Usage
基本語法如下：
```csh
rsync [options] [arguments]
```

## Common Options
- `-a`：以歸檔模式運行，這意味著會保留檔案的權限、時間戳等屬性。
- `-v`：顯示詳細的輸出，讓使用者可以看到正在進行的操作。
- `-z`：在傳輸過程中啟用壓縮，適合於網路帶寬有限的情況。
- `-r`：遞迴地同步目錄。
- `--delete`：在目標位置刪除源位置不存在的檔案，保持兩者一致。

## Common Examples
以下是一些常見的 `rsync` 使用範例：

1. 將本地目錄同步到遠端伺服器：
   ```csh
   rsync -avz /local/directory/ user@remote:/remote/directory/
   ```

2. 從遠端伺服器下載檔案到本地：
   ```csh
   rsync -avz user@remote:/remote/directory/ /local/directory/
   ```

3. 同步目錄並刪除目標位置中不再存在的檔案：
   ```csh
   rsync -avz --delete /local/directory/ user@remote:/remote/directory/
   ```

4. 僅同步特定類型的檔案，例如 `.txt` 檔案：
   ```csh
   rsync -avz --include='*.txt' --exclude='*' /local/directory/ user@remote:/remote/directory/
   ```

## Tips
- 在進行大規模同步之前，可以使用 `--dry-run` 選項來模擬執行，查看將要進行的操作而不實際執行。
- 定期備份重要資料，使用 `cron` 定時任務來自動化 `rsync` 操作。
- 確保在使用 `--delete` 選項時，先確認目標位置的檔案是否需要保留，以避免意外刪除重要檔案。