# [台灣] C Shell (csh) cp 使用方式: 複製檔案和目錄

## Overview
`cp` 命令用於在檔案系統中複製檔案和目錄。它可以將一個或多個檔案複製到指定的目的地，並且可以選擇性地覆蓋現有檔案。

## Usage
基本語法如下：
```
cp [options] [arguments]
```

## Common Options
- `-i`：在覆蓋檔案之前提示使用者確認。
- `-r`：遞迴複製目錄及其內容。
- `-u`：只複製源檔案比目的檔案更新的檔案。
- `-v`：在複製過程中顯示詳細信息。

## Common Examples
1. 複製單一檔案：
   ```csh
   cp file1.txt file2.txt
   ```

2. 複製並覆蓋檔案，並提示確認：
   ```csh
   cp -i file1.txt file2.txt
   ```

3. 遞迴複製目錄：
   ```csh
   cp -r dir1/ dir2/
   ```

4. 只複製更新的檔案：
   ```csh
   cp -u file1.txt file2.txt
   ```

5. 顯示詳細的複製過程：
   ```csh
   cp -v file1.txt file2.txt
   ```

## Tips
- 使用 `-i` 選項可以避免意外覆蓋重要檔案。
- 在複製大型目錄時，建議使用 `-v` 來監控進度。
- 確保目的地路徑存在，否則 `cp` 可能會報錯。