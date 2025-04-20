# [台灣] C Shell (csh) sha256sum 使用法: 計算檔案的 SHA-256 雜湊值

## Overview
`sha256sum` 是一個用來計算和檢查檔案的 SHA-256 雜湊值的命令。這個命令可以幫助使用者驗證檔案的完整性，確保檔案在傳輸或儲存過程中沒有被修改。

## Usage
基本語法如下：
```csh
sha256sum [options] [arguments]
```

## Common Options
- `-b`：以二進位模式讀取檔案。
- `-c`：檢查檔案的 SHA-256 雜湊值。
- `-h`：顯示幫助信息。
- `-o <file>`：將輸出寫入指定的檔案。

## Common Examples
以下是一些常見的使用範例：

1. 計算單個檔案的 SHA-256 雜湊值：
   ```csh
   sha256sum filename.txt
   ```

2. 計算多個檔案的 SHA-256 雜湊值：
   ```csh
   sha256sum file1.txt file2.txt file3.txt
   ```

3. 將 SHA-256 雜湊值輸出到檔案：
   ```csh
   sha256sum filename.txt > hash.txt
   ```

4. 檢查檔案的 SHA-256 雜湊值：
   ```csh
   sha256sum -c hash.txt
   ```

## Tips
- 在計算雜湊值之前，確保檔案名稱正確，避免錯誤的輸出。
- 使用 `-o` 選項可以將結果直接寫入檔案，方便後續使用。
- 定期檢查檔案的雜湊值可以幫助發現未經授權的變更。