# [台灣] C Shell (csh) ftp 使用法: 用於檔案傳輸的命令

## Overview
ftp 命令是一個用於在網路上傳輸檔案的工具，允許用戶透過文件傳輸協定（File Transfer Protocol）來上傳或下載檔案。

## Usage
基本語法如下：
```
ftp [options] [arguments]
```

## Common Options
- `-i`：以二進位模式傳輸檔案，適合傳輸非文本檔案。
- `-v`：顯示詳細的傳輸過程，方便用戶了解進度。
- `-n`：不自動登入，適合需要手動輸入用戶名和密碼的情況。

## Common Examples
以下是一些常見的 ftp 使用範例：

1. 連接到 FTP 伺服器：
   ```csh
   ftp ftp.example.com
   ```

2. 使用指定的用戶名登入：
   ```csh
   ftp -n ftp.example.com
   user myusername mypassword
   ```

3. 下載檔案：
   ```csh
   ftp> get myfile.txt
   ```

4. 上傳檔案：
   ```csh
   ftp> put myfile.txt
   ```

5. 列出伺服器上的檔案：
   ```csh
   ftp> ls
   ```

## Tips
- 在使用 ftp 進行檔案傳輸時，建議使用 `-i` 選項來避免檔案傳輸過程中的換行符號問題。
- 確保在傳輸敏感資料時使用安全的傳輸協定，如 SFTP，以提高安全性。
- 在連接到 FTP 伺服器後，使用 `binary` 命令切換到二進位模式，以確保檔案的完整性。