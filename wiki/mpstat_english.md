# [Linux] C Shell (csh) mpstat用法: Monitor CPU usage statistics

## Overview
The `mpstat` command is used to report processors-related statistics, including CPU usage, which helps in monitoring the performance of the system. It provides a breakdown of CPU activity, allowing users to identify bottlenecks and optimize system performance.

## Usage
The basic syntax of the `mpstat` command is as follows:

```bash
mpstat [options] [interval] [count]
```

## Common Options
- `-P ALL`: Display statistics for all CPUs.
- `-u`: Show CPU utilization.
- `-I SUM`: Display interrupt statistics.
- `-V`: Show version information.
- `-h`: Display help information.

## Common Examples

1. **Display CPU usage for all processors:**
   ```bash
   mpstat -P ALL
   ```

2. **Monitor CPU usage every 2 seconds for 5 times:**
   ```bash
   mpstat 2 5
   ```

3. **Show CPU utilization only:**
   ```bash
   mpstat -u
   ```

4. **Display interrupt statistics:**
   ```bash
   mpstat -I SUM
   ```

5. **Check the version of mpstat:**
   ```bash
   mpstat -V
   ```

## Tips
- Use `mpstat` in combination with other monitoring tools like `top` or `vmstat` for a comprehensive view of system performance.
- Regularly monitor CPU statistics to identify trends and potential issues before they impact system performance.
- Consider using the `-h` option to familiarize yourself with additional options and features of `mpstat`.