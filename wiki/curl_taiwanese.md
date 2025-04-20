# [台灣] C Shell (csh) curl 使用方式: 用於傳輸數據的命令

## Overview
curl 是一個用於從或向伺服器傳輸數據的命令行工具。它支持多種協議，包括 HTTP、HTTPS、FTP 等，並且可以用來下載或上傳文件。

## Usage
基本語法如下：
```csh
curl [options] [arguments]
```

## Common Options
- `-O`：將下載的文件保存為原始文件名。
- `-L`：自動跟隨重定向。
- `-u`：用於提供用戶名和密碼，格式為 `username:password`。
- `-d`：用於發送 POST 請求的數據。
- `-I`：僅獲取 HTTP 標頭。

## Common Examples
以下是一些常見的使用範例：

1. 下載一個文件並保存為原始文件名：
   ```csh
   curl -O https://example.com/file.zip
   ```

2. 自動跟隨重定向並下載文件：
   ```csh
   curl -L -O https://example.com/redirected-file.zip
   ```

3. 使用用戶名和密碼進行身份驗證：
   ```csh
   curl -u username:password https://example.com/protected
   ```

4. 發送 POST 請求並附加數據：
   ```csh
   curl -d "param1=value1&param2=value2" https://example.com/submit
   ```

5. 獲取 HTTP 標頭而不下載內容：
   ```csh
   curl -I https://example.com
   ```

## Tips
- 使用 `-O` 選項時，確保你有適當的權限來保存文件。
- 當需要處理重定向時，記得使用 `-L` 選項。
- 對於需要身份驗證的請求，使用 `-u` 提供用戶名和密碼。
- 測試 API 時，可以使用 `-d` 選項來發送 JSON 數據，並搭配 `-H "Content-Type: application/json"` 指定內容類型。