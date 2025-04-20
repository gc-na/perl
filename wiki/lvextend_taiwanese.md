# [台灣] C Shell (csh) lvextend 使用方法: 擴展邏輯卷的大小

## Overview
`lvextend` 命令用於擴展邏輯卷的大小，使其能夠使用更多的物理存儲空間。這對於需要更多存儲的應用程序或系統非常有用。

## Usage
基本語法如下：
```
lvextend [options] [arguments]
```

## Common Options
- `-L +size`：增加指定大小的空間。
- `-l +size`：以邏輯區塊數量增加空間。
- `-r`：在擴展邏輯卷的同時自動擴展文件系統。

## Common Examples
1. 擴展邏輯卷 10G：
   ```bash
   lvextend -L +10G /dev/vg_name/lv_name
   ```

2. 以邏輯區塊增加 100 個區塊：
   ```bash
   lvextend -l +100 /dev/vg_name/lv_name
   ```

3. 同時擴展邏輯卷和文件系統：
   ```bash
   lvextend -r -L +5G /dev/vg_name/lv_name
   ```

## Tips
- 在執行 `lvextend` 前，確保已經備份重要數據，以防不測。
- 使用 `-r` 選項可以節省時間，因為它會自動擴展文件系統。
- 定期檢查邏輯卷的使用情況，以便及時擴展。