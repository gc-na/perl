# [Linux] C Shell (csh) dstat用法: Monitor system resources in real-time

## Overview
The `dstat` command is a versatile tool used to monitor system resources in real-time. It combines the functionality of various monitoring tools, providing detailed information about CPU, memory, disk, network, and other system metrics in a single output.

## Usage
The basic syntax of the `dstat` command is as follows:

```csh
dstat [options] [arguments]
```

## Common Options
- `-c`: Show CPU usage.
- `-d`: Display disk activity.
- `-n`: Monitor network activity.
- `-m`: Report memory usage.
- `-t`: Include a timestamp in the output.
- `--help`: Display help information for the command.

## Common Examples
Here are some practical examples of using the `dstat` command:

1. **Basic Resource Monitoring**:
   ```csh
   dstat
   ```

2. **Monitor CPU and Disk Activity**:
   ```csh
   dstat -cd
   ```

3. **View Network and Memory Usage**:
   ```csh
   dstat -nm
   ```

4. **Include Timestamps**:
   ```csh
   dstat -t
   ```

5. **Monitor All Resources**:
   ```csh
   dstat -cdnm
   ```

## Tips
- Use the `-t` option to add timestamps, which can help in correlating events with system performance.
- Combine multiple options to get a comprehensive view of system performance.
- Consider running `dstat` in a separate terminal window to keep monitoring while performing other tasks.