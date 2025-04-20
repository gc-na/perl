# [台灣] C Shell (csh) script 使用法: 記錄終端輸出

## Overview
`script` 命令用來記錄終端的輸出，並將這些輸出保存到一個檔案中。這對於需要保存會話記錄或進行後續檢查的情況非常有用。

## Usage
基本語法如下：
```
script [options] [arguments]
```

## Common Options
- `-a`：將輸出附加到已存在的檔案，而不是覆蓋它。
- `-f`：即時顯示輸出，讓使用者可以即時看到記錄的內容。
- `-q`：靜默模式，啟用後不會顯示開始和結束的提示。

## Common Examples
以下是一些常見的使用範例：

1. 開始記錄會話並將輸出保存到 `session.log` 檔案：
   ```csh
   script session.log
   ```

2. 附加輸出到已存在的檔案：
   ```csh
   script -a session.log
   ```

3. 在即時模式下記錄輸出：
   ```csh
   script -f session.log
   ```

4. 使用靜默模式記錄會話：
   ```csh
   script -q session.log
   ```

## Tips
- 確保在結束記錄時使用 `exit` 命令，這樣可以正確關閉 `script` 會話。
- 定期檢查生成的記錄檔案，以確保它們不會變得過於龐大。
- 使用 `cat` 或 `less` 命令查看記錄檔案的內容，方便後續查閱。