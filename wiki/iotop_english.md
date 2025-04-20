# [Linux] C Shell (csh) iotop用法: Monitor disk I/O usage by processes

## Overview
The `iotop` command is a powerful tool that allows users to monitor disk I/O usage by processes in real-time. It provides a dynamic view of which processes are consuming the most disk resources, helping to identify bottlenecks and optimize system performance.

## Usage
The basic syntax of the `iotop` command is as follows:

```bash
iotop [options] [arguments]
```

## Common Options
- `-o`, `--only`: Show only processes or threads actually doing I/O, which can help focus on active processes.
- `-b`, `--batch`: Run in batch mode, useful for logging output to a file.
- `-n NUM`, `--iter NUM`: Set the number of iterations before exiting.
- `-d SEC`, `--delay SEC`: Set the delay between updates in seconds.

## Common Examples
Here are some practical examples of using `iotop`:

1. **Basic Usage**: Launch `iotop` to view real-time disk I/O.
   ```bash
   iotop
   ```

2. **Show Only Active Processes**: Display only the processes that are currently performing I/O.
   ```bash
   iotop -o
   ```

3. **Batch Mode for Logging**: Run `iotop` in batch mode and log the output to a file for later analysis.
   ```bash
   iotop -b -n 10 > iotop_log.txt
   ```

4. **Set Update Interval**: Change the update interval to 2 seconds.
   ```bash
   iotop -d 2
   ```

5. **Limit Iterations**: Run `iotop` for a specific number of iterations, e.g., 5.
   ```bash
   iotop -n 5
   ```

## Tips
- Use `iotop` with root privileges to ensure you can see all processes and their I/O usage.
- Combine `iotop` with other monitoring tools like `top` or `htop` for a comprehensive view of system performance.
- Regularly check for processes with high I/O usage to maintain optimal system performance and prevent slowdowns.