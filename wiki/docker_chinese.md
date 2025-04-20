# [操作系统] C Shell (csh) docker 使用等价: 管理容器和镜像

## 概述
docker 命令用于管理容器和镜像，它允许用户创建、运行和管理容器化应用程序。通过 docker，用户可以轻松地部署和管理应用程序环境，确保一致性和可移植性。

## 使用方法
基本语法如下：
```
docker [options] [arguments]
```

## 常用选项
- `run`：创建并启动一个新的容器。
- `ps`：列出当前运行的容器。
- `images`：列出本地可用的镜像。
- `pull`：从 Docker Hub 或其他注册表下载镜像。
- `build`：根据 Dockerfile 构建镜像。

## 常见示例
1. **运行一个新的容器**
   ```bash
   docker run hello-world
   ```

2. **列出所有运行中的容器**
   ```bash
   docker ps
   ```

3. **列出所有本地镜像**
   ```bash
   docker images
   ```

4. **从 Docker Hub 拉取镜像**
   ```bash
   docker pull ubuntu
   ```

5. **根据 Dockerfile 构建镜像**
   ```bash
   docker build -t my-image .
   ```

## 小贴士
- 在使用 `docker run` 时，可以使用 `-d` 选项在后台运行容器。
- 使用 `--rm` 选项可以在容器停止后自动删除它。
- 定期清理未使用的镜像和容器，以节省存储空间。可以使用 `docker system prune` 命令。