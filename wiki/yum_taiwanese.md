# [台灣] C Shell (csh) yum 使用方式: 管理軟體包

## Overview
`yum` 是一個用於管理 Linux 系統上軟體包的命令行工具。它可以幫助用戶安裝、更新和刪除軟體包，並且能自動處理依賴關係。

## Usage
基本語法如下：
```
yum [options] [arguments]
```

## Common Options
- `install`：安裝指定的軟體包。
- `remove`：刪除指定的軟體包。
- `update`：更新已安裝的軟體包到最新版本。
- `list`：列出可用的或已安裝的軟體包。
- `search`：搜索指定的軟體包。

## Common Examples
- 安裝一個軟體包：
  ```bash
  yum install package_name
  ```

- 刪除一個軟體包：
  ```bash
  yum remove package_name
  ```

- 更新所有已安裝的軟體包：
  ```bash
  yum update
  ```

- 列出所有可用的軟體包：
  ```bash
  yum list available
  ```

- 搜索特定的軟體包：
  ```bash
  yum search package_name
  ```

## Tips
- 在執行 `yum` 命令之前，建議使用 `yum check-update` 來檢查可用的更新。
- 使用 `-y` 選項可以自動回答所有提示，適合批次安裝：
  ```bash
  yum install -y package_name
  ```
- 定期清理快取以釋放空間，可以使用 `yum clean all` 命令。