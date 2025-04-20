# [台灣] C Shell (csh) sha512sum 用法: 計算檔案的 SHA-512 雜湊值

## Overview
`sha512sum` 是一個用於計算和驗證檔案的 SHA-512 雜湊值的命令。這個命令可以幫助用戶確保檔案的完整性，檢查檔案是否在傳輸或存儲過程中被修改。

## Usage
基本語法如下：
```csh
sha512sum [options] [arguments]
```

## Common Options
- `-b`：以二進位模式讀取檔案。
- `-c`：檢查檔案的 SHA-512 雜湊值。
- `-h`：顯示幫助信息。
- `--tag`：輸出雜湊值與檔案名的標籤格式。

## Common Examples
1. 計算單個檔案的 SHA-512 雜湊值：
   ```csh
   sha512sum example.txt
   ```

2. 計算多個檔案的 SHA-512 雜湊值：
   ```csh
   sha512sum file1.txt file2.txt
   ```

3. 將 SHA-512 雜湊值輸出到檔案：
   ```csh
   sha512sum example.txt > example.sha512
   ```

4. 檢查檔案的 SHA-512 雜湊值：
   ```csh
   sha512sum -c example.sha512
   ```

## Tips
- 在進行檔案傳輸或備份時，建議計算並保存 SHA-512 雜湊值，以便日後檢查檔案的完整性。
- 使用 `-b` 選項可以確保在處理二進位檔案時不會出現問題。
- 定期檢查檔案的雜湊值可以及早發現檔案損壞或被篡改的情況。