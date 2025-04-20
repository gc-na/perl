# [台灣] C Shell (csh) iconv 使用方式: 轉換文字編碼

## Overview
`iconv` 是一個用於轉換文件或標準輸入的文字編碼的命令。它可以讓使用者在不同的編碼格式之間進行轉換，這在處理多語言文本時特別有用。

## Usage
基本語法如下：
```
iconv [options] [arguments]
```

## Common Options
- `-f`：指定輸入文件的編碼格式。
- `-t`：指定輸出文件的編碼格式。
- `-o`：將輸出寫入到指定的文件，而不是標準輸出。
- `-c`：忽略無法轉換的字符。

## Common Examples
以下是一些常見的使用範例：

1. 將 UTF-8 編碼的文件轉換為 ISO-8859-1 編碼：
   ```csh
   iconv -f UTF-8 -t ISO-8859-1 input.txt -o output.txt
   ```

2. 將標準輸入的 UTF-16 編碼轉換為 UTF-8 編碼：
   ```csh
   iconv -f UTF-16 -t UTF-8 < input.txt > output.txt
   ```

3. 忽略無法轉換的字符，將 ASCII 編碼轉換為 UTF-8 編碼：
   ```csh
   iconv -f ASCII -t UTF-8 -c input.txt -o output.txt
   ```

## Tips
- 確保知道源文件的編碼格式，這樣可以避免轉換錯誤。
- 使用 `-o` 選項來指定輸出文件，這樣可以保留原始文件不變。
- 在轉換之前，可以使用 `file` 命令來檢查文件的編碼格式。