# [台灣] C Shell (csh) 7z 使用法: 壓縮和解壓縮檔案

## Overview
7z 是一個強大的檔案壓縮和解壓縮工具，支援多種壓縮格式。它能有效地減少檔案大小，方便儲存和傳輸。

## Usage
基本語法如下：
```
7z [options] [arguments]
```

## Common Options
- `a`: 添加檔案到壓縮檔案。
- `x`: 解壓縮檔案。
- `t`: 測試壓縮檔案的完整性。
- `l`: 列出壓縮檔案中的檔案。
- `d`: 刪除壓縮檔案中的檔案。

## Common Examples
- 壓縮檔案：
  ```bash
  7z a archive.7z file1.txt file2.txt
  ```
  
- 解壓縮檔案：
  ```bash
  7z x archive.7z
  ```

- 列出壓縮檔案中的檔案：
  ```bash
  7z l archive.7z
  ```

- 測試壓縮檔案的完整性：
  ```bash
  7z t archive.7z
  ```

- 刪除壓縮檔案中的特定檔案：
  ```bash
  7z d archive.7z file1.txt
  ```

## Tips
- 使用 `-p` 選項來為壓縮檔案設置密碼，增加安全性。
- 定期測試壓縮檔案的完整性，以確保檔案未損壞。
- 將常用的命令寫入別名，方便快速使用。