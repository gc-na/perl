# [Linux] C Shell (csh) docker uso equivalente: Gestione dei container

## Overview
The `docker` command is a powerful tool used to manage containers in a Docker environment. It allows users to create, run, stop, and manage containerized applications, making it easier to deploy and scale applications in a consistent manner.

## Usage
The basic syntax of the `docker` command is as follows:

```bash
docker [options] [arguments]
```

## Common Options
- `run`: Create and start a container.
- `ps`: List running containers.
- `stop`: Stop a running container.
- `rm`: Remove a stopped container.
- `images`: List all images on the local machine.
- `pull`: Download an image from a Docker registry.
- `build`: Build an image from a Dockerfile.

## Common Examples
Here are some practical examples of using the `docker` command:

1. **Run a container**:
   ```bash
   docker run hello-world
   ```

2. **List running containers**:
   ```bash
   docker ps
   ```

3. **Stop a running container**:
   ```bash
   docker stop <container_id>
   ```

4. **Remove a stopped container**:
   ```bash
   docker rm <container_id>
   ```

5. **List all images**:
   ```bash
   docker images
   ```

6. **Pull an image from Docker Hub**:
   ```bash
   docker pull ubuntu
   ```

7. **Build an image from a Dockerfile**:
   ```bash
   docker build -t my-image .
   ```

## Tips
- Always check the status of your containers with `docker ps` to ensure they are running as expected.
- Use `docker logs <container_id>` to view the logs of a specific container for troubleshooting.
- Tag your images appropriately when building to keep track of different versions.
- Regularly clean up unused containers and images with `docker system prune` to free up space.