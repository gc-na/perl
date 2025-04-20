# [台灣] C Shell (csh) uniq 使用方法: 刪除重複行

## Overview
`uniq` 命令用於刪除相鄰的重複行。它通常與其他命令結合使用，例如 `sort`，以便在處理文本文件時更有效地過濾重複的數據。

## Usage
基本語法如下：
```
uniq [options] [arguments]
```

## Common Options
- `-c`: 計算每個唯一行出現的次數。
- `-d`: 只顯示重複的行。
- `-u`: 只顯示唯一的行，即不重複的行。
- `-i`: 忽略大小寫的差異。

## Common Examples
1. 刪除重複行：
   ```bash
   uniq input.txt output.txt
   ```

2. 計算每個唯一行的出現次數：
   ```bash
   uniq -c input.txt
   ```

3. 顯示重複的行：
   ```bash
   uniq -d input.txt
   ```

4. 忽略大小寫的重複行：
   ```bash
   uniq -i input.txt output.txt
   ```

## Tips
- 在使用 `uniq` 前，通常需要先對文件進行排序，以確保重複行是相鄰的。
- 可以將 `uniq` 與管道結合使用，以處理其他命令的輸出，例如：
  ```bash
  sort input.txt | uniq
  ```
- 使用 `-u` 選項可以快速找到不重複的行，這在數據分析中非常有用。