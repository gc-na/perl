# [台灣] C Shell (csh) basename 用法: 獲取檔案名稱

## Overview
`basename` 命令用於從完整的檔案路徑中提取檔案名稱，去除路徑和檔案擴展名。這在處理檔案時非常有用，特別是當你只想要檔案的名稱而不需要其他資訊時。

## Usage
基本語法如下：
```
basename [options] [arguments]
```

## Common Options
- `-a`：處理多個檔案名稱，返回每個檔案的名稱。
- `-s`：指定要去除的檔案擴展名。

## Common Examples
以下是一些常見的使用範例：

1. 提取檔案名稱：
   ```csh
   basename /usr/local/bin/script.sh
   ```
   輸出：
   ```
   script.sh
   ```

2. 去除檔案擴展名：
   ```csh
   basename /usr/local/bin/script.sh .sh
   ```
   輸出：
   ```
   script
   ```

3. 處理多個檔案：
   ```csh
   basename -a /usr/local/bin/script1.sh /usr/local/bin/script2.sh
   ```
   輸出：
   ```
   script1.sh
   script2.sh
   ```

4. 去除特定擴展名：
   ```csh
   basename /home/user/document.txt .txt
   ```
   輸出：
   ```
   document
   ```

## Tips
- 當需要處理多個檔案時，使用 `-a` 選項可以一次性獲取所有檔案名稱。
- 使用 `-s` 選項可以方便地去除檔案的特定擴展名，這對於批量處理檔案非常有用。
- 結合其他命令，如 `find`，可以更有效地管理檔案名稱的提取和處理。