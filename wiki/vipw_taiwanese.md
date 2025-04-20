# [台灣] C Shell (csh) vipw 使用法: 編輯密碼檔案

## Overview
`vipw` 命令用於安全地編輯系統的密碼檔案，通常是 `/etc/passwd` 和 `/etc/shadow`。這個命令可以確保在編輯過程中不會有其他進程同時修改這些檔案，從而避免數據損壞。

## Usage
基本語法如下：
```
vipw [options] [arguments]
```

## Common Options
- `-s`：編輯 `/etc/shadow` 檔案。
- `-l`：以只讀模式打開檔案，防止意外修改。

## Common Examples
1. 編輯密碼檔案：
   ```bash
   vipw
   ```

2. 編輯影子檔案：
   ```bash
   vipw -s
   ```

3. 以只讀模式查看密碼檔案：
   ```bash
   vipw -l
   ```

## Tips
- 在使用 `vipw` 前，確保你有適當的權限，通常需要 root 權限。
- 編輯完成後，仔細檢查更改，避免因格式錯誤導致系統無法登錄。
- 使用 `vipw` 時，建議在終端機中保持其他進程的最小化，以便於檢查編輯的影響。