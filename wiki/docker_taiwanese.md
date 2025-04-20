# [台灣] C Shell (csh) docker 使用方式: 管理容器和映像檔

## Overview
docker 命令用於管理容器和映像檔，讓使用者能夠輕鬆地創建、運行和管理應用程式的容器化環境。這個命令是現代軟體開發和部署中不可或缺的工具。

## Usage
基本語法如下：
```
docker [options] [arguments]
```

## Common Options
- `run`: 創建並運行一個新的容器。
- `ps`: 列出當前正在運行的容器。
- `images`: 列出本地的所有映像檔。
- `rmi`: 刪除指定的映像檔。
- `exec`: 在運行中的容器內執行命令。

## Common Examples
以下是一些常見的使用範例：

1. **運行一個新的容器**
   ```bash
   docker run hello-world
   ```

2. **列出所有運行中的容器**
   ```bash
   docker ps
   ```

3. **列出所有本地映像檔**
   ```bash
   docker images
   ```

4. **刪除一個映像檔**
   ```bash
   docker rmi <image_id>
   ```

5. **在運行中的容器內執行命令**
   ```bash
   docker exec -it <container_id> /bin/bash
   ```

## Tips
- 確保定期清理不再使用的容器和映像檔，以節省磁碟空間。
- 使用 `docker-compose` 來管理多個容器的應用程式，這樣可以簡化配置和啟動過程。
- 在開發環境中使用 `--rm` 選項來自動刪除容器，這樣可以避免堆積不必要的容器。