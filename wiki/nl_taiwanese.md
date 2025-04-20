# [台灣] C Shell (csh) nl 使用法: 顯示檔案行號

## Overview
`nl` 命令用於在檔案的每一行前面添加行號，這對於查看和編輯文本檔案時非常有用。它可以幫助用戶更容易地定位特定行。

## Usage
基本語法如下：
```
nl [options] [arguments]
```

## Common Options
- `-b`：指定行號的格式，常用的有 `a`（所有行）和 `t`（僅對非空行）。
- `-f`：指定在每個檔案的開頭添加行號。
- `-n`：設置行號的格式，選項有 `ln`（左對齊）、`rn`（右對齊）和 `rz`（零填充）。

## Common Examples
以下是一些常見的使用範例：

1. 為檔案 `example.txt` 添加行號：
   ```csh
   nl example.txt
   ```

2. 只為非空行添加行號：
   ```csh
   nl -b t example.txt
   ```

3. 使用零填充格式的行號：
   ```csh
   nl -n rz example.txt
   ```

4. 將行號添加到多個檔案中：
   ```csh
   nl file1.txt file2.txt
   ```

## Tips
- 使用 `-b t` 選項可以讓輸出更整潔，特別是在處理長檔案時。
- 結合 `-n` 選項可以自定義行號的顯示方式，根據需要選擇合適的格式。
- 可以將 `nl` 命令的輸出重定向到新檔案中，以保存添加行號的結果：
  ```csh
  nl example.txt > numbered_example.txt
  ```