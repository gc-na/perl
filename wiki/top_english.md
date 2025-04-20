# [Linux] C Shell (csh) top Usage: Monitor system processes in real-time

## Overview
The `top` command is a powerful utility that provides a real-time view of the system's processes. It displays information about CPU usage, memory usage, and the processes currently running on the system, allowing users to monitor system performance and resource utilization.

## Usage
The basic syntax of the `top` command is as follows:

```csh
top [options] [arguments]
```

## Common Options
Here are some common options you can use with the `top` command:

- `-d <seconds>`: Set the delay between updates (in seconds).
- `-p <pid>`: Monitor a specific process by its process ID (PID).
- `-u <user>`: Show processes for a specific user.
- `-n <number>`: Specify the number of updates to display before exiting.

## Common Examples

1. **Run top with default settings**:
   ```csh
   top
   ```

2. **Update every 5 seconds**:
   ```csh
   top -d 5
   ```

3. **Monitor a specific process (e.g., PID 1234)**:
   ```csh
   top -p 1234
   ```

4. **Display processes for a specific user (e.g., user 'john')**:
   ```csh
   top -u john
   ```

5. **Limit the output to 10 updates**:
   ```csh
   top -n 10
   ```

## Tips
- Press `h` while in the `top` interface to view help and learn about interactive commands.
- Use `k` followed by a PID to kill a process directly from the `top` interface.
- To sort processes by CPU usage, press `Shift + P`, and for memory usage, press `Shift + M`.
- Customize the display by pressing `f` to add or remove fields according to your needs.