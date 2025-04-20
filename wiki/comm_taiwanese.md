# [台灣] C Shell (csh) comm 使用法: 比較兩個已排序的檔案

## Overview
`comm` 命令用於比較兩個已排序的檔案，並顯示它們之間的差異。這個命令會列出三個部分：只在第一個檔案中出現的行、只在第二個檔案中出現的行，以及兩個檔案中都出現的行。

## Usage
基本語法如下：
```csh
comm [options] [file1] [file2]
```

## Common Options
- `-1`：不顯示只在第一個檔案中出現的行。
- `-2`：不顯示只在第二個檔案中出現的行。
- `-3`：不顯示在兩個檔案中都出現的行。
- `-i`：在比較時忽略大小寫。

## Common Examples
以下是一些實用的例子：

1. 比較兩個檔案並顯示所有差異：
   ```csh
   comm file1.txt file2.txt
   ```

2. 只顯示在 `file1.txt` 中出現的行：
   ```csh
   comm -13 file1.txt file2.txt
   ```

3. 只顯示在 `file2.txt` 中出現的行：
   ```csh
   comm -23 file1.txt file2.txt
   ```

4. 忽略大小寫進行比較：
   ```csh
   comm -i file1.txt file2.txt
   ```

## Tips
- 確保在使用 `comm` 命令之前，兩個檔案都是已排序的，否則結果可能不正確。
- 可以使用 `sort` 命令對檔案進行排序，例如：
  ```csh
  sort file1.txt > sorted_file1.txt
  sort file2.txt > sorted_file2.txt
  comm sorted_file1.txt sorted_file2.txt
  ```
- 使用選項時，可以根據需要組合多個選項來獲得所需的輸出。