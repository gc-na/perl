# [Linux] C Shell (csh) chkconfig用法: Manage system services

## Overview
The `chkconfig` command is used in Unix-like operating systems to manage the system services that start and stop at different run levels. It allows users to configure which services should be activated or deactivated at system startup.

## Usage
The basic syntax of the `chkconfig` command is as follows:

```csh
chkconfig [options] [service] [on|off|reset]
```

## Common Options
- `--list`: Displays the current status of all services.
- `--add`: Adds a new service to the chkconfig management.
- `--del`: Removes a service from chkconfig management.
- `--level`: Specifies the run levels for the service.
- `--help`: Displays help information for the command.

## Common Examples
1. **List all services and their statuses:**
   ```csh
   chkconfig --list
   ```

2. **Enable a service at specific run levels:**
   ```csh
   chkconfig httpd on
   ```

3. **Disable a service at specific run levels:**
   ```csh
   chkconfig httpd off
   ```

4. **Add a new service:**
   ```csh
   chkconfig --add myservice
   ```

5. **Remove a service from chkconfig management:**
   ```csh
   chkconfig --del myservice
   ```

## Tips
- Always check the current status of services with `chkconfig --list` before making changes.
- Use the `--level` option to specify which run levels you want to modify for a service.
- Be cautious when disabling critical services, as it may affect system functionality.