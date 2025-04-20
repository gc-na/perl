# [台灣] C Shell (csh) strace 使用方式: 追蹤系統呼叫和信號

## Overview
`strace` 是一個用於追蹤程序執行過程中的系統呼叫和信號的工具。它可以幫助開發者和系統管理員了解程序的行為，調試問題，或分析性能。

## Usage
基本語法如下：
```
strace [options] [arguments]
```

## Common Options
- `-e trace=<set>`: 指定要追蹤的系統呼叫類型。
- `-p <pid>`: 附加到一個已經在運行的進程，並追蹤它的系統呼叫。
- `-o <file>`: 將輸出寫入指定的文件，而不是標準輸出。
- `-c`: 總結系統呼叫的統計信息。

## Common Examples
1. 追蹤一個程序的所有系統呼叫：
   ```bash
   strace ./my_program
   ```

2. 追蹤特定的系統呼叫，例如 `open` 和 `read`：
   ```bash
   strace -e trace=open,read ./my_program
   ```

3. 附加到已經在運行的進程，假設進程ID為1234：
   ```bash
   strace -p 1234
   ```

4. 將輸出寫入文件 `output.txt`：
   ```bash
   strace -o output.txt ./my_program
   ```

5. 獲取系統呼叫的統計信息：
   ```bash
   strace -c ./my_program
   ```

## Tips
- 在使用 `strace` 時，盡量只追蹤必要的系統呼叫，以減少輸出量，這樣更容易分析。
- 使用 `-o` 選項將輸出保存到文件中，可以方便後續的查看和分析。
- 結合 `grep` 使用，可以快速找到感興趣的系統呼叫：
  ```bash
  strace ./my_program | grep open
  ```