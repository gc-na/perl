# [Linux] C Shell (csh) vmstat 用法: Monitor system performance

## Overview
The `vmstat` command is used to report virtual memory statistics, system processes, and CPU activity. It provides a snapshot of system performance, helping users identify potential bottlenecks and monitor resource usage over time.

## Usage
The basic syntax of the `vmstat` command is as follows:

```csh
vmstat [options] [interval] [count]
```

## Common Options
- `-a`: Show active and inactive memory.
- `-m`: Display memory statistics for slabs.
- `-s`: Display memory statistics as a summary.
- `-d`: Show disk statistics.
- `interval`: The time interval (in seconds) between updates.
- `count`: The number of updates to display.

## Common Examples
Here are some practical examples of using the `vmstat` command:

1. **Basic Usage**: Display system performance statistics every 2 seconds.
   ```csh
   vmstat 2
   ```

2. **Show Active and Inactive Memory**: Include active and inactive memory statistics.
   ```csh
   vmstat -a 2
   ```

3. **Display Memory Statistics Summary**: Get a summary of memory statistics.
   ```csh
   vmstat -s
   ```

4. **Monitor Disk Statistics**: Show disk I/O statistics.
   ```csh
   vmstat -d 2
   ```

5. **Limit Output to Specific Count**: Display performance statistics every 1 second for 5 iterations.
   ```csh
   vmstat 1 5
   ```

## Tips
- Use `vmstat` in conjunction with other monitoring tools like `top` or `iostat` for a more comprehensive view of system performance.
- Monitor `vmstat` output over time to identify trends in resource usage, which can help with capacity planning.
- Pay attention to the `si` (swap in) and `so` (swap out) columns; high values may indicate memory pressure.