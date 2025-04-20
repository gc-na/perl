# [台灣] C Shell (csh) helm 使用法: 管理 Kubernetes 應用程式

## Overview
`helm` 是一個用於管理 Kubernetes 應用程式的工具，它可以幫助用戶簡化應用程式的部署和管理過程。透過使用 Helm，您可以輕鬆地安裝、升級和刪除 Kubernetes 應用程式，並管理其配置。

## Usage
基本語法如下：
```csh
helm [options] [arguments]
```

## Common Options
- `install`: 安裝一個新的 Helm chart。
- `upgrade`: 升級已安裝的 Helm chart。
- `uninstall`: 卸載已安裝的 Helm chart。
- `list`: 列出所有已安裝的 Helm releases。
- `repo`: 管理 Helm chart 的倉庫。

## Common Examples
以下是一些常見的使用範例：

### 安裝一個 Helm chart
```csh
helm install my-release stable/mysql
```

### 升級已安裝的 Helm chart
```csh
helm upgrade my-release stable/mysql
```

### 卸載已安裝的 Helm chart
```csh
helm uninstall my-release
```

### 列出所有已安裝的 Helm releases
```csh
helm list
```

### 添加一個新的 Helm chart 倉庫
```csh
helm repo add my-repo https://example.com/charts
```

## Tips
- 在使用 Helm 之前，確保您的 Kubernetes 環境已正確設置。
- 定期更新您的 Helm chart 倉庫，以獲取最新的應用程式版本。
- 使用 `helm history <release-name>` 查看特定 release 的歷史紀錄，方便追蹤變更。