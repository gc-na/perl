# [Linux] C Shell (csh) docker-compose uso: Manage multi-container Docker applications

## Overview
The `docker-compose` command is a tool used to define and run multi-container Docker applications. With a simple YAML file, you can configure your application services, networks, and volumes, allowing you to manage complex setups easily.

## Usage
The basic syntax of the `docker-compose` command is as follows:

```bash
docker-compose [options] [arguments]
```

## Common Options
- `up`: Builds, (re)creates, starts, and attaches to containers for a service.
- `down`: Stops and removes containers, networks, images, and volumes created by `up`.
- `build`: Builds or rebuilds services.
- `logs`: Displays logs from containers.
- `exec`: Executes a command in a running container.
- `ps`: Lists containers associated with the project.

## Common Examples
Here are some practical examples of using `docker-compose`:

1. **Start services defined in `docker-compose.yml`:**
   ```bash
   docker-compose up
   ```

2. **Start services in detached mode (in the background):**
   ```bash
   docker-compose up -d
   ```

3. **Stop and remove all containers and networks:**
   ```bash
   docker-compose down
   ```

4. **Build or rebuild services:**
   ```bash
   docker-compose build
   ```

5. **View logs from all services:**
   ```bash
   docker-compose logs
   ```

6. **Execute a command in a specific service's container:**
   ```bash
   docker-compose exec <service_name> <command>
   ```

7. **List all running containers:**
   ```bash
   docker-compose ps
   ```

## Tips
- Always define your services in a `docker-compose.yml` file to keep your configurations organized.
- Use the `-d` option with `up` for a cleaner terminal output and to run your containers in the background.
- Regularly check logs with `docker-compose logs` to troubleshoot issues with your services.
- Use version control for your `docker-compose.yml` file to track changes and collaborate with others effectively.