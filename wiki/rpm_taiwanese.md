# [台灣] C Shell (csh) rpm 使用法: 管理 RPM 套件

## Overview
`rpm` 命令是用來管理 RPM 套件的工具，主要用於安裝、卸載、查詢和驗證 RPM 格式的軟體包。

## Usage
基本語法如下：
```csh
rpm [options] [arguments]
```

## Common Options
- `-i`：安裝一個新的 RPM 套件。
- `-e`：卸載已安裝的 RPM 套件。
- `-q`：查詢已安裝的 RPM 套件。
- `-v`：顯示詳細的輸出資訊。
- `-h`：在安裝過程中顯示進度條。

## Common Examples
安裝一個 RPM 套件：
```csh
rpm -i package.rpm
```

卸載一個已安裝的 RPM 套件：
```csh
rpm -e package_name
```

查詢已安裝的 RPM 套件：
```csh
rpm -q package_name
```

顯示已安裝套件的詳細資訊：
```csh
rpm -qi package_name
```

## Tips
- 在安裝或卸載套件之前，建議使用 `-q` 來確認套件是否已經存在。
- 使用 `-v` 和 `-h` 選項可以讓你在安裝過程中獲得更好的可視化反饋。
- 定期檢查系統中已安裝的 RPM 套件，以確保系統的整潔與安全。