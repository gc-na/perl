# [台灣] C Shell (csh) sftp 使用法: 用於安全檔案傳輸

## Overview
sftp（SSH File Transfer Protocol）是一種安全的檔案傳輸協定，允許用戶在網路上安全地傳輸檔案。它基於SSH協定，提供了加密的連接，確保資料在傳輸過程中的安全性。

## Usage
基本的sftp命令語法如下：
```
sftp [options] [user@]host
```

## Common Options
- `-b batchfile`：使用批次檔進行自動化傳輸。
- `-C`：啟用壓縮，減少傳輸的資料量。
- `-o`：指定sftp的選項，例如`-oPort=2222`來指定連接埠。
- `-P port`：指定連接的埠號。

## Common Examples
以下是一些常見的sftp使用範例：

1. 連接到遠端主機：
   ```bash
   sftp user@hostname
   ```

2. 上傳檔案到遠端主機：
   ```bash
   sftp user@hostname
   put localfile.txt
   ```

3. 從遠端主機下載檔案：
   ```bash
   sftp user@hostname
   get remotefile.txt
   ```

4. 使用批次檔自動傳輸：
   ```bash
   sftp -b batchfile.txt user@hostname
   ```

5. 使用壓縮進行傳輸：
   ```bash
   sftp -C user@hostname
   ```

## Tips
- 在使用sftp時，確保你的SSH金鑰已正確配置，以便無需每次都輸入密碼。
- 使用`-b`選項可以自動化重複的傳輸任務，節省時間。
- 定期檢查檔案傳輸的完整性，確保資料未被損壞。