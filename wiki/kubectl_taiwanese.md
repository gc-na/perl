# [台灣] C Shell (csh) kubectl 使用方式: 管理 Kubernetes 叢集

## Overview
`kubectl` 是 Kubernetes 的命令行工具，用於管理和操作 Kubernetes 叢集。它提供了一個簡單的介面來執行各種操作，如部署應用程式、檢查叢集狀態和管理資源。

## Usage
基本語法如下：
```
kubectl [options] [arguments]
```

## Common Options
- `get`: 獲取資源的列表或詳細資訊。
- `apply`: 應用配置變更到資源。
- `delete`: 刪除指定的資源。
- `describe`: 顯示資源的詳細資訊。
- `logs`: 查看 Pod 的日誌。

## Common Examples
1. 獲取所有 Pod 的列表：
   ```bash
   kubectl get pods
   ```

2. 應用配置檔案：
   ```bash
   kubectl apply -f deployment.yaml
   ```

3. 刪除一個特定的 Pod：
   ```bash
   kubectl delete pod my-pod
   ```

4. 顯示一個服務的詳細資訊：
   ```bash
   kubectl describe service my-service
   ```

5. 查看特定 Pod 的日誌：
   ```bash
   kubectl logs my-pod
   ```

## Tips
- 使用 `-n` 選項來指定命名空間，例如 `kubectl get pods -n my-namespace`。
- 定期使用 `kubectl get all` 來快速查看所有資源的狀態。
- 使用 `--help` 參數來獲取特定命令的幫助資訊，例如 `kubectl get --help`。