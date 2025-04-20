# [台灣] C Shell (csh) scp 用法: 複製檔案至遠端伺服器

## Overview
`scp`（Secure Copy Protocol）是一個用於安全地在本地和遠端伺服器之間複製檔案的命令。它使用 SSH 協議來加密傳輸，確保資料的安全性。

## Usage
基本語法如下：
```csh
scp [options] [source] [destination]
```

## Common Options
- `-r`：遞迴複製整個目錄。
- `-P`：指定遠端主機的端口號（注意是大寫的 P）。
- `-i`：指定使用的身份驗證金鑰文件。
- `-v`：顯示詳細的輸出，方便除錯。

## Common Examples
以下是一些常見的 `scp` 使用範例：

1. 複製本地檔案到遠端伺服器：
   ```csh
   scp localfile.txt user@remotehost:/path/to/destination/
   ```

2. 從遠端伺服器複製檔案到本地：
   ```csh
   scp user@remotehost:/path/to/remotefile.txt /local/destination/
   ```

3. 遞迴複製整個目錄到遠端伺服器：
   ```csh
   scp -r localdirectory/ user@remotehost:/path/to/destination/
   ```

4. 使用指定的端口號複製檔案：
   ```csh
   scp -P 2222 localfile.txt user@remotehost:/path/to/destination/
   ```

## Tips
- 確保你有適當的權限來訪問遠端伺服器。
- 使用 `-v` 選項可以幫助你了解傳輸過程中的問題。
- 考慮使用 SSH 金鑰來簡化身份驗證過程，避免每次都輸入密碼。