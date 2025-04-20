# [操作系统] C Shell (csh) docker-compose 用法: 管理多容器Docker应用

## 概述
docker-compose 是一个用于定义和运行多容器 Docker 应用的工具。通过使用 YAML 文件来配置应用服务，用户可以轻松地管理和部署多个容器。

## 用法
基本语法如下：
```bash
docker-compose [options] [arguments]
```

## 常用选项
- `up`：启动服务并创建容器。
- `down`：停止并删除容器、网络和卷。
- `build`：根据 Dockerfile 构建服务镜像。
- `logs`：查看服务的输出日志。
- `exec`：在运行的容器中执行命令。

## 常见示例
1. 启动服务：
   ```bash
   docker-compose up
   ```

2. 在后台启动服务：
   ```bash
   docker-compose up -d
   ```

3. 停止服务并删除容器：
   ```bash
   docker-compose down
   ```

4. 查看服务日志：
   ```bash
   docker-compose logs
   ```

5. 在特定服务的容器中执行命令：
   ```bash
   docker-compose exec <service_name> <command>
   ```

## 提示
- 使用 `-d` 选项可以在后台运行服务，适合生产环境。
- 定期使用 `docker-compose down` 清理不再使用的容器和网络。
- 在修改 `docker-compose.yml` 文件后，使用 `docker-compose up` 重新启动服务以应用更改。