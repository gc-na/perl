# [台灣] C Shell (csh) wget 使用法: 下載檔案的工具

## Overview
`wget` 是一個用於從網路上下載檔案的命令行工具。它支援 HTTP、HTTPS 和 FTP 協議，並且可以在不需要使用者介入的情況下進行下載。

## Usage
基本語法如下：
```
wget [options] [arguments]
```

## Common Options
- `-O <file>`: 指定下載後檔案的名稱。
- `-c`: 繼續未完成的下載。
- `-q`: 靜默模式，不顯示進度。
- `--limit-rate=<rate>`: 限制下載速度。
- `-r`: 進行遞迴下載。

## Common Examples
以下是一些常見的使用範例：

1. 下載單一檔案：
   ```bash
   wget https://example.com/file.zip
   ```

2. 指定下載檔案名稱：
   ```bash
   wget -O myfile.zip https://example.com/file.zip
   ```

3. 繼續未完成的下載：
   ```bash
   wget -c https://example.com/largefile.zip
   ```

4. 靜默下載：
   ```bash
   wget -q https://example.com/file.zip
   ```

5. 遞迴下載整個網站：
   ```bash
   wget -r https://example.com/
   ```

## Tips
- 使用 `-c` 選項可以避免重複下載已經下載的部分，節省時間和帶寬。
- 在下載大檔案時，可以使用 `--limit-rate` 來控制下載速度，以免佔用過多的網路資源。
- 在下載網站時，請遵守網站的使用條款，避免過度請求導致伺服器負擔。