# [台灣] C Shell (csh) dpkg 使用法: 管理 Debian 套件

## Overview
`dpkg` 是一個用於管理 Debian 和 Ubuntu 系統上軟體包的命令行工具。它可以安裝、移除和管理已安裝的套件，並且能夠提供有關這些套件的詳細資訊。

## Usage
基本語法如下：
```
dpkg [options] [arguments]
```

## Common Options
- `-i`：安裝指定的套件。
- `-r`：移除指定的套件，但保留其配置文件。
- `-P`：完全移除指定的套件，包括配置文件。
- `-l`：列出所有已安裝的套件。
- `-s`：顯示指定套件的狀態資訊。
- `--get-selections`：列出所有已安裝的套件及其選擇狀態。

## Common Examples
以下是一些常見的 `dpkg` 使用範例：

1. 安裝套件：
   ```bash
   dpkg -i package.deb
   ```

2. 移除套件：
   ```bash
   dpkg -r package_name
   ```

3. 完全移除套件：
   ```bash
   dpkg -P package_name
   ```

4. 列出所有已安裝的套件：
   ```bash
   dpkg -l
   ```

5. 顯示特定套件的狀態：
   ```bash
   dpkg -s package_name
   ```

6. 列出所有已安裝的套件及其狀態：
   ```bash
   dpkg --get-selections
   ```

## Tips
- 在安裝套件之前，確保已經下載了正確的 `.deb` 檔案。
- 使用 `dpkg -l` 可以快速檢查系統中已安裝的套件，方便管理。
- 如果在安裝過程中遇到依賴問題，考慮使用 `apt` 工具來解決依賴關係。