# [台灣] C Shell (csh) stat 使用法: 獲取文件狀態資訊

## Overview
`stat` 命令用於顯示文件或文件系統的狀態資訊，包括大小、權限、擁有者、修改時間等。

## Usage
基本語法如下：
```
stat [options] [arguments]
```

## Common Options
- `-c`：自定義輸出格式。
- `-f`：顯示文件系統的狀態資訊。
- `-L`：跟隨符號鏈接顯示目標文件的狀態。

## Common Examples
1. 顯示單個文件的狀態資訊：
   ```csh
   stat filename.txt
   ```

2. 使用自定義格式顯示文件大小和修改時間：
   ```csh
   stat -c '%s %y' filename.txt
   ```

3. 顯示目錄的狀態資訊：
   ```csh
   stat /path/to/directory
   ```

4. 跟隨符號鏈接顯示目標文件的狀態：
   ```csh
   stat -L symlink
   ```

## Tips
- 使用 `-c` 選項可以自定義輸出，讓資訊更符合你的需求。
- 當需要檢查多個文件時，可以將文件名放在命令後面，`stat file1.txt file2.txt`。
- 若要獲取文件系統的詳細資訊，使用 `-f` 選項是非常有用的。