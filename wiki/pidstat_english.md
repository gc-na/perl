# [Linux] C Shell (csh) pidstat 使用法: Monitor process statistics

## Overview
The `pidstat` command is a useful tool for monitoring individual process statistics in real-time. It provides detailed information about CPU usage, memory consumption, and other performance metrics for running processes, making it invaluable for system administrators and developers who need to optimize performance.

## Usage
The basic syntax of the `pidstat` command is as follows:

```bash
pidstat [options] [arguments]
```

## Common Options
- `-h`: Display the output in a human-readable format.
- `-r`: Report memory usage statistics.
- `-u`: Report CPU usage statistics.
- `-p <pid>`: Specify the process ID to monitor.
- `-t`: Display statistics for threads.

## Common Examples
Here are some practical examples of how to use the `pidstat` command:

1. **Monitor CPU usage for all processes:**
   ```bash
   pidstat -u 1
   ```
   This command will display CPU usage statistics for all processes every second.

2. **Monitor memory usage for a specific process:**
   ```bash
   pidstat -r -p 1234 1
   ```
   Replace `1234` with the actual process ID. This will show memory usage statistics for the specified process every second.

3. **Monitor both CPU and memory usage:**
   ```bash
   pidstat -u -r 1
   ```
   This command will provide both CPU and memory usage statistics for all processes every second.

4. **Monitor thread statistics for a specific process:**
   ```bash
   pidstat -t -p 5678 1
   ```
   Replace `5678` with the desired process ID. This will display thread-level statistics for the specified process every second.

## Tips
- Use the `-h` option to make the output more readable, especially when dealing with large numbers.
- Combine options to get a comprehensive view of process performance; for example, using `-u -r` together.
- Regularly monitor processes during peak usage times to identify performance bottlenecks.
- Consider redirecting the output to a file for further analysis using `pidstat [options] > output.txt`.