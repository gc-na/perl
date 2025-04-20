# [Linux] C Shell (csh) free comando: Muestra la memoria del sistema

## Overview
The `free` command in C Shell (csh) is used to display the amount of free and used memory in the system. It provides a quick overview of memory usage, including physical memory, swap memory, and buffers used by the kernel.

## Usage
The basic syntax of the `free` command is as follows:

```csh
free [options] [arguments]
```

## Common Options
- `-h`: Display the memory in a human-readable format (e.g., KB, MB).
- `-m`: Show the memory usage in megabytes.
- `-g`: Show the memory usage in gigabytes.
- `-s <seconds>`: Continuously display memory usage at specified intervals.

## Common Examples
Here are some practical examples of using the `free` command:

1. **Display memory usage in the default format:**
   ```csh
   free
   ```

2. **Display memory usage in a human-readable format:**
   ```csh
   free -h
   ```

3. **Show memory usage in megabytes:**
   ```csh
   free -m
   ```

4. **Show memory usage in gigabytes:**
   ```csh
   free -g
   ```

5. **Continuously display memory usage every 5 seconds:**
   ```csh
   free -s 5
   ```

## Tips
- Use the `-h` option for a quick and easy-to-read summary of memory usage.
- Combine the `-s` option with `-h` for real-time monitoring in a human-readable format.
- Regularly check memory usage to identify potential performance issues in your system.