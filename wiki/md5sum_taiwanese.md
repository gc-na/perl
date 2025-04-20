# [台灣] C Shell (csh) md5sum 使用法: 計算檔案的 MD5 雜湊值

## Overview
md5sum 命令用於計算和驗證檔案的 MD5 雜湊值。這個雜湊值可以用來檢查檔案的完整性，確保檔案在傳輸或儲存過程中沒有被修改。

## Usage
基本語法如下：
```csh
md5sum [options] [arguments]
```

## Common Options
- `-b`：以二進位模式處理檔案。
- `-c`：檢查檔案的 MD5 雜湊值是否與給定的檔案匹配。
- `-t`：以文本模式處理檔案。

## Common Examples
1. 計算單一檔案的 MD5 雜湊值：
   ```csh
   md5sum example.txt
   ```

2. 計算多個檔案的 MD5 雜湊值：
   ```csh
   md5sum file1.txt file2.txt
   ```

3. 將 MD5 雜湊值輸出到檔案：
   ```csh
   md5sum example.txt > checksum.md5
   ```

4. 檢查 MD5 雜湊值：
   ```csh
   md5sum -c checksum.md5
   ```

## Tips
- 在使用 md5sum 前，確保檔案存在，以避免錯誤訊息。
- 將 MD5 雜湊值儲存到檔案中，可以方便未來的檢查。
- 使用 `-b` 選項來處理二進位檔案，確保計算的準確性。