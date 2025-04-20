# [台灣] C Shell (csh) dirname 用法: 取得路徑的目錄部分

## Overview
`dirname` 命令用於從給定的路徑中提取目錄部分。這對於需要獲取文件所在目錄的情況非常有用。

## Usage
基本語法如下：
```
dirname [options] [arguments]
```

## Common Options
- `-z`：如果路徑為空，則返回空字串。
- `--help`：顯示幫助信息。

## Common Examples
以下是一些實用的範例：

1. 獲取單一文件的目錄：
   ```csh
   dirname /usr/local/bin/script.sh
   ```
   輸出：
   ```
   /usr/local/bin
   ```

2. 獲取相對路徑的目錄：
   ```csh
   dirname ./documents/report.txt
   ```
   輸出：
   ```
   ./documents
   ```

3. 使用變數獲取目錄：
   ```csh
   set filepath = /home/user/pictures/photo.jpg
   echo `dirname $filepath`
   ```
   輸出：
   ```
   /home/user/pictures
   ```

## Tips
- 在處理多個文件時，可以使用循環來獲取每個文件的目錄。
- 確保提供的路徑是有效的，以避免錯誤的輸出。