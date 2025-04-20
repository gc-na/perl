# [台灣] C Shell (csh) grep 用法: 搜尋文本中的模式

## Overview
`grep` 是一個強大的命令行工具，用於在文本中搜尋特定的模式或字串。它可以從檔案或標準輸入中過濾出符合條件的行，並顯示出來。

## Usage
基本的語法如下：
```
grep [options] [arguments]
```

## Common Options
- `-i`：忽略大小寫。
- `-v`：反向匹配，顯示不符合模式的行。
- `-r`：遞迴搜尋目錄中的檔案。
- `-n`：顯示行號。
- `-l`：僅顯示包含匹配模式的檔案名稱。

## Common Examples
以下是一些常見的用法示例：

1. 搜尋檔案中的字串：
   ```shell
   grep "hello" file.txt
   ```

2. 忽略大小寫搜尋：
   ```shell
   grep -i "hello" file.txt
   ```

3. 反向匹配，顯示不包含字串的行：
   ```shell
   grep -v "hello" file.txt
   ```

4. 遞迴搜尋目錄中的所有檔案：
   ```shell
   grep -r "hello" /path/to/directory
   ```

5. 顯示行號：
   ```shell
   grep -n "hello" file.txt
   ```

## Tips
- 使用 `-i` 選項可以在搜尋時不受大小寫影響，這對於不確定字母大小寫的情況特別有用。
- 結合 `-r` 和 `-l` 可以快速找到包含特定字串的檔案名稱，這在處理大型專案時非常方便。
- 如果需要搜尋多個字串，可以使用 `-e` 選項來指定多個模式。