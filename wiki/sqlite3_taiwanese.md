# [台灣] C Shell (csh) sqlite3 使用法: 操作 SQLite 資料庫

## Overview
sqlite3 是一個命令行工具，用於與 SQLite 資料庫進行互動。它允許用戶執行 SQL 查詢、創建和修改資料庫，以及管理資料表和資料。

## Usage
基本語法如下：
```csh
sqlite3 [options] [arguments]
```

## Common Options
- `-help`：顯示幫助信息。
- `-version`：顯示 sqlite3 的版本。
- `-init <file>`：在啟動時執行指定的 SQL 文件。
- `-batch`：以批處理模式運行，適合自動化腳本。

## Common Examples
1. **打開一個資料庫**
   ```csh
   sqlite3 mydatabase.db
   ```

2. **執行 SQL 查詢**
   ```csh
   sqlite3 mydatabase.db "SELECT * FROM users;"
   ```

3. **從文件導入數據**
   ```csh
   sqlite3 mydatabase.db ".import data.csv users"
   ```

4. **導出資料表到文件**
   ```csh
   sqlite3 mydatabase.db "SELECT * FROM users;" > output.txt
   ```

5. **創建資料表**
   ```csh
   sqlite3 mydatabase.db "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);"
   ```

## Tips
- 使用 `.exit` 或 `Ctrl+D` 來安全退出 sqlite3。
- 在執行複雜查詢之前，建議先在小型測試資料庫中進行測試。
- 定期備份資料庫，以防數據丟失。