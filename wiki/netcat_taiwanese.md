# [台灣] C Shell (csh) netcat 使用法: 網路連接工具

## Overview
netcat（通常簡稱為 nc）是一個功能強大的網路工具，可以用來讀取和寫入網路連接，支援 TCP 和 UDP 協議。它常用於網路調試和資料傳輸。

## Usage
基本語法如下：
```
netcat [options] [arguments]
```

## Common Options
- `-l`：啟動一個伺服器模式，等待連接。
- `-p`：指定伺服器模式下的埠號。
- `-u`：使用 UDP 而不是 TCP。
- `-v`：啟用詳細模式，顯示更多的運行資訊。
- `-z`：掃描模式，僅檢查指定埠是否開放。

## Common Examples
以下是一些常見的使用範例：

1. **建立 TCP 連接**
   ```bash
   netcat example.com 80
   ```

2. **啟動伺服器並監聽指定埠**
   ```bash
   netcat -l -p 1234
   ```

3. **使用 UDP 傳輸資料**
   ```bash
   netcat -u -l -p 1234
   ```

4. **掃描開放的埠**
   ```bash
   netcat -z -v example.com 1-100
   ```

5. **從檔案傳輸資料**
   ```bash
   netcat -l -p 1234 < file.txt
   ```

## Tips
- 使用 `-v` 選項可以幫助你了解連接的詳細資訊，特別是在調試時。
- 當使用伺服器模式時，確保埠號不被其他服務佔用。
- 結合其他命令使用管道，可以進行更複雜的資料處理和傳輸。