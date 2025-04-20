# [台灣] C Shell (csh) stty 使用法: 設定終端機屬性

## Overview
`stty` 命令用於設定和顯示終端機的屬性。它可以調整輸入和輸出的行為，讓使用者能夠更好地控制終端機的功能。

## Usage
基本語法如下：
```
stty [options] [arguments]
```

## Common Options
- `-a`：顯示所有的終端機屬性。
- `-g`：以可重用的格式顯示當前的設定。
- `erase`：設定刪除鍵的功能。
- `kill`：設定用於刪除整行的鍵。
- `intr`：設定中斷鍵的功能。

## Common Examples
以下是一些常見的 `stty` 使用範例：

1. 顯示當前終端機的所有屬性：
   ```csh
   stty -a
   ```

2. 設定刪除鍵為 `Ctrl + H`：
   ```csh
   stty erase ^H
   ```

3. 設定中斷鍵為 `Ctrl + C`：
   ```csh
   stty intr ^C
   ```

4. 以可重用格式顯示當前設定：
   ```csh
   stty -g
   ```

## Tips
- 在修改終端機屬性之前，使用 `stty -a` 來查看當前設定，以便於回復。
- 如果不小心更改了設定，可以使用 `stty sane` 來恢復到合理的預設值。
- 熟悉常用的鍵盤快捷鍵設定，可以提高終端機的使用效率。