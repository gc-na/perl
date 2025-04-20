# [台灣] C Shell (csh) head 用法： 顯示檔案的前幾行

## Overview
`head` 命令用來顯示檔案的前幾行內容。這對於快速查看檔案的開頭部分非常有用，特別是在處理大型檔案時。

## Usage
基本語法如下：
```
head [options] [arguments]
```

## Common Options
- `-n [number]`：指定要顯示的行數，預設為10行。
- `-q`：在顯示多個檔案時，不顯示檔案名稱。
- `-v`：在顯示多個檔案時，顯示檔案名稱。

## Common Examples
- 顯示檔案 `example.txt` 的前10行：
  ```csh
  head example.txt
  ```

- 顯示檔案 `example.txt` 的前5行：
  ```csh
  head -n 5 example.txt
  ```

- 顯示多個檔案的前10行，並顯示檔案名稱：
  ```csh
  head -v file1.txt file2.txt
  ```

- 顯示檔案 `example.txt` 的前20行，不顯示檔案名稱：
  ```csh
  head -q -n 20 example.txt
  ```

## Tips
- 使用 `head` 來快速檢查檔案的格式或內容，特別是在處理大型檔案時。
- 結合其他命令使用，例如 `grep`，可以先用 `head` 篩選出感興趣的行。
- 如果你只想查看檔案的開頭部分，使用 `-n` 選項來減少輸出行數，這樣更方便閱讀。