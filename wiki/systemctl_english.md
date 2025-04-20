# [Linux] C Shell (csh) systemctl用法: 管理系统服务

## Overview
The `systemctl` command is a powerful utility used to examine and control the systemd system and service manager. It allows users to manage system services, check their status, start or stop them, and enable or disable them at boot time.

## Usage
The basic syntax of the `systemctl` command is as follows:

```
systemctl [options] [arguments]
```

## Common Options
- `start`: Starts a specified service.
- `stop`: Stops a specified service.
- `restart`: Restarts a specified service.
- `status`: Displays the status of a specified service.
- `enable`: Enables a service to start automatically at boot.
- `disable`: Prevents a service from starting automatically at boot.
- `list-units`: Lists all active units (services, sockets, etc.).

## Common Examples
Here are some practical examples of using the `systemctl` command:

1. **Start a service**:
   ```bash
   systemctl start nginx
   ```

2. **Stop a service**:
   ```bash
   systemctl stop nginx
   ```

3. **Restart a service**:
   ```bash
   systemctl restart nginx
   ```

4. **Check the status of a service**:
   ```bash
   systemctl status nginx
   ```

5. **Enable a service to start at boot**:
   ```bash
   systemctl enable nginx
   ```

6. **Disable a service from starting at boot**:
   ```bash
   systemctl disable nginx
   ```

7. **List all active services**:
   ```bash
   systemctl list-units --type=service
   ```

## Tips
- Always check the status of a service after starting or stopping it to ensure it is functioning as expected.
- Use `systemctl list-units` to get an overview of all active services and their states.
- Be cautious when enabling services to start at boot, as this can affect system performance and boot time.