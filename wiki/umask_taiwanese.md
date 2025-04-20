# [台灣] C Shell (csh) umask 使用法: 設定檔案權限的預設值

## Overview
`umask` 命令用來設定新建立檔案和目錄的預設權限。它定義了在創建新檔案或目錄時，系統應該去除哪些權限。

## Usage
基本語法如下：
```csh
umask [options] [arguments]
```

## Common Options
- `-S`：以符號形式顯示當前的 umask 設定。
- `-p`：顯示當前的 umask 值，但不改變它。

## Common Examples
1. **查看當前 umask 設定**：
   ```csh
   umask
   ```

2. **以符號形式查看 umask**：
   ```csh
   umask -S
   ```

3. **設定 umask 值為 022**（使新檔案對群組和其他使用者只可讀）：
   ```csh
   umask 022
   ```

4. **設定 umask 值為 007**（使新檔案對其他使用者不可讀和不可執行）：
   ```csh
   umask 007
   ```

## Tips
- 在設定 umask 值時，請考慮安全性，確保不會意外地給予過多的權限。
- 可以在使用者的啟動檔（如 `.cshrc`）中設定 umask，以便每次登入時自動應用。
- 測試 umask 設定後，記得檢查新建立的檔案和目錄的權限，以確保它們符合預期。